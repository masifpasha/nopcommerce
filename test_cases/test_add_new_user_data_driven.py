import string
import time
import random

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils
from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.Add_Customer_Page import Add_Customer_Page

class Test_03_Add_New_User_Data_Driven:
    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = './test_data/admin_login_page.xlsx'
    status_list = []

    def test_add_new_customer(self,setup):
        self.logger.info("*************** Test_03_Add_New_Customer Started  ************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)

        self.username = excel_utils.read_data(self.path,"Sheet1",2,1)
        self.password = excel_utils.read_data(self.path,"Sheet1",2,2)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(5)
        self.driver.maximize_window()
        self.logger.info("*************** window maximized  ************")

        self.add_customer_lp = Add_Customer_Page(self.driver)
        self.rows = excel_utils.get_row_count(self.path,"Sheet2")
        print("No.of Rows",self.rows)

        self.logger.info("*************** click customer ************")
        self.add_customer_lp.click_customers()
        self.logger.info("*************** click customer add ************")
        self.add_customer_lp.click_customers_from_menu_options()
        self.logger.info("*************** click add new ************")
        self.add_customer_lp.click_addnew()

        for r in range(2,self.rows+1):
            self.logger.info("*************** r value %s  ************",r)
            self.password = excel_utils.read_data(self.path,"Sheet2",r,2)
            self.firstname = excel_utils.read_data(self.path,"Sheet2",r,3)
            self.lastname = excel_utils.read_data(self.path,"Sheet2",r,4)
            self.gender = excel_utils.read_data(self.path,"Sheet2",r,5)
            self.company = excel_utils.read_data(self.path,"Sheet2",r,6)
            self.istaxexempt = excel_utils.read_data(self.path,"Sheet2",r,7)
            self.newsletter = excel_utils.read_data(self.path,"Sheet2",r,8)
            self.cusrole = excel_utils.read_data(self.path,"Sheet2",r,9)
            self.manager = excel_utils.read_data(self.path,"Sheet2",r,10)
            self.active = excel_utils.read_data(self.path,"Sheet2",r,11)
            self.cuspassword = excel_utils.read_data(self.path,"Sheet2",r,12)
            self.admincomment = excel_utils.read_data(self.path,"Sheet2",r,13)

            email = generate_random_email()
            self.add_customer_lp.enter_email(email)
            self.logger.info("*************** email. done  ************")
            self.add_customer_lp.enter_password(self.password)
            self.logger.info("*************** password done ************")
            self.add_customer_lp.enter_firstname(self.firstname)
            self.logger.info("*************** firstname done ************")
            self.add_customer_lp.enter_lastname(self.lastname)
            self.logger.info("*************** lastname done ************")
            self.add_customer_lp.select_gender(self.gender)
            self.add_customer_lp.enter_companyname(self.company)
            self.add_customer_lp.select_tax_exempt()
            self.add_customer_lp.newsletter(self.newsletter)
            self.add_customer_lp.select_customer_role(self.cusrole)
            self.add_customer_lp.select_manager_of_vendor()
            self.add_customer_lp.customer_save_password()
            self.add_customer_lp.enter_admin_comments(self.admincomment)
            self.add_customer_lp.click_save()

            print("Status List : ",self.status_list)
            self.logger.info("*************** %s  ************",self.status_list)

            if "FAIL" in self.status_list:
                self.logger.info(" test_add_new_user_data_driven test is failed")
                assert False
            else:
                self.logger.info(" test_add_new_user_data_driven test is passed")
                self.add_customer_lp.click_addnew()
                assert True

        self.driver.close()

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits,k=8))
    domain = random.choice(['gmail.com','yahoo.com','outlook.com','hotmail.com'])
    return f'{username}@{domain}'
