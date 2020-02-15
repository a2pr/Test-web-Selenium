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

    def testWithoutPassFill(self):
        google = self.driver
        self.driver.get("https://testingandplay.com/example/form")
        self.driver.set_window_size(974, 938)
        password = self.driver.find_element(By.NAME, "password")
        password.click()
        password.send_keys("")
        self.driver.find_element(By.ID, "radios2-input").click()
        self.assertIn("Senha obrigatória", self.driver.find_element_by_xpath(
            "//div[@class=\'invalid-feedback\']").text)

    def testWithoutEmailFill(self):
        google = self.driver
        self.driver.get("https://testingandplay.com/example/form")
        self.driver.set_window_size(974, 938)
        email = self.driver.find_element(By.NAME, "email")
        email.click()
        email.send_keys("")
        self.driver.find_element(By.ID, "radios2-input").click()
        self.assertIn("Email obrigatório.", self.driver.find_element_by_xpath(
            "//div[@class=\'invalid-feedback\']").text)

    def testWithoutRequired(self):
        google = self.driver
        self.driver.get("https://testingandplay.com/example/form")
        self.driver.set_window_size(974, 938)
        autocomplete = self.driver.find_element(By.XPATH, "//input[@id=\'typeahead-basic\']")
        autocomplete.send_keys("ala")
        self.driver.find_element(By.XPATH, "//button[@id=\'ngb-typeahead-0-0\']").click()
        self.driver.find_element(By.XPATH, "//select[@id=\'select-input\']").click()
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
        self.assertIn("Formulário inválido\n×",
                      self.driver.find_element_by_xpath("//ngb-alert[@class=\'alert alert-danger alert-dismissible\']").text)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
