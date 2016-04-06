

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("span.pseudolink.link-white").click()
        wd.find_element_by_id("user_login").click()
        wd.find_element_by_id("user_login").clear()
        wd.find_element_by_id("user_login").send_keys(username)
        wd.find_element_by_name("USER_PASSWORD").click()
        wd.find_element_by_name("USER_PASSWORD").clear()
        wd.find_element_by_name("USER_PASSWORD").send_keys(password)
        wd.find_element_by_name("Login").click()

    def logout(self):
        wd = self.app.wd
        self.app.open_lk()
        wd.find_element_by_xpath("//div[@class='profile_menu']//a[.='Выйти']").click()
