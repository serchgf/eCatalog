import logging
import os
import pathlib
import time
import json

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys

from src.page_objects.home_page import HomePage
from src.page_objects.base_page import images

_JSON_PATH = os.path.join(pathlib.Path(__file__).parent.parent, "locators", "HomePage.json")


# --------------------------------------------SERGIO GARCIA---------------------------------------------------------------
# PDP Visualize Product Details Page-------------------------------------------------------------------------------------------------------------

# MXTEST-10418
#@pytest.mark.phase2_sp1
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10418_PDP_Video_Preview(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/search/detail/moog-suspension-control-arm-and-ball-joint-assembly-ck620054/mym0/ck620054?q=ck620054"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.click_resources_tab()
    home_page.wait_spinner_disappears()
    home_page.click_on_video()
    home_page.take_screenshot("reproducing video")


# MXTEST-10419
#@pytest.mark.phase2_sp1
@pytest.mark.flaky(reruns=1)
def test_MXTEST_10419_PDP_With_No_video_Resource(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/search/detail/dupli-color-scratch-fix-all-in-1-0.5-ounce-metallic-steel-blue-touch-up-paint-acc0408/dpli/acc0408?q=acc0408"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.click_resources_tab()
    home_page.wait_spinner_disappears()
    home_page.press_PageDown_key()
    # CREAR FUNCION QUE VALIDE QUE NO ES VISIBLE EL VIDEO
    assert home_page.validate_hidden_video_resource(), "This video resource should not be visible"
    home_page.take_screenshot("video no exists as expected")


# MXTEST-10420
@pytest.mark.phase2_sp1
@pytest.mark.flaky(reruns=1)
def test_MXTEST_10420_FAQ_Top_Answer(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.wait_spinner_disappears()
    home_page.click_help_center()
    home_page.validate_help_center_page()
    home_page.scroll_to_element("hcp_all_faq_btn")
    faq_titles = home_page.element("hcp_faq_titles").find_elements()
    assert len(faq_titles) == 5, "The page should display 5 frequently asked questions"
    faq_titles[0].click()
    home_page.element("hcp_faq_answer").wait_visible()
    faq_titles[2].click()
    home_page.element("hcp_faq_answer").wait_visible()

# MXTEST-10421
@pytest.mark.phase2_sp1
@pytest.mark.flaky(reruns=1)
def test_MXTEST_10421_FAQ_All_Answer(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.wait_spinner_disappears()
    home_page.click_help_center()
    home_page.validate_help_center_page()
    home_page.scroll_to_element("hcp_all_faq_btn")
    faq_5_titles = home_page.element("hcp_faq_titles").find_elements()
    assert len(faq_5_titles) == 5, "The page should display 5 frequently asked questions"
    home_page.element("hcp_all_faq_btn").find_element().click()
    faq_all_titles = home_page.element("hcp_faq_titles").find_elements()
    assert len(faq_all_titles) >= 18, "The page should display 18 frequently asked questions"

# MXTEST-10422
@pytest.mark.phase2_sp1
@pytest.mark.flaky(reruns=1)
def test_MXTEST_10422_HelpCenter_ReportIncident(web_drivers):

    text = """Lorem ipsum dolor sit amet consectetur adipiscing elit, 
semper pulvinar ad cubilia turpis porta, varius leo nisi hendrerit hac 
morbi. Tortor nostra senectus molestie malesuada conubia commodo ultricies 
facilisis elementum, placerat nulla sollicitudin sociis interdum lectus 
vestibulum magna est montes, rhoncus consequat platea ornare condimentum per 
proin turpis. Leo proin ut ante orci accumsan parturient gravida dapibus nascetur, 
id himenaeos sodales inceptos pharetra vehicula sociis vivamus, lacinia hac 
pulvinar aliquet montes torquent mollis nam. conubia nunc semper turpis tortor 
dapibus nisi, tellus et quis pellentesque sollicitudin, felis senectus hendrerit 
suspendisse dictumst. Ac tristique augue proin netus turpis eget metus mollis porta 
litora, id volutpat felis sodales integer at curabitur iaculis et bibendum, vehicula 
feugiat natoque pretium cras taciti quisque vitae consequat. Mollis potenti nascetur 
habitant natoque fringilla feugiat hac etiam commodo, conubia nunc eu.
"""
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.wait_spinner_disappears()
    home_page.click_help_center()
    home_page.validate_help_center_page()
    home_page.element("hcp_issue_report").find_element().click()
    home_page.validate_issue_report_modal()
    home_page.element("irm_employId").wait_visible().send_keys("3805", Keys.ENTER)  #
    home_page.select_incident_type()
    home_page.select_frequency()
    home_page.scroll_to_element("irm_submit_btn")
    home_page.element("irm_description").find_element().send_keys(text)
    home_page.element("irm_add_file").find_element().send_keys(os.path.abspath(images.pic3))
    home_page.element("irm_form").find_element().submit()
    home_page.element("irm_send_notification").wait_visible()

# MXTEST-10423
@pytest.mark.phase2_sp1
#@pytest.mark.flaky(reruns=1)
def test_MXTEST_10423_HelpCenter_InvalidEmail(web_drivers):
    text = """Lorem ipsum dolor sit amet consectetur adipiscing elit, 
semper pulvinar ad cubilia turpis porta, varius leo nisi hendrerit hac 
morbi. Tortor nostra senectus molestie malesuada conubia commodo ultricies 
facilisis elementum, placerat nulla sollicitudin sociis interdum lectus 
vestibulum magna est montes, rhoncus consequat platea ornare condimentum per 
proin turpis. Leo proin ut ante orci accumsan parturient gravida dapibus nascetur, 
id himenaeos sodales inceptos pharetra vehicula sociis vivamus, lacinia hac 
pulvinar aliquet montes torquent mollis nam. conubia nunc semper turpis tortor 
dapibus nisi, tellus et quis pellentesque sollicitudin, felis senectus hendrerit 
suspendisse dictumst. Ac tristique augue proin netus turpis eget metus mollis porta 
litora, id volutpat felis sodales integer at curabitur iaculis et bibendum, vehicula 
feugiat natoque pretium cras taciti quisque vitae consequat. Mollis potenti nascetur 
habitant natoque fringilla feugiat hac etiam commodo, conubia nunc eu.
"""
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.wait_spinner_disappears()
    home_page.click_help_center()
    #home_page.wait_spinner_disappears()
    home_page.validate_help_center_page()
    home_page.element("hcp_issue_report").find_element().click()
    home_page.validate_issue_report_modal()
    home_page.element("irm_employId").wait_visible().send_keys("4050", Keys.ENTER)
    home_page.element("irm_employeeEmail").wait_clickable().send_keys("a@b", Keys.ENTER)
    email_error = home_page.element("irm_error_msg").wait_visible().text
    assert email_error == "Por favor, escribe un correo electrónico válido", "The invalid email message is not displayed in page"
    home_page.element("irm_employeeEmail").wait_visible().clear()
    home_page.element("irm_employeeEmail").wait_visible().send_keys("juan@gmail.com", Keys.ENTER)
    assert email_error == "Por favor, escribe un correo electrónico válido", "The invalid email message is not displayed in page"
    home_page.element("irm_employeeEmail").wait_visible().clear()
    home_page.element("irm_employeeEmail").wait_visible().send_keys("juan.larios@oreillyauto.mx", Keys.ENTER)
    home_page.select_incident_type()
    home_page.select_frequency()
    home_page.scroll_to_element("irm_submit_btn")
    home_page.element("irm_description").find_element().send_keys(text)
    home_page.element("irm_add_file").find_element().send_keys(os.path.abspath(images.pic3))
    home_page.element("irm_form").find_element().submit()
    messages = [message.text for message in home_page.element("irm_error_msg").find_elements()]
    assert home_page.validate_error_messages(messages) == 0, "The modal should not display any error message"
    home_page.element("irm_send_notification").wait_visible()


# MXTEST-10424
@pytest.mark.phase2_sp1
@pytest.mark.flaky(reruns=1)
def test_MXTEST_10424_HelpCenter_ErrorWhenReporting(web_drivers):

    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.wait_spinner_disappears()
    home_page.click_help_center()
    #home_page.wait_spinner_disappears()
    home_page.validate_help_center_page()
    home_page.element("hcp_issue_report").find_element().click()
    home_page.validate_issue_report_modal()
    home_page.scroll_to_element("irm_submit_btn")
    home_page.element("irm_submit_btn").find_element().click()
    messages = [message.text for message in home_page.element("irm_error_msg").find_elements()]
    assert home_page.validate_error_messages(messages) > 0, "The modal should display at least one error message"
    home_page.scroll_to_element("irm_employId")
    home_page.element("irm_employId").wait_visible().send_keys("3805", Keys.ENTER)  #
    home_page.select_incident_type()
    home_page.element("irm_description").find_element().send_keys(" ")
    home_page.element("irm_add_file").find_element().send_keys(os.path.abspath(images.pic1))
    assert home_page.element("irm_upload_error_msg").wait_visible().text == "error Solo se permiten archivos de hasta 2 MB.", "The upload size error message does not appear on the page"
    home_page.element("irm_upload_error_msg").wait_until_disappears()
    home_page.clear_img_input()
    home_page.element("irm_add_file").find_element().send_keys(os.path.abspath(images.pic2))
    home_page.element("irm_submit_btn").find_element().click()
    messages = [message.text for message in home_page.element("irm_error_msg").find_elements()]
    assert home_page.validate_error_messages(messages) > 0, "The modal should display at least one error message"




# General System Functionality-------------------------------------------------------------------------------------------------------------

# MXTEST-10425
@pytest.mark.phase2_sp1
@pytest.mark.flaky(reruns=1)
def test_MXTEST_10425_HelpCenter_Video_assistance(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.wait_spinner_disappears()
    home_page.click_help_center()
    #home_page.wait_spinner_disappears()
    home_page.validate_help_center_page()
    home_page.scroll_to_element("hcp_video_title")
    title_txt = home_page.get_video_titles()
    window_title = home_page.select_random_video()
    assert window_title in title_txt, f"The title of the new window should be one of this {title_txt}"
    home_page.close()
    home_page.back_to_window()
    home_page.element("hcp_all_videos_btn").find_element().click()
    title_txt = home_page.get_video_titles()
    window_title = home_page.select_random_video()
    assert window_title.upper() in title_txt, f"The title of the new window should be one of this {title_txt}"


# MXTEST-10426
#@pytest.mark.phase2_sp1
@pytest.mark.flaky(reruns=1)
def test_MXTEST_10426_RelatedCarrousel_Product(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    search_criteria = "8199"
    home_page.search_and_enter(search_criteria)
    home_page.wait_spinner_disappears()
    product_list = home_page.get_link_product_list()
    home_page.clic_javacript(product_list[0])
    home_page.wait_spinner_disappears()
    home_page.click_details_tab()
    home_page.click_random_related_product()
    home_page.wait_spinner_disappears()


# MXTEST-10427
@pytest.mark.phase2_sp1
#@pytest.mark.flaky(reruns=1)
def test_MXTEST_10427_RelatedCarrousel_Category(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    search_criteria = "8199"
    home_page.search_and_enter(search_criteria)
    home_page.wait_spinner_disappears()
    product_list = home_page.get_link_product_list()
    home_page.clic_javacript(product_list[0])
    home_page.wait_spinner_disappears()
    home_page.click_details_tab()
    home_page.press_PageDown_key()
    home_page.press_PageDown_key()
    home_page.wait_spinner_disappears()
    home_page.press_PageDown_key()
    home_page.click_random_related_Category()
    home_page.wait_spinner_disappears()

# MXTEST-10428
#@pytest.mark.phase2_sp1
#@pytest.mark.flaky(reruns=1)
def test_MXTEST_10428_PDP_Article_WITHOUT_Related_Categories(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    search_criteria = "dr1040"
    home_page.search_and_enter(search_criteria)
    home_page.wait_spinner_disappears()
    product_list = home_page.get_link_product_list()
    home_page.clic_javacript(product_list[0])
    home_page.wait_spinner_disappears()
    home_page.click_details_tab()
    home_page.press_PageDown_key()
    home_page.press_PageDown_key()
    home_page.validate_hidden_related_cateogory()

# MXTEST-10429
#@pytest.mark.phase2_sp1
#@pytest.mark.flaky(reruns=1)
def test_MXTEST_10429_PDP_Article_WITHOUT_Related_products(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    search_criteria = "dr1040"
    home_page.search_and_enter(search_criteria)
    home_page.wait_spinner_disappears()
    product_list = home_page.get_link_product_list()
    home_page.clic_javacript(product_list[0])
    home_page.wait_spinner_disappears()
    home_page.click_details_tab()
    home_page.press_PageDown_key()
    home_page.press_PageDown_key()
    home_page.validate_hidden_related_product()
