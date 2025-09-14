import string
import time
import random

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.Add_Customer_Page import Add_Customer_Page

class Test_03_Add_New_customer:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_new_customer(self,setup):
        self.logger.info("*************** Test_03_Add_New_Customer Started  ************")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("*************** Login Complete *******************************")
        self.logger.info("*************** Starting add new customer*********************")

        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_options()
        self.add_customer.click_addnew()
        self.logger.info("*************** Providing Customer Info started **************")
        email = generate_random_email()
        self.add_customer.enter_email(email)
        self.add_customer.enter_password("Test@123")
        self.add_customer.enter_firstname("Jenny")
        self.add_customer.enter_lastname("Shaw")
        self.add_customer.select_gender("Male")

        self.add_customer.enter_companyname("MyCompany")
        self.add_customer.select_tax_exempt()
        self.logger.info("*************** good till here        ***********************")
        self.add_customer.newsletter("nopCommerce")
        self.logger.info("*************** nopCommerce is Selected ***********************")

        self.add_customer.select_customer_role("Registered")
        self.logger.info("*************** Guests is Selected ***********************")
        self.add_customer.select_manager_of_vendor()
        self.logger.info("*************** Vendor is Selected ***********************")
        self.add_customer.customer_save_password()
        self.logger.info("*************** Password click is Selected ***********************")
        self.add_customer.enter_admin_comments("Test admin comment")
        self.logger.info("*************** Comments are Entered ***********************")
        self.add_customer.click_save()
        self.logger.info("*************** Save Button is Clicked ***************")

        customer_add_success_text = "successfully."
        success_text = self.driver.find_element(By.XPATH,"//div[@class='content-wrapper']/div[1]").text

        self.logger.info(f"************* {customer_add_success_text} ***********")
        self.logger.info(f"************* {success_text} ************************")

        if customer_add_success_text.strip() in success_text.strip():
            assert True
            self.logger.info("*************** Test 03 Add New Customer test passed Successfully ***************")
            self.driver.save_screenshot("./screenshots/test_add_new_customer_pass.png")
            self.driver.close()
        else:
            self.logger.info("*************** Test 03 Add New Customer test failed ***************")
            self.driver.save_screenshot("./screenshots/test_add_new_customer_fail.png")
            self.driver.close()
            assert False


def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits,k=8))
    domain = random.choice(['gmail.com','yahoo.com','outlook.com','hotmail.com'])
    return f'{username}@{domain}'

