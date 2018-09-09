from base.seleniumdriver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    _user_settings_icon = "//*[@id='navbar']//span[text()='User Settings']"
    _user_icon = "My Courses"
    _login_not_successful_message = "//div[contains(text(), 'Invalid email or password')]"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType= "link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        return self.isElementPresent(self._user_icon, locatorType= "link")

    def verifyLoginNotSuccessful(self):
        return self.isElementPresent(self._login_not_successful_message, locatorType= "xpath")

    def verifyTitle(self):
        title = self.getTitle()
        if "Google" in title:
            return True
        else:
            return False