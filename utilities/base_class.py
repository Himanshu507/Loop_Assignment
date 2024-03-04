import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class BaseClass:

    def wait_for_element_visibility(self, locator, time=5):
        """
        Wait for the element identified by the given locator to become visible on the web page.

        Args:
            locator: A tuple specifying the locator strategy (e.g., By.ID, By.XPATH) and the locator value.
            time: Optional. The maximum time (in seconds) to wait for the element visibility. Default is 5 seconds.
        """
        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_element_invisibility(self, locator, time=5):
        """
        Wait for the element identified by the given locator to become invisible on the web page.

        Args:
            locator: A tuple specifying the locator strategy (e.g., By.ID, By.XPATH) and the locator value.
            time: The maximum time (in seconds) to wait for the element to become invisible. Default is 5 secs.
        """
        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.invisibility_of_element_located(locator))

    def wait_for_presence_of_element(self, locator, time=5):
        """
        Wait for the element identified by the given locator to be present in the DOM of the web page.

        Args:
            locator: A tuple specifying the locator strategy (e.g., By.ID, By.XPATH) and the locator value.
            time: Optional. The maximum time (in seconds) to wait for the element presence. Default is 5 seconds.
        """
        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.presence_of_element_located(locator))

    def get_current_url(self):
        """
        Get the current URL of the web page.

        Returns:
            str: The current URL of the web page.
        """
        return self.driver.current_url

    def open_url(self, url):
        """
        Open the specified URL in the web browser.

        Args:
            url: The URL to open in the web browser.
        """
        return self.driver.get(url)
