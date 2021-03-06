# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class register1(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_register1(self):
        success = True
        wd = self.wd
        wd.get("http://bx.marya.ru/")
        wd.find_element_by_css_selector("span.pseudolink.link-white").click()
        wd.find_element_by_link_text("Зарегистрироваться").click()
        wd.find_element_by_name("REGISTER[NAME]").click()
        wd.find_element_by_name("REGISTER[NAME]").clear()
        wd.find_element_by_name("REGISTER[NAME]").send_keys("Тест")
        wd.find_element_by_name("REGISTER[LAST_NAME]").click()
        wd.find_element_by_name("REGISTER[LAST_NAME]").clear()
        wd.find_element_by_name("REGISTER[LAST_NAME]").send_keys("Тестовая")
        wd.find_element_by_name("REGISTER[LOGIN]").click()
        wd.find_element_by_name("REGISTER[LOGIN]").clear()
        wd.find_element_by_name("REGISTER[LOGIN]").send_keys("testlogin")
        wd.find_element_by_name("REGISTER[PASSWORD]").click()
        wd.find_element_by_name("REGISTER[PASSWORD]").clear()
        wd.find_element_by_name("REGISTER[PASSWORD]").send_keys("123456")
        wd.find_element_by_name("REGISTER[CONFIRM_PASSWORD]").click()
        wd.find_element_by_name("REGISTER[CONFIRM_PASSWORD]").clear()
        wd.find_element_by_name("REGISTER[CONFIRM_PASSWORD]").send_keys("123456")
        wd.find_element_by_name("REGISTER[EMAIL]").click()
        wd.find_element_by_name("REGISTER[EMAIL]").clear()
        wd.find_element_by_name("REGISTER[EMAIL]").send_keys("testmarya@yandex.ru")
        if not wd.find_element_by_xpath("//select[@class='select-phone-code']//option[1]").is_selected():
            wd.find_element_by_xpath("//select[@class='select-phone-code']//option[1]").click()
        wd.find_element_by_name("REGISTER[PERSONAL_PHONE]").click()
        wd.find_element_by_name("REGISTER[PERSONAL_PHONE]").clear()
        wd.find_element_by_name("REGISTER[PERSONAL_PHONE]").send_keys("937 260-97-57")
        wd.find_element_by_css_selector("div.jq-selectbox__trigger").click()
        wd.find_element_by_xpath("//div[@class='all-wrap']//li[.='Краснодар']").click()
        wd.find_element_by_xpath("//div[@class='all-wrap']/div[3]/div/div[2]/form[1]/div[9]/div[2]/div/div[1]/div[2]/div").click()
        wd.find_element_by_xpath("//div[@class='all-wrap']/div[3]/div/div[2]/form[1]/div[9]/div[2]/div/div[2]/ul/li[2]").click()
        wd.find_element_by_name("next_step").click()
        self.assertTrue((len(wd.find_elements_by_xpath("//div[2]/div/p/b")) != 0))
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
