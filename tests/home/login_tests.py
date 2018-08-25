from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("test@gmail.com", "abcabc")

        userIcon = driver.find_element(By.LINK_TEXT, "My Courses")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")
        driver.quit()