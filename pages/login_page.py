from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Step 1 Locators
    email_textbox = (By.ID, "email")
    continue_button = (By.XPATH, "//button[text()='Continue']")

    # Step 2 Locators
    password_textbox = (By.ID, "password")
    login_button = (By.XPATH, "//button[text()='Login']")

    # Step 3 Locator
    error_message = (By.XPATH, "/html/body/div[1]/div[2]/div/form/div/p")
    password_error_message = (By.XPATH, "//p[text()='Password is required']")
    login_error_message = (By.XPATH, "/html/body/div[1]/div[2]/div/div[2]")

    # Step 1 Methods
    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    # Step 2 Methods
    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
     self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
      return self.driver.find_element(*self.error_message).text
    
    # HTML5 Browser Validation Message
    def get_email_validation_message(self):
     return self.driver.find_element(*self.email_textbox).get_attribute("validationMessage")
    
    # Empty password
    def get_password_error_message(self):
     return self.driver.find_element(*self.password_error_message).text
    
    #Invalid Password
    def get_login_error_message(self):
     return self.driver.find_element(*self.login_error_message).text
    
    def get_current_url(self):
     return self.driver.current_url
    
    def get_page_title(self):
     return self.driver.title