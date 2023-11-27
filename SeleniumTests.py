import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


class LoginTest(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        return driver
        

    def test_valid_login(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://automationintesting.online/#/admin")

        # Find elements
        driver.find_element(By.ID, 'username').send_keys('admin')
        driver.find_element(By.ID, 'password').send_keys('password')
        driver.find_element(By.ID, 'doLogin').click()

        # Assertations
        driver.implicitly_wait(10)
        frontPageLink = driver.find_element(By.ID, 'frontPageLink').text
        self.assertEqual(frontPageLink, 'Front Page')

    def test_empty_fields(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://automationintesting.online/#/admin") 

        # Find Elements
        driver.find_element(By.ID, 'doLogin').click()

        # Assertations
        cssValue = driver.find_element(By.ID, "username").value_of_css_property("border")
        self.assertTrue("rgb(128, 128, 128)" in cssValue) # rgb(128, 128, 128) is the value of red (Borders turn red when empty)

    def test_invalid_logins(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://automationintesting.online/#/admin") 

        # Find Elements
        driver.find_element(By.ID, 'username').send_keys('asf')
        driver.find_element(By.ID, 'password').send_keys('sword')
        driver.find_element(By.ID, 'doLogin').click()

        # Assertations
        cssValue = driver.find_element(By.ID, "username").value_of_css_property("border")
        self.assertTrue("rgb(128, 128, 128)" in cssValue) # rgb(128, 128, 128) is the value of red (Borders turn red when empty)

    def test_room_creation(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://automationintesting.online/#/admin")

        # Find elements
        driver.find_element(By.ID, 'username').send_keys('admin')
        driver.find_element(By.ID, 'password').send_keys('password')
        driver.find_element(By.ID, 'doLogin').click()

        driver.implicitly_wait(10)
        # Room 1
        driver.find_element(By.ID,"roomName").send_keys("102")
        driver.find_element(By.ID,"roomPrice").send_keys("100")
        driver.find_element(By.ID,"wifiCheckbox").click()
        driver.find_element(By.ID,"createRoom").click()
        
        # Room 2
        driver.find_element(By.ID,"roomName").send_keys("103")
        driver.find_element(By.ID,"roomPrice").send_keys("200")

        driver.find_element(By.ID,"createRoom").click()

        driver.implicitly_wait(2)
        # Assertions
        deleteButtonsAmount = driver.find_element(By.CLASS_NAME, "roomDelete")
        self.assertIsNotNone(deleteButtonsAmount)


if __name__ == "__main__":
    unittest.main()
