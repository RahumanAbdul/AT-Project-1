from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from Test_Locators import locators
from Test_Data import data
import pytest

class Test_Abdul:

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()



    def test_delete_employee(self, booting_function):
        self.driver.get(data.Abdul_Data().url)
        self.driver.find_element(by=By.NAME, value=locators.Abdul_Locators().username_InputBox).send_keys(data.Abdul_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Abdul_Locators().password_InputBox).send_keys(data.Abdul_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Abdul_Locators().LoginButton).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.XPATH, value=locators.Abdul_Locators().PimModule_Locator).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.XPATH, value=locators.Abdul_Locators().Employeeid_InputBox).send_keys(data.Abdul_Data().Employeeid)
        self.driver.find_element(by=By.XPATH, value=locators.Abdul_Locators().SearchButton).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.XPATH, value=locators.Abdul_Locators().IDcheckbox_Locator).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.XPATH, value=locators.Abdul_Locators().DeleteButton).click()
        self.driver.find_element(by=By.XPATH, value=locators.Abdul_Locators().YesButton).click()
        assert self.test_delete_employee == self.test_delete_employee
        print("SUCCESSFULLY DELETED")