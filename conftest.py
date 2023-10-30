import logging
import os.path
import pathlib
import datetime
import shutil

import pytest

from src.factory.webdriver_factory import get_drivers

_SCREENSHOT_PATH = os.path.join(pathlib.Path(__file__).parent, "Screenshots")
_REPORTS_PATH = os.path.join(pathlib.Path(__file__).parent, "Reports")
_LOGS_PATH = os.path.join(pathlib.Path(__file__).parent, "logs")


@pytest.fixture(autouse=True)
def web_drivers(request):
    caller = request.node.name
    driver, wait_driver = get_drivers()
    report_directory_path = create_report_directory()
    if not os.path.exists(os.path.join(report_directory_path)):
        os.makedirs(report_directory_path)
    yield driver, wait_driver
    try_take_screenshot(driver, caller)
    move_to_report_dir(_SCREENSHOT_PATH, report_directory_path)
    driver.quit()

def try_take_screenshot(driver, test_name):
    try:
        file_path = os.path.join(_SCREENSHOT_PATH, f"{test_name}.png")
        driver.save_screenshot(file_path)
    except:
        logging.error(f"cannot save screenshot after execution of {test_name}")


def create_report_directory():
    logging.info("Creating Report Directory")
    main_report_dir = 'Reports/eCatalog_' + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M/")
    """main_report_dir = 'images_report/SGE_PO_Test_report ' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S/")"""
    return main_report_dir


def move_to_report_dir(file_source, path_to_move):
    logging.info("Move to report directory")
    file_source = file_source+'/'
    file_destination = path_to_move
    get_files = os.listdir(file_source)
    logging.info(f"numero de archivos en Screenshots: {len(get_files)}")
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
