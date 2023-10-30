import time

from src.page_objects.product_page import ProductPage


def test_create_a_review_product(web_drivers):
    name = "Cheems"
    review_txt = "very nice product, I love it!! 100% recomended"
    product_page = ProductPage(*web_drivers)
    product_page.open()
    product_page.click_on_write_a_review_link()
    product_page.write_a_review(name, review_txt)
    product_page.rate_the_product(4)
    product_page.click_on_continue_btn()
    expected_message = "Thank you for your review. It has been submitted to the webmaster for approval."
    actual_message = product_page.get_alert_message()
    assert expected_message == actual_message, f"Search text: {expected_message}, should be displayed"
    product_page.take_screenshot("test_create_a_review_product")
