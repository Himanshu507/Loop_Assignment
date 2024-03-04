from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from utilities.base_class import BaseClass


class HistoryStorePage(BaseClass):

    def __init__(self, driver):
        """
        Constructor for Store history page class.
        Args:
            driver: WebDriver instance for interacting with the web browser.
        """
        self.driver = driver

    store_name_locator = (By.XPATH, "//h6[.='Store name']")
    selected_dropdown_locator = (By.XPATH, "//div[@id='drilldown-options-fc']/div/div/p")

    def is_loading_completed(self) -> bool:
        """
        This method successfully detects that History view by store is loaded or not.
        Returns:
            bool: Return true if loaded otherwise return false
        """
        try:
            self.wait_for_presence_of_element(locator=self.store_name_locator, time=15)
            print(f"Successfully entered into the History view by Store Page")
            return True
        except NoSuchElementException:
            return False

    def is_reversals_selected(self) -> bool:
        """
        This method checks that reversals is selected or not
        :return:
            bool: Return true if reversals is selected otherwise return False
        """
        self.wait_for_presence_of_element(locator=self.selected_dropdown_locator, time=15)
        selected_dropdown: WebElement = self.driver.find_element(*self.selected_dropdown_locator)
        print(f"Successfully get the selected dropdown value webelement which is {selected_dropdown.text}")
        if 'Reversals' == selected_dropdown.text:
            return True
        else:
            return False

    def get_table_value(self, row, column) -> float:
        """
        This method gets selected cell value
        Args:
            row: Int instance for selecting the row
            column: Int instance for selecting the column
        :return:
            float: Return the value of selected cell
        """
        cell_xpath: str = f"((//table/tbody/tr)[{row}]/td)[{column}]/h6"  # created the dynamic xpath
        cell_locator: WebElement = self.driver.find_element(By.XPATH, cell_xpath)
        return float(cell_locator.text.replace("$", "").replace(",", ""))

    def get_table_month_names(self, column) -> str:
        """
        This method gets selected cell value
        Args:
            column: Int instance for selecting the column
        :return:
            str: Return the value of selected cell
        """
        cell_xpath: str = f"(//table/thead/tr/th)[{column}]/div/div/h6"  # created the dynamic xpath
        cell_locator: WebElement = self.driver.find_element(By.XPATH, cell_xpath)
        return cell_locator.text
