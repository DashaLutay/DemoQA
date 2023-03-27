from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time


def test_check_title_demo(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)

