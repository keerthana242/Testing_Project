import time
from utilities.driver_factory import DriverFactory
from pages.login_page import LoginPage


class TestLogin:

    def setup_method(self):
        factory = DriverFactory()
        self.driver = factory.get_driver()
        self.driver.get("https://tichi-app-webapp-stage.web.app/login")
        self.login = LoginPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    # Test Case 1 - Empty Email
    def test_empty_email(self):
        self.login.enter_email("")
        self.login.click_continue()

        expected = "Email is required"
        actual = self.login.get_error_message()

        assert actual == expected

    # Test Case 2 - Invalid Email mising @
    def test_invalid_email(self):

     self.login.enter_email("abc")
     self.login.click_continue()

     expected = "Please include an '@' in the email address. 'abc' is missing an '@'."

     actual = self.login.get_email_validation_message()

     assert actual == expected


    #Invalid Email missing Domain Nmae
    def test_invalid_email_without_domain(self):

     self.login.enter_email("abc@")
     self.login.click_continue()

     expected = "Please enter a part following '@'. 'abc@' is incomplete."
     actual = self.login.get_email_validation_message()

     assert actual == expected

     #Invalid Email Missin Username
    def test_invalid_email_without_username(self):

     self.login.enter_email("@gmail.com")
     self.login.click_continue()

     expected = "Please enter a part followed by '@'. '@gmail.com' is incomplete."
     actual = self.login.get_email_validation_message()

     assert actual == expected


    # Test Case 3 - Valid Login
    def test_valid_login(self):
        self.login.enter_email("23csa55@karpagamtech.ac.in")
        self.login.click_continue()

        time.sleep(2)

        self.login.enter_password("Keerthana@2005")
        self.login.click_login()

        time.sleep(3)

    #Empty password
    def test_empty_password(self):

     self.login.enter_email("23csa55@karpagamtech.ac.in")
     self.login.click_continue()
     time.sleep(2)
     self.login.click_login()
     expected = "Password is required"
     actual = self.login.get_password_error_message().strip()
     assert actual == expected

     #Invalid Password
    def test_incorrect_password(self):

    # Enter registered email
     self.login.enter_email("23csa55@karpagamtech.ac.in")
     self.login.click_continue()
     time.sleep(2)
     self.login.enter_password("Keerthi@2005")
     self.login.click_login()
    # Verify error message
     expected = "Invalid login details"
     actual = self.login.get_login_error_message().strip()
     assert actual == expected

    #Valid Password
    def test_valid_login(self):
     self.login.enter_email("23csa55@karpagamtech.ac.in")
     self.login.click_continue()
     time.sleep(2)
     self.login.enter_password("Keerthana@2005")
     self.login.click_login()
     time.sleep(3)
    # Verify navigation to dashboard
     expected = "https://tichi-app-webapp-stage.web.app/home"
     actual = self.login.get_current_url()
     assert actual == expected

    #Verify page title
    def test_page_title(self):
     expected = "Tichi"  
     actual = self.login.get_page_title()
     assert actual == expected

    #Verity the url
    def test_login_page_url(self):

     expected = "https://tichi-app-webapp-stage.web.app/login"

     actual = self.login.get_current_url()

     assert actual == expected 
