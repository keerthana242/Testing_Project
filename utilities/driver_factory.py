from selenium import webdriver

class DriverFactory:

    def get_driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver