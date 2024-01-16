from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
import time

from faker import Faker

fake_data_generator = Faker()

def generate_fake_data():
    return {
        "first_name": fake_data_generator.first_name(),
        "last_name": fake_data_generator.last_name(),
        "email": fake_data_generator.email(),
        "password": fake_data_generator.password()
    }

# Sleep for 2 seconds
time.sleep(2)

class Test_001_AccountReg:
    baseURL = "https://demo.opencart.com/"

    def test_account_reg(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        print("started ")
        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        time.sleep(3)
        self.hp.clickRegister()
        time.sleep(3)
        print("filling registration Page form")

        self.regpage = AccountRegistrationPage(self.driver)
        fake_data = generate_fake_data()
        self.regpage.setFirstName(fake_data["first_name"])
        self.regpage.setLastName(fake_data["last_name"])
        self.regpage.setEmail(fake_data["email"])
        self.regpage.setPassword(fake_data["password"])
        time.sleep(2)

        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        print("registration succesfull")


        if self.driver.title == "Register Account":
            assert True
        else:
            assert False

