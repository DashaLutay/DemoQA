from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement


class FormPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DemoQa'
        }
        self.first_name = WebElement(self.driver, '#firstName')



