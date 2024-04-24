from  testcases.conftest import appium_driver_setup,mobile_json_data
import pytest
from pages.mobileapppages.loginpage import LoginPage
from pages.mobileapppages.moreoptionsvalidation import More_Options_Validation
from pages.mobileapppages.searchpage import SearchPage
from pages.mobileapppages.addrecipiepage import Add_Recipie_Page
from pages.mobileapppages.clickallelements import Click_All_Navigation_Elements
import time

class TestBigOvenMobileApp : 

    @pytest.mark.run(order=11)
    def test_login_functionality(self,appium_driver_setup,mobile_json_data) :
        driver = appium_driver_setup
        driver.implicitly_wait(5);
        login_page = LoginPage(driver);
        login_page.login_functionality(mobile_json_data['username'] , mobile_json_data['password']);
        login_page.logout_functionality();

    @pytest.mark.run(order=12)
    def test_moreoptions_validation(self,appium_driver_setup,mobile_json_data) :
        driver = appium_driver_setup
        driver.implicitly_wait(5);
        login_page = LoginPage(driver);
        login_page.login_functionality(mobile_json_data['username'] , mobile_json_data['password']);
        more_options = More_Options_Validation(driver);
        more_options.click_on_moreoptions();
        for element in mobile_json_data['moreoptions'] :
            time.sleep(3);
            assert more_options.moreoptions_validation(element) == True , f"{element} is not displayed";
        more_options.click_on_app_update();
        login_page.logout_functionality();

    @pytest.mark.run(order=13)
    def test_search_functionality(self,appium_driver_setup,mobile_json_data) :
        driver = appium_driver_setup
        driver.implicitly_wait(5);
        login_page = LoginPage(driver);
        login_page.login_functionality(mobile_json_data['username'] , mobile_json_data['password']);
        search_page = SearchPage(driver);
        search_page.search_functionality(mobile_json_data['searchdata']);
        login_page.logout_functionality();

    @pytest.mark.run(order=14)
    def test_add_recipie_functionality(self,appium_driver_setup,mobile_json_data) :
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_functionality(mobile_json_data['username'] , mobile_json_data['password']);
        addRecipePage = Add_Recipie_Page(driver);
        addRecipePage.add_recipie_functionality(mobile_json_data['title'],mobile_json_data['ingredients'],mobile_json_data['instructions']);
        loginPage.logout_functionality();

    @pytest.mark.run(order=15)
    def test_click_navbar_elements(self,appium_driver_setup,mobile_json_data) :
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_functionality(mobile_json_data['username'] , mobile_json_data['password']);
        click_all_elements = Click_All_Navigation_Elements(driver);
        click_all_elements.click_all_elements();
        loginPage.logout_functionality();

        
