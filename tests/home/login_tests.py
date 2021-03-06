import pytest as pytest
from pages.home.login_page import LoginPage
import unittest
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse= True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login verification")

    @pytest.mark.run(order=1)
    def test_Invalid_Login(self):
        self.lp.logout()
        self.lp.login("test@gmail.com", "axxxbcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True
