import logging
import os
import pathlib
import time
import json

import pytest
from selenium.common import TimeoutException

from src.page_objects.home_page import HomePage

_JSON_PATH = os.path.join(pathlib.Path(__file__).parent.parent, "locators", "HomePage.json")


# --------------------------------------------SERGIO GARCIA---------------------------------------------------------------
# PDP Visualize Product Details Page-------------------------------------------------------------------------------------------------------------

# MXTEST-10418
@pytest.mark.phase2_sp1
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10418_PDP_Video_Preview(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/search/detail/moog-suspension-control-arm-and-ball-joint-assembly-ck620054/mym0/ck620054?q=ck620054"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.click_resources_tab()
    home_page.wait_spinner_disappears()
    # click on video

    home_page.take_screenshot("reproducing video")


# MXTEST-10419
@pytest.mark.phase2_sp1
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10419_PDP_With_No_video_Resource(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/search/detail/dupli-color-scratch-fix-all-in-1-0.5-ounce-metallic-steel-blue-touch-up-paint-acc0408/dpli/acc0408?q=acc0408"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.click_resources_tab()
    home_page.wait_spinner_disappears()
    # CREAR FUNCION QUE VALIDE QUE NO ES VISIBLE EL VIDEO

    home_page.take_screenshot("video no exists as expected")


# MXTEST-10420

# MXTEST-10421

# MXTEST-10422

# MXTEST-10423

# MXTEST-10424

# General System Functionality-------------------------------------------------------------------------------------------------------------

# MXTEST-10425

# MXTEST-10426
@pytest.mark.phase2_sp1
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10426_RelatedCarrousel_Product(web_drivers):
    pass

# MXTEST-10427

# MXTEST-10428

# MXTEST-10429