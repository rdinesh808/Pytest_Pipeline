import random
import time
from faker import Faker
import pytest
from selenium.webdriver.common.by import By
from com_object_repository import objectrepo as obr

fack = Faker()

def wait(n):
    """Pause execution for n seconds."""
    try:
        time.sleep(n)
    except Exception as e:
        print("Interruption Error:", e)

@pytest.mark.usefixtures("setup")
class TestCommon:
    driver = None
    @pytest.mark.parametrize("page", ["selenium_automation_practice.php"])
    def test_login(self, page):
        """Test opening a page."""
        try:
            self.driver.get(f"https://www.tutorialspoint.com/selenium/practice/{page}")
            wait(2)
        except Exception as e:
            print("Login Error:", e)

    def test_enter_first_name(self):
        try:
            name = self.driver.find_element(By.ID, obr.firstname)
            name.send_keys(fack.name_male())
            wait(1)
            first_name = name.get_attribute("value")
            print("Name is : ", first_name)
            wait(1)
        except Exception as e:
            print("Error entering first name:", e)

    def test_enter_email(self):
        try:
            email = self.driver.find_element(By.ID, obr.email)
            email.send_keys(fack.email())
            wait(1)
            mail = email.get_attribute("value")
            print("Mail is : ", mail)
            wait(1)
        except Exception as e:
            print("Error entering mail :", e)

    def test_select_gender(self):
        try:
            gender = self.driver.find_elements(By.XPATH, obr.gender)
            n = random.randint(0, len(gender) - 1)
            gender[n].click()
            wait(2)
            sex = gender[n].find_element(By.XPATH, "../label").text
            print("Gender is:", sex)
            wait(2)
        except Exception as e:
            print("Error entering Gender:", e)

    def test_enter_mobile(self):
        try:
            mobile = self.driver.find_element(By.NAME, obr.mobile)
            mobile.send_keys(fack.phone_number())
            wait(1)
            phone = mobile.get_attribute("value")
            print("Mobile is : ", phone)
            wait(1)
        except Exception as e:
            print("Error entering Mobile :", e)
