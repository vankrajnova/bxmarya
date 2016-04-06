from selenium.webdriver.firefox.webdriver import WebDriver


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://bx.marya.ru/")

    def login_page(self, username, password):
        wd = self.wd
        self.open_home_page()
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

    def open_lk(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@class='ta-right']//span[.='Константин Григорьев']").click()

    def logout(self):
        wd = self.wd
        self.open_lk()
        wd.find_element_by_xpath("//div[@class='profile_menu']//a[.='Выйти']").click()


    def destroy(self):
        self.wd.quit()



