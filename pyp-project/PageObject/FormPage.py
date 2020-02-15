from PageObject.PageExample import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FormPage(BasePage):

    email = "//input[@placeholder=\'Email\']"
    autocomplete = "//input[@id=\'typeahead-basic\']"
    city = "//button[@id=\'ngb-typeahead-0-0\']"
    element = "//button[@id='ngb-typeahead-0-0']"
    password = "//input[@placeholder=\'Senha\']"
    select = "//select[@id=\'select-input\']"
    option = "//option[. = \'3\']"
    radio = "//input[@id=\'radios2-input\']"
    textarea = "//textarea[@id=\'textarea-input\']"
    file = "//input[@id=\'file-input\']"
    check = "//input[@id=\'check-input\']"
    signup_button = "//button[@id=\'submit-input\']"
    alert = "//ngb-alert[@class=\'alert alert-success alert-dismissible\']"
    email_miss = "//div[@class=\'invalid-feedback\']"

    def set_email(self, email):
        self._driver.find_element_by_xpath(FormPage.email).send_keys(email)

    def set_autocomplete(self, autocomplete):
        self._driver.find_element_by_xpath(FormPage.autocomplete).send_keys(autocomplete)

    def city_click(self):
        self._driver.find_element_by_xpath(FormPage.city).click()

    def set_password(self, password):
        self._driver.find_element_by_xpath(FormPage.password).send_keys(password)

    def set_select(self, select):
        self._driver.find_element_by_xpath(FormPage.select).send_keys(select)

    def option_click(self, option):
        self._driver.find_element_by_xpath(FormPage.option).click()

    def set_radio(self):
        self._driver.find_element_by_xpath(FormPage.radio).click()

    def set_textarea(self, textarea):
        self._driver.find_element_by_xpath(FormPage.textarea).send_keys(textarea)

    def set_file(self, file):
        self._driver.find_element_by_xpath(FormPage.file).send_keys(file)

    def click_check(self):
        self._driver.find_element_by_xpath(FormPage.check).click()

    def click_signup_button(self):
        self._driver.find_element_by_xpath(FormPage.signup_button).click()

    def get_alert(self, alert):
        return self._driver.find_element_by_xpath(FormPage.alert).text

    def email_warning(self):
        return self._driver.find_element_by_xpath(FormPage.email_miss).text

    def wait_element(self):
       element = WebDriverWait.until(EC.element_to_be_clickable((By.XPATH, FormPage.element)))

    def get_select(self):
        select = self._driver.find_element_by_xpath(FormPage.select)
        return select

    def get_all_option(self):
        all_options = self._driver.find_elementens_by_tagName("options")
        return all_options

