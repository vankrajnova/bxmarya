# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class login(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)


    def open_home_page(self, wd):
        wd.get("http://bx.marya.ru/")

    def login_page(self, wd, username, password):
        # find link
        wd.find_element_by_css_selector("span.pseudolink.link-white").click()
        # login
        wd.find_element_by_id("user_login").click()
        wd.find_element_by_id("user_login").clear()
        wd.find_element_by_id("user_login").send_keys(username)
        wd.find_element_by_name("USER_PASSWORD").click()
        wd.find_element_by_name("USER_PASSWORD").clear()
        wd.find_element_by_name("USER_PASSWORD").send_keys(password)
        wd.find_element_by_name("Login").click()

    def open_lk(self, wd):
        wd.find_element_by_xpath("//div[@class='ta-right']//span[.='Константин Григорьев']").click()

    def logout(self, wd):
        wd.find_element_by_xpath("//div[@class='profile_menu']//a[.='Выйти']").click()


    def test_login(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login_page(wd, username="bxuser", password="bxuser")
        self.open_lk(wd)
        self.logout(wd)

    def test_login_empty_password(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login_page(wd, username="bxuser", password="")
        wd.find_element_by_css_selector("div.mfp-close.cn-modal-close").click()



    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
