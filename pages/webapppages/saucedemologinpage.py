from actions.saucedemo_actions import SauceDemo_Actions
from selenium.webdriver.common.by import By

class SauceDemoLoginPage(SauceDemo_Actions) :

    username_input = (By.ID,"user-name");
    password_input = (By.ID,"password");
    login_button = (By.ID,"login-button");
    sidebar_button = (By.ID,"react-burger-menu-btn");
    logout_button = (By.ID,"logout_sidebar_link");
    app_logo = (By.XPATH,"//div[@class='app_logo']");
    error_msg = (By.XPATH, "//button[@class='error-button']/parent::h3");

    def __init__(self,driver):
        super().__init__(driver);

    def login_functionality(self,username,password) :
        self.webElement_input(self.username_input,username);
        self.webElement_input(self.password_input,password);
        self.webElement_click(self.login_button);
    
    def getText_appLogo(self) :
        return self.driver.find_element(*self.app_logo).text;

    def login_with_lockedaccount(self,username,password) :
        self.webElement_input(self.username_input,username);
        self.webElement_input(self.password_input,password);
        self.webElement_click(self.login_button);
    
    def getText_errormsg(self) :
        return self.driver.find_element(*self.error_msg).text;

    def clear_inputValues(self) :
        self.webElement_input_clear(self.username_input);
        self.webElement_input_clear(self.password_input);

    def logout_functionality(self) :
        self.webElement_click(self.sidebar_button);
        self.webElement_click(self.logout_button);