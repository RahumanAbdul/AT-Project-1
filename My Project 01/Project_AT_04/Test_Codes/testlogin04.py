from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from Test_Locators import locators
from Test_Data import data
import pytest


class Test_Abdul:

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(5)
        yield
        self.driver.close()


    def test_edit_employee_information(self, booting_function):
        self.driver.get(data.Abdul_Data().url)
        self.driver.find_element(by=By.NAME, value=locators.Abdul_Locators().username_InputBox).send_keys(data.Abdul_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Abdul_Locators().password_Inputbox).send_keys(data.Abdul_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Abdul_Locators().LoginButton).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.XPATH, value=locators.Abdul_Locators().PimModule_Locator).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.XPATH, value=locators.Abdul_Locators().Employeeid_InputBox).send_keys(data.Abdul_Data().Employeeid)
        self.driver.find_element(by=By.XPATH, value=locators.Abdul_Locators().SearchButton).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.XPATH, value=locators.Abdul_Locators().EditButton).click()
        self.driver.find_element(by=By.NAME, value=locators.Abdul_Locators().FirstName_InputBox).send_keys(data.Abdul_Data().FirstName)
        self.driver.find_element(by=By.XPATH, value=locators.Abdul_Locators().SaveButton).click()
        assert self.test_edit_employee_information == self.test_edit_employee_information
        print("SUCCESSFULLY UPDATED")
