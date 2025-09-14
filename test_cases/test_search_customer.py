import time

import pytest
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.Add_Customer_Page import Add_Customer_Page
from base_pages.Search_Customer_Page import Search_Customer_Page

class Test_04_Search_Customer:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_customer_by_email(self,setup):
        self.logger.info("************ Test 04 Search Customer by email Started ****************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("********** login completed ***********")
        self.logger.info("***** navigating to customer search page **********")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_options()
        self.logger.info("********** starting search customer by email ************")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.enter_customer_email("arthur_holmes@nopCommerce.com")
        self.search_customer.click_search_button()
        time.sleep(3)

        Is_email_present = self.search_customer.search_customer_by_email("arthur_holmes@nopCommerce.com")
        if Is_email_present == True:
            assert True
            self.logger.info("**********test 04 search by email test passed *********")
            self.driver.close()
        else:
            self.logger.info("********** test 04 search by email test failed ********* ")
            self.driver.save_screenshot("./screenshots/test_04_search_by_email_fail.png")
            self.driver.close()

    @pytest.mark.regression
    def test_search_customer_by_name(self,setup):
        self.logger.info("************ Test 04 Search Customer by name ************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("********** login completed ***********")
        self.logger.info("***** navigating to customer search page **********")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_options()
        self.logger.info("********** starting search customer by name ************")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.enter_customer_firstname("Arthur")
        self.search_customer.enter_customer_lastname("Holmes")
        self.search_customer.click_search_button()
        time.sleep(3)

        Is_name_present = self.search_customer.search_customer_by_name("Arthur Holmes")
        if Is_name_present == True:
            assert True
            self.logger.info(" ************ test 04 02 search customer by name is pass *********")
            self.driver.close()
        else:
            self.logger.info("*** test 04 02 search customer by name is failed **********")
            self.driver.save_screenshot("./screenshots/test_04_02search_customer_fail.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_customer_by_companyname(self,setup):
        self.logger.info("************ Test 04 Search Customer by Companyname ************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("********** login completed ***********")
        self.logger.info("***** navigating to customer search page **********")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_options()
        self.logger.info("********** starting search customer by Company name ************")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.enter_customer_companyname("nopCommerce")
        self.search_customer.click_search_button()
        time.sleep(3)

        Is_cmpname_present = self.search_customer.search_customer_by_company("nopCommerce")
        if Is_cmpname_present == True:
            assert True
            self.logger.info(" ************ test 04 03 search customer by Company name is pass *********")
            self.driver.close()
        else:
            self.logger.info("*** test 04 02 search customer by Compnay name is failed **********")
            self.driver.save_screenshot("./screenshots/test_04_customer_Company_fail.png")
            self.driver.close()
            assert False
