from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from data.global_data import GlobalData
from utilities.base_class import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        """
        Constructor for LoginPage class.
        Args:
            driver: WebDriver instance for interacting with the web browser.
        """
        self.driver = driver

    login_btn_locator = (By.XPATH, "//button[@data-testid='login-button']")
    email_locator = (By.XPATH, "//div[@data-testid='login-email']/div/input")
    password_locator = (By.XPATH, "//input[@id=':r2:']")
    welcome_locator = (By.XPATH, "//h2")

    def get_login_btn(self):
        """
        Get the login button element.
        Returns:
            WebElement: The login button element.
        """
        return self.driver.find_element(*self.login_btn_locator)

    def get_email_input_box(self):
        """
        Get the email input box element.
        Returns:
            WebElement: The email input box element.
        """
        return self.driver.find_element(*self.email_locator)

    def get_pass_input_box(self):
        """
        Get the password input box element.
        Returns:
            WebElement: The password input box element.
        """
        return self.driver.find_element(*self.password_locator)

    def login_with_email_pass(self) -> bool:
        """
        This method successfully logins with test data
        Returns:
            bool: Return true is successfully login otherwise return false
        """
        try:
            email_input: WebElement = self.get_email_input_box()
            password_input: WebElement = self.get_pass_input_box()
            login_btn: WebElement = self.get_login_btn()
            login_data: list = GlobalData.credential
            email: str = login_data['username']
            password: str = login_data['password']
            email_input.clear()
            email_input.send_keys(email)
            print(f"Successfully entered the username - {email}")
            password_input.clear()
            password_input.send_keys(password)
            print(f"Successfully entere the password - {password}")
            login_btn.click()
            print(f"Successfully clicked the Login Button")
            self.wait_for_presence_of_element(locator=self.welcome_locator, time=15)
            print(f"Successfully entered into the HomePage")
            return True
        except:
            return False
