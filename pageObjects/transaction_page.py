from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from data.global_data import GlobalData
from utilities.base_class import BaseClass


class TransactionPage(BaseClass):

    def __init__(self, driver):
        """
        Constructor for transaction page class.
        Args:
            driver: WebDriver instance for interacting with the web browser.
        """
        self.driver = driver

    location_locator = (By.XPATH, "(//button[@data-testid='selectBtn'])[1]")
    marketplace_locator = (By.XPATH, "(//button[@data-testid='selectBtn'])[3]")
    unselect_locator = (By.XPATH, "//p[contains(text(), 'Unselect All')]")
    apply_locator = (By.XPATH, "//button[@data-testid='applyBtn']")

    def is_loading_completed(self) -> bool:
        """
        This method successfully detects that Transaction page is loaded or not.
        Returns:
            bool: Return true if loaded otherwise return false
        """
        try:
            self.wait_for_presence_of_element(locator=self.location_locator, time=15)
            print(f"Successfully entered into the Transaction Page")
            return True
        except NoSuchElementException:
            return False

    def get_location_locator(self) -> WebElement:
        """
        This method returns the location locator
        :return:
            WebElement: Return the WebElement
        """
        return self.driver.find_element(*self.location_locator)

    def get_apply_locator(self) -> WebElement:
        """
        This method returns the apply button locator
        :return:
            WebElement: Return the WebElement
        """
        return self.driver.find_element(*self.apply_locator)

    def get_market_place_locator(self) -> WebElement:
        """
        This method returns the Market place locator
        :return:
            WebElement: Return the WebElement
        """
        return self.driver.find_element(*self.marketplace_locator)

    def get_unselect_locator(self) -> WebElement:
        """
        This method returns the unselect locator
        :return:
            WebElement: Return the WebElement
        """
        return self.driver.find_element(*self.unselect_locator)

    def select_locations(self):
        """
        This method gets selects the location eg. Artisan Alchemy, Blissful Buffet
        :return:
            None
        """
        self.get_location_locator().click()
        print("Successfully clicks on the location dropdown menu")
        self.get_unselect_locator().click()
        print("Successfully clicks on the unselect all dropdown menu")
        locations: list = GlobalData.locations
        for location in locations:
            loc_xpath: str = f"//p[.='{location}']"
            cell_locator: WebElement = self.driver.find_element(By.XPATH, loc_xpath)
            cell_locator.click()
        self.get_apply_locator().click()
        print("Successfully Selected the locations")

    def select_marketplace(self):
        """
        This method gets selects the marketplace eg. Grubhub
        :return:
            None
        """
        self.get_market_place_locator().click()
        print("Successfully clicks on the marketplace dropdown menu")
        self.get_unselect_locator().click()
        print("Successfully clicks on the unselect all dropdown menu")
        markets: list = GlobalData.marketplace
        for market in markets:
            loc_xpath: str = f"//p[.='{market}']"
            cell_locator: WebElement = self.driver.find_element(By.XPATH, loc_xpath)
            cell_locator.click()
        self.get_apply_locator().click()
        print("Successfully Selected the Marketplace")

