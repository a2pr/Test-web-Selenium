# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from PageObject.FormPage import FormPage
from PageObject.data import User #dados de teste
from selenium.webdriver.support.ui import WebDriverWait

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver")
        self.driver.get("https://testingandplay.com/example/form")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def testEmailMandatory(self):
        self.driver.implicitly_wait(500)
        form_page = FormPage(self.driver)
        form_page.set_email(User.emptyEmail)
        form_page.set_autocomplete(User.autocomplete)
        form_page.city_click()
        self.assertIn(User.emailMandatorio, form_page.email_warning())


    def test_form_success(self):
        form_page =FormPage(self.driver)
        form_page.set_email(User.email)
        form_page.set_autocomplete(User.autocomplete)
        wait = WebDriverWait(self.driver, 20)
        form_page.wait_element()
        form_page.city_click()
        select = form_page.get_select()
        all_options = form_page.get_all_option()

        for option in all_options:
            if option.text == User.option3:
                option.click()
        form_page.set_textarea(User.textarea)
        form_page.set_file(User.file)
        form_page.set_password(User.password)
        form_page.set_radio()
        form_page.click_check()
        form_page.click_signup_button()

        self.assertIn(User.cadastrarSucesso, FormPage.get_alert())
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
