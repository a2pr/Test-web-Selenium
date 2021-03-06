import unittest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_something(self):
        self.driver.get("https://testingandplay.com/example/form")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("qweqweqweqwe")
        self.assertIn("Email inválido", self.driver.find_element_by_xpath("//div[@class =\'invalid-feedback\']").text)
        autocomplete = self.driver.find_element(By.XPATH, "//input[@id=\'typeahead-basic\']")
        autocomplete.send_keys("ala")
        self.driver.find_element(By.XPATH, "//button[@id=\'ngb-typeahead-0-0\']").click()
        self.driver.find_element(By.ID, "select-input").click()
        dropdown = self.driver.find_element(By.ID, "select-input")
        dropdown.find_element(By.XPATH, "//option[. = '3']").click()
        dropdown = self.driver.find_element(By.ID, "select-input")
        dropdown.find_element(By.XPATH, "//option[. = '2']").click()
        self.driver.find_element(By.ID, "select-input").click()
        self.driver.find_element(By.ID, "textarea-input").click()
        self.driver.find_element(By.ID, "textarea-input").send_keys("Hello there SMOSH GAMES")
        file = self.driver.find_element_by_xpath("//input[@id=\'file-input\']")
        file.send_keys("C:/Users/A2PR/Desktop/Test-web-Selenium/pyp-project/test.txt")
        self.driver.find_element(By.ID, "radios2-input").click()
        self.driver.find_element(By.ID, "check-input").click()
        self.driver.find_element(By.ID, "submit-input").click()
        self.assertIn("Formulário inválido\n×", self.driver.find_element_by_xpath(
            "//ngb-alert[@class=\'alert alert-danger alert-dismissible\']").text)


    def testWithWrongEmailFormat(self):
        google = self.driver
        google.get("https://testingandplay.com/example/form")
        google.set_window_size(974, 938)
        email = google.find_element(By.NAME, "email")
        email.click()
        email.send_keys("qqqqq")
        google.find_element(By.ID, "radios2-input").click()
        self.assertIn("Email inválido.", google.find_element_by_xpath(
            "//div[@class=\'invalid-feedback\']").text)

    def testCadastroWithWrongEmailFormat(self):
        self.driver.get("https://www.testingandplay.com/example/form")
        self.driver.set_window_size(1094, 584)
        email = self.driver.find_element(By.NAME, "email")
        email.click()
        email.send_keys("qqqqq")
        autocomplete = self.driver.find_element(By.XPATH, "//input[@id=\'typeahead-basic\']")
        autocomplete.send_keys("ala")
        self.driver.find_element(By.XPATH, "//button[@id=\'ngb-typeahead-0-0\']").click()
        self.driver.find_element(By.ID, "select-input").click()
        dropdown = self.driver.find_element(By.ID, "select-input")
        dropdown.find_element(By.XPATH, "//option[. = '3']").click()
        self.driver.find_element(By.ID, "select-input").click()
        self.driver.find_element(By.ID, "textarea-input").click()
        self.driver.find_element(By.ID, "textarea-input").send_keys("loremp ipson somthing")
        file_input = self.driver.find_element_by_xpath("//input[@id=\'file-input\']")
        file_input.send_keys("C:/Users/A2PR/Desktop/Test-web-Selenium/pyp-project/test.txt")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.ID, "radios2-input").click()
        self.driver.find_element(By.ID, "check-input").click()
        self.driver.find_element(By.ID, "submit-input").click()

        self.assertIn("Email inválido.", self.driver.find_element_by_xpath(
            "//div[@class=\'invalid-feedback\']").text)

        self.assertIn("Formulário inválido\n×",  self.driver.find_element_by_xpath("//ngb-alert[@class=\'alert alert-danger alert-dismissible\']").text)


    def testCadastroWithEmailUsingOnlyDomain(self):
        self.driver.get("https://www.testingandplay.com/example/form")
        self.driver.set_window_size(1094, 584)
        email = self.driver.find_element(By.NAME, "email")
        email.click()
        email.send_keys("@gmail.com")
        autocomplete = self.driver.find_element(By.XPATH, "//input[@id=\'typeahead-basic\']")
        autocomplete.send_keys("ala")
        self.driver.find_element(By.XPATH, "//button[@id=\'ngb-typeahead-0-0\']").click()
        self.driver.find_element(By.ID, "select-input").click()
        dropdown = self.driver.find_element(By.ID, "select-input")
        dropdown.find_element(By.XPATH, "//option[. = '3']").click()
        self.driver.find_element(By.ID, "select-input").click()
        self.driver.find_element(By.ID, "textarea-input").click()
        self.driver.find_element(By.ID, "textarea-input").send_keys("loremp ipson somthing")
        file_input = self.driver.find_element_by_xpath("//input[@id=\'file-input\']")
        file_input.send_keys("C:/Users/A2PR/Desktop/Test-web-Selenium/pyp-project/test.txt")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.ID, "radios2-input").click()
        self.driver.find_element(By.ID, "check-input").click()
        self.driver.find_element(By.ID, "submit-input").click()

        self.assertIn("Email inválido.", self.driver.find_element_by_xpath(
            "//div[@class=\'invalid-feedback\']").text)

        self.assertIn("Formulário inválido\n×",  self.driver.find_element_by_xpath("//ngb-alert[@class=\'alert alert-danger alert-dismissible\']").text)


    def testCadastroWithEmailUsingOnlySpecialChar(self):
        self.driver.get("https://www.testingandplay.com/example/form")
        self.driver.set_window_size(1094, 584)
        email = self.driver.find_element(By.NAME, "email")
        email.click()
        email.send_keys("@")
        autocomplete = self.driver.find_element(By.XPATH, "//input[@id=\'typeahead-basic\']")
        autocomplete.send_keys("ala")
        self.driver.find_element(By.XPATH, "//button[@id=\'ngb-typeahead-0-0\']").click()
        self.driver.find_element(By.ID, "select-input").click()
        dropdown = self.driver.find_element(By.ID, "select-input")
        dropdown.find_element(By.XPATH, "//option[. = '3']").click()
        self.driver.find_element(By.ID, "select-input").click()
        self.driver.find_element(By.ID, "textarea-input").click()
        self.driver.find_element(By.ID, "textarea-input").send_keys("loremp ipson somthing")
        file_input = self.driver.find_element_by_xpath("//input[@id=\'file-input\']")
        file_input.send_keys("C:/Users/A2PR/Desktop/Test-web-Selenium/pyp-project/test.txt")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.ID, "radios2-input").click()
        self.driver.find_element(By.ID, "check-input").click()
        self.driver.find_element(By.ID, "submit-input").click()

        self.assertIn("Email inválido.", self.driver.find_element_by_xpath(
            "//div[@class=\'invalid-feedback\']").text)

        self.assertIn("Formulário inválido\n×",  self.driver.find_element_by_xpath("//ngb-alert[@class=\'alert alert-danger alert-dismissible\']").text)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
