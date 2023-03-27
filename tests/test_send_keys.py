from pages.form_page import FormPage
from pages.elements_page import ElementsPage
import time


def test_send_keys(browser):
    form_page = FormPage(browser)
    form_page.visit()
    form_page.first_name.send_keys('Dasha')
    time.sleep(3)
