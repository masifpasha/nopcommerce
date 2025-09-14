import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils

class Test_02_Admin_Login_Data_Driven:
    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = './test_data/admin_login_page.xlsx'
    status_list = []

    def test_valid_admin_login_data_driven(self,setup):
        self.logger.info("*************** test_valid_admin_login_data_driven  ************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)

        self.rows = excel_utils.get_row_count(self.path,"Sheet1")
        print("No.of Rows",self.rows)

        for r in range(2,self.rows+1):
            self.username = excel_utils.read_data(self.path,"Sheet1",r,1)
            self.password = excel_utils.read_data(self.path,"Sheet1",r,2)
            self.expected = excel_utils.read_data(self.path,"Sheet1",r,3)
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.expected == "Yes":
                    self.logger.info(" test data is passed")
                    self.status_list.append("PASS")
                    self.admin_lp.click_logout()
                elif self.expected == "No":
                    self.logger.info(" test data is failed")
                    self.status_list.append("FAIL")
                    self.admin_lp.click_logout()
            elif act_title != exp_title:
                if self.expected == 'Yes':
                    self.logger.info(" test data is failed")
                    self.status_list.append("FAIL")
                elif self.expected == 'No':
                    self.logger.info(" test data is passed")
                    self.status_list.append("PASS")

        print("Status List : ",self.status_list)

        if "FAIL" in self.status_list:
            self.logger.info(" test_admin_login_data_driven test is failed")
            assert False
        else:
            self.logger.info(" test_admin_login_data_driven test is passed")
            assert True

        self.driver.close()
