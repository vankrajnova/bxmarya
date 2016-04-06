from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://bx.marya.ru/")


    def open_lk(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@class='ta-right']//span[.='Константин Григорьев']").click()


    def destroy(self):
        self.wd.quit()



