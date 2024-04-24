import pytest
from testcases.conftest import *
from pages.webapppages.saucedemologinpage import SauceDemoLoginPage
from pages.webapppages.saucedemocheckoutpage import SauceDemoCheckOutPage
from pages.webapppages.sidebarvalidation import SideBarValidation
import time


@pytest.mark.usefixtures("browser_setup","log_on_failure")
class Test_SauceDemo :

    @pytest.mark.run(order=1)
    def test_login_functionality(self,ui_json_data,browser_setup) :
        driver = browser_setup;
        loginPage = SauceDemoLoginPage(driver);
        loginPage.login_functionality(ui_json_data['username'],ui_json_data['password']);
        assert loginPage.getText_appLogo().__eq__(ui_json_data['titlelogo']);
        loginPage.logout_functionality();
    
    @pytest.mark.run(order=2)
    def test_checkout_functionality(self,ui_json_data,browser_setup) :
        driver = browser_setup;
        loginPage = SauceDemoLoginPage(driver);
        loginPage.login_functionality(ui_json_data['username'],ui_json_data['password']);
        assert loginPage.getText_appLogo().__eq__(ui_json_data['titlelogo']);
        checkoutPage = SauceDemoCheckOutPage(driver);
        checkoutPage.checkOut_functionality(ui_json_data['firstname'],ui_json_data['lastname'],ui_json_data['pincode']);
        loginPage.logout_functionality();
    
    @pytest.mark.run(order=3)
    def test_sidebar_validation(self,ui_json_data,browser_setup) :
        driver = browser_setup;
        loginPage = SauceDemoLoginPage(driver);
        loginPage.login_functionality(ui_json_data['username'],ui_json_data['password']);
        assert loginPage.getText_appLogo().__eq__(ui_json_data['titlelogo']);
        sideBar = SideBarValidation(driver);
        sideBar.clickOn_sidebarBtn();
        time.sleep(3);
        for element in ui_json_data['sidebarElements'] :
            assert True == sideBar.sideBar_validation(element);
        sideBar.clickOn_closeBtn();
        loginPage.logout_functionality();
    
    @pytest.mark.run(order=4)
    def test_login_with_lockedAccount(self,ui_json_data,browser_setup) :
        driver = browser_setup;
        loginPage = SauceDemoLoginPage(driver);
        loginPage.login_with_lockedaccount(ui_json_data['lockeduser'],ui_json_data['password']);
        assert loginPage.getText_errormsg().__eq__(ui_json_data['errormsg']);
        loginPage.clear_inputValues();
    
    