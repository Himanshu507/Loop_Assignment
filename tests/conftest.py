import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='class')
def setup(request):
    # Initialize WebDriver for Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://app.tryloop.ai/login/password")
    request.cls.driver = driver
    yield driver
    driver.quit()
