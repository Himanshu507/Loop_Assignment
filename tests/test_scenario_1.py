from data.global_data import GlobalData
from pageObjects.login_page import LoginPage
from pageObjects.store_history_page import HistoryStorePage
from utilities.base_class import BaseClass


class TestScenario001(BaseClass):

    month_sum_values: list = []
    grand_total_month: list = []
    month_names: list = []

    def test_TC_001(self):
        loginpage: LoginPage = LoginPage(self.driver)
        print("Successfully get the login page class object")
        assert loginpage.login_with_email_pass(), "Failed to login"
        print("Successfully LoggedIn")
        self.open_url(GlobalData.pages_urls['history_page'])
        print("Successfully Opened the History By Store page")
        history_store_page: HistoryStorePage = HistoryStorePage(self.driver)
        assert history_store_page.is_loading_completed(), "Failed to load history view by store page"
        print("Successfully loads the history view by store page.")
        assert history_store_page.is_reversals_selected(), "Reversal is not selected"
        print("Successfully validate that reversal is selected.")
        for column in range(2, 9):
            sum_month: float = 0.0
            TestScenario001.month_names.append(history_store_page.get_table_month_names(column=column))
            for row in range(1, 11):
                sum_month += history_store_page.get_table_value(row=row, column=column)
            month_grand_total = history_store_page.get_table_value(row=12, column=column)
            TestScenario001.month_sum_values.append(round(sum_month, 2))
            TestScenario001.grand_total_month.append(month_grand_total)
        print("Successfully get sum of the values of corresponding months & grand total of months")

    def test_TC_002(self):
        month_name: str = TestScenario001.month_names[0]
        print(f"Checks the value of {month_name} month")
        month_sum: float = TestScenario001.month_sum_values[0]
        print(f"The value of {month_name} Month sum is {month_sum}")
        month_grand_total: float = TestScenario001.grand_total_month[0]
        print(f"The value of grand total of {month_name} month is {month_grand_total} month")
        assert month_sum == month_grand_total, "Month Sum is not equal to Month Grand total"
        print(f"Month sum {month_sum} is equal to month grand total {month_grand_total}")


    def test_TC_003(self):
        month_name: str = TestScenario001.month_names[1]
        print(f"Checks the value of {month_name} month")
        month_sum: float = TestScenario001.month_sum_values[1]
        print(f"The value of {month_name} Month sum is {month_sum}")
        month_grand_total: float = TestScenario001.grand_total_month[1]
        print(f"The value of grand total of {month_name} month is {month_grand_total} month")
        assert month_sum == month_grand_total, "Month Sum is not equal to Month Grand total"
        print(f"Month sum {month_sum} is equal to month grand total {month_grand_total}")


    def test_TC_004(self):
        month_name: str = TestScenario001.month_names[2]
        print(f"Checks the value of {month_name} month")
        month_sum: float = TestScenario001.month_sum_values[2]
        print(f"The value of {month_name} Month sum is {month_sum}")
        month_grand_total: float = TestScenario001.grand_total_month[2]
        print(f"The value of grand total of {month_name} month is {month_grand_total} month")
        assert month_sum == month_grand_total, "Month Sum is not equal to Month Grand total"
        print(f"Month sum {month_sum} is equal to month grand total {month_grand_total}")


    def test_TC_005(self):
        month_name: str = TestScenario001.month_names[3]
        print(f"Checks the value of {month_name} month")
        month_sum: float = TestScenario001.month_sum_values[3]
        print(f"The value of {month_name} Month sum is {month_sum}")
        month_grand_total: float = TestScenario001.grand_total_month[3]
        print(f"The value of grand total of {month_name} month is {month_grand_total} month")
        assert month_sum == month_grand_total, "Month Sum is not equal to Month Grand total"
        print(f"Month sum {month_sum} is equal to month grand total {month_grand_total}")


    def test_TC_006(self):
        month_name: str = TestScenario001.month_names[4]
        print(f"Checks the value of {month_name} month")
        month_sum: float = TestScenario001.month_sum_values[4]
        print(f"The value of {month_name} Month sum is {month_sum}")
        month_grand_total: float = TestScenario001.grand_total_month[4]
        print(f"The value of grand total of {month_name} month is {month_grand_total} month")
        assert month_sum == month_grand_total, "Month Sum is not equal to Month Grand total"
        print(f"Month sum {month_sum} is equal to month grand total {month_grand_total}")


    def test_TC_007(self):
        month_name: str = TestScenario001.month_names[5]
        print(f"Checks the value of {month_name} month")
        month_sum: float = TestScenario001.month_sum_values[5]
        print(f"The value of {month_name} Month sum is {month_sum}")
        month_grand_total: float = TestScenario001.grand_total_month[5]
        print(f"The value of grand total of {month_name} month is {month_grand_total} month")
        assert month_sum == month_grand_total, "Month Sum is not equal to Month Grand total"
        print(f"Month sum {month_sum} is equal to month grand total {month_grand_total}")


    def test_TC_008(self):
        month_name: str = TestScenario001.month_names[6]
        print(f"Checks the value of {month_name} month")
        month_sum: float = TestScenario001.month_sum_values[6]
        print(f"The value of {month_name} Month sum is {month_sum}")
        month_grand_total: float = TestScenario001.grand_total_month[6]
        print(f"The value of grand total of {month_name} month is {month_grand_total} month")
        assert month_sum == month_grand_total, "Month Sum is not equal to Month Grand total"
        print(f"Month sum {month_sum} is equal to month grand total {month_grand_total}")
