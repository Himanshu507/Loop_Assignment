from data.global_data import GlobalData
from pageObjects.login_page import LoginPage
from pageObjects.transaction_page import TransactionPage
from utilities.base_class import BaseClass


class TestScenario002(BaseClass):

    month_sum_values: list = []
    grand_total_month: list = []
    month_names: list = []

    def test_TC_001(self):
        loginpage: LoginPage = LoginPage(self.driver)
        print("Successfully get the login page class object")
        assert loginpage.login_with_email_pass(), "Failed to login"
        print("Successfully LoggedIn")
        self.open_url(GlobalData.pages_urls['transaction_page'])
        print("Successfully Opened the Transaction page")
        transaction_page: TransactionPage = TransactionPage(self.driver)
        print("Successfully get the transaction page class object")
        transaction_page.select_locations()
        print("Successfully selects the desired locations")
        transaction_page.select_marketplace()
        print("Successfully selects the desired marketplace")