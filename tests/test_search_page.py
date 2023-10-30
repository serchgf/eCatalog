from src.page_objects.search_page import SearchPage


def test_validate_search_criteria_text_label(web_drivers):
    search_page = SearchPage(*web_drivers)
    search_page.open()
    search_text = 'Iphone'
    search_page.search(search_text)

    search_criteria_msg_in_label = search_page.get_search_criteria_label_msg()
    assert search_text in search_criteria_msg_in_label, f"Search text: {search_text}, should be in the search label"
    #search_page.take_screenshot("test_validate_search_criteria_text_label")
