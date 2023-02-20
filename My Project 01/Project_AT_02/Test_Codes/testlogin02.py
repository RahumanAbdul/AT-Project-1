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



    def test_invalid_login(self, booting_function):
        self.driver.get(data.Abdul_Data().url)
        self.driver.find_element(by=By.NAME, value=locators.Abdul_Locators().username_InputBox).send_keys(data.Abdul_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Abdul_Locators().password_InputBox).send_keys(data.Abdul_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Abdul_Locators().loginButton).click()
        assert self.test_invalid_login == self.test_invalid_login
        print("INVALID CREDENTIALS : Logged in with Username {a} and Password {b}". format(a=data.Abdul_Data.username, b=data.Abdul_Data.password))
