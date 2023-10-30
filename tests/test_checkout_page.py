import time

import pytest

from src.page_objects.checkout_page import CheckoutPage


def test_guest_checkout(web_drivers):
    user_data = {"first_name": "Jhon",
                 "last_name": "Weak",
                 "email": "thats_my_dog@ytu.com",
                 "telephone": "1234567890",
                 "postcode": "38080",
                 "city": "Guadalajara",
                 "country": "Mexico",
                 "address": "Avenida siempre viva",
                 "state": "Jalisco",
                 "comment": "llamar cuando este por llegar"}
    checkout_page = CheckoutPage(*web_drivers)
    checkout_page.open()
    search_text = 'Iphone'
    checkout_page.search(search_text)
    checkout_page.click_on_iphone_link()
    checkout_page.click_add_to_cart()
    checkout_page.click_on_checkout_btn()
    checkout_page.click_on_guest_radio_btn()
    checkout_page.click_on_continue_btn()
    checkout_page.fill_register(user_data)
    title_expected = expected_message = "Your order has been placed!"
    assert checkout_page.get_h1_success_message(expected_message)
    assert title_expected == checkout_page.get_title()
    checkout_page.take_screenshot("test_guest_checkout")
