# -*- coding: utf-8 -*-
import unittest

from selenium.webdriver.firefox.webdriver import WebDriver

from model.reginfo import Reginfo


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class register(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://bx.marya.ru/")


    def open_register_page(self):
        wd = self.wd
        wd.find_element_by_css_selector("span.pseudolink.link-white").click()
        wd.find_element_by_link_text("Зарегистрироваться").click()


    def create_registration_information(self, reginfo):
        wd = self.wd
        self.open_register_page()
        wd.find_element_by_name("REGISTER[NAME]").click()
        wd.find_element_by_name("REGISTER[NAME]").clear()
        wd.find_element_by_name("REGISTER[NAME]").send_keys(reginfo.name)
        wd.find_element_by_name("REGISTER[LAST_NAME]").click()
        wd.find_element_by_name("REGISTER[LAST_NAME]").clear()
        wd.find_element_by_name("REGISTER[LAST_NAME]").send_keys(reginfo.lastname)
        wd.find_element_by_name("REGISTER[LOGIN]").click()
        wd.find_element_by_name("REGISTER[LOGIN]").clear()
        wd.find_element_by_name("REGISTER[LOGIN]").send_keys(reginfo.username)
        wd.find_element_by_name("REGISTER[PASSWORD]").click()
        wd.find_element_by_name("REGISTER[PASSWORD]").clear()
        wd.find_element_by_name("REGISTER[PASSWORD]").send_keys(reginfo.password)
        wd.find_element_by_name("REGISTER[CONFIRM_PASSWORD]").click()
        wd.find_element_by_name("REGISTER[CONFIRM_PASSWORD]").clear()
        wd.find_element_by_name("REGISTER[CONFIRM_PASSWORD]").send_keys(reginfo.confirm_password)
        wd.find_element_by_name("REGISTER[EMAIL]").click()
        wd.find_element_by_name("REGISTER[EMAIL]").clear()
        wd.find_element_by_name("REGISTER[EMAIL]").send_keys(reginfo.email)
        wd.find_element_by_name("REGISTER[PERSONAL_PHONE]").click()
        wd.find_element_by_name("REGISTER[PERSONAL_PHONE]").clear()
        wd.find_element_by_name("REGISTER[PERSONAL_PHONE]").send_keys(reginfo.phone)
        wd.find_element_by_css_selector("div.jq-selectbox__select-text").click()
        wd.find_element_by_xpath("//div[@class='all-wrap']//li[.='Курск']").click()
        wd.find_element_by_xpath(
            "//div[@class='all-wrap']/div[3]/div/div[2]/form[1]/div[9]/div[2]/div/div[1]/div[1]").click()
        wd.find_element_by_xpath(
            "//div[@class='all-wrap']/div[3]/div/div[2]/form[1]/div[9]/div[2]/div/div[2]/ul/li").click()
        self.open_next_step_page()



    def open_next_step_page(self):
        wd = self.wd
        wd.find_element_by_name("next_step").click()


    def test_register(self):
        self.open_home_page()
        self.create_registration_information(Reginfo(name="Тест", lastname="Тестовая", username="testlogin", password="123456", confirm_password="123456", email="test@mail.ru", phone="989 898-98-98"))


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
