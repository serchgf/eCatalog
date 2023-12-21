import logging
import os.path
import pathlib
import datetime
import shutil
from py.xml import html
import allure
import pytest
from allure_commons.types import AttachmentType

from src.factory.webdriver_factory import get_drivers

_SCREENSHOT_PATH = os.path.join(pathlib.Path(__file__).parent, "screenshots")
_REPORTS_PATH = os.path.join(pathlib.Path(__file__).parent, "Reports")
_LOGS_PATH = os.path.join(pathlib.Path(__file__).parent, "logs")
_REPORT_DATETIME = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M/")



@pytest.fixture(autouse=True)
def web_drivers(request):

    caller = request.node.name
    driver, wait_driver = get_drivers()
    report_directory_path = create_report_directory()
    if not os.path.exists(os.path.join(report_directory_path)):
        os.makedirs(report_directory_path)
    if not os.path.exists(os.path.join(_SCREENSHOT_PATH)):
        os.makedirs(_SCREENSHOT_PATH)
    if not os.path.exists(os.path.join(_LOGS_PATH)):
        os.makedirs(_LOGS_PATH)
    yield driver, wait_driver
    try_take_screenshot(driver, caller)
    move_to_report_dir(_SCREENSHOT_PATH, report_directory_path)
    driver.quit()


def try_take_screenshot(driver, test_name):
    try:
        file_path = os.path.join(_SCREENSHOT_PATH, f"{test_name}.png")
        driver.save_screenshot(file_path)
        allure.attach(driver.get_screenshot_as_png(), name=f"{test_name}.png", attachment_type=AttachmentType.PNG)
    except:
        logging.error(f"cannot save screenshot after execution of {test_name}")
        return test_name


def create_report_directory():
    logging.info("Creating Report Directory")
    # main_report_dir = 'Reports/eCatalog_' + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M/")
    main_report_dir = 'Reports/eCatalog_' + _REPORT_DATETIME
    return main_report_dir


def move_to_report_dir(file_source, path_to_move):
    logging.info("Move to report directory")
    file_source = file_source+'/'
    file_destination = path_to_move
    get_files = os.listdir(file_source)
    logging.info(f"numero de archivos en screenshots: {len(get_files)}")
    if len(get_files) == 0 or len(get_files) is None:
        logging.info("No image to move")
    else:
        for f in get_files:
            try:
                shutil.move(file_source + f, file_destination + f)
            except:
             logging.info("Error, img no moved or not exist")

    log_files = os.listdir(_LOGS_PATH)
    log_file_source = _LOGS_PATH+'/'
    if len(log_files) == 0 or len(log_files) is None:
        logging.info("No log to move")
    else:
        for f in log_files:
            try:
                shutil.move(log_file_source + f, file_destination + f)
            except:
                pass
    return file_destination



#agregue config
def pytest_configure(config):
    # to remove environment section
    config._metadata = None
    report_directory_path = create_report_directory()
    config.option.htmlpath = f"{report_directory_path}eCatalog_Test_Report.html"
    config.option.imagepath = report_directory_path

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    print(str(item))
    html_path = str(item.config.option.imagepath)

    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield

    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        # always add url to images_report
        xfail = hasattr(report, "wasxfail")
        # if (images_report.skipped and xfail) or (images_report.failed and not xfail):
        # only add additional html on failure
        message = "_Error" if report.failed else "_Successful"

        # img_name = sge_fun.obtener_fecha() + message + ".png"
        #img_name = item.name + message + ".png"

        img_name = item.name + ".png"
        report_directory_path = 'Reports/eCatalog_' + _REPORT_DATETIME
        new_path_img = move_to_report_dir(_SCREENSHOT_PATH, report_directory_path)
        main_dir = str(pathlib.Path(new_path_img).resolve().parents[1])
        extra.append(pytest_html.extras.html("additional html" + f"{main_dir}/{new_path_img}{img_name}"))
        #image = f"{new_path_img}{img_name}"
        image = f"{img_name}"
        print("image source en new_path_img img_name")
        insert_img = str(
            f'<div class="image"><a class="image" href="{image}" target="_blank"><img src="{image}"></a></div>')
        extra.append(pytest_html.extras.html(insert_img))
        report.extras = extra

def pytest_html_report_title(report):
    report.title = f"eCatalog Report {_REPORT_DATETIME.replace('/','')}"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(
        [html.img(src="../../image_files/logo_oreilly.png", style="right:8%; height:240px; top:0; position:fixed;")])

