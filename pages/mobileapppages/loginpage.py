from actions.mobileapp_actions import Appium_Actions
from appium.webdriver.common.appiumby import AppiumBy
class  LoginPage(Appium_Actions) :

    signin_button = (AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']");
    email_input = (AppiumBy.XPATH,"//android.widget.EditText[@resource-id='com.bigoven.android:id/email']");
    password_input = (AppiumBy.XPATH,"//android.widget.EditText[@resource-id='com.bigoven.android:id/password']");
    # confirm_signin_button = ("xpath","//android.widget.TextView[@text='Sign in']");
    moreoptions_button = (AppiumBy.XPATH , "//android.widget.ImageView[@content-desc='More options']");
    settings_button = (AppiumBy.XPATH , "//android.widget.TextView[@text = 'Settings']");
    signout_button = (AppiumBy.XPATH , "//android.widget.TextView[@text='Sign Out']");
    confrim_signout_button = (AppiumBy.XPATH , "//android.widget.Button[@resource-id='android:id/button1']");

    def  __init__ (self, driver):
        super().__init__(driver);

    def  login_functionality(self ,email,password) :
        self.click_webelement(self.signin_button);
        self.input_webelement(self.email_input,email);
        self.input_webelement(self.password_input,password);
        self.click_webelement(self.signin_button);
        

    def  logout_functionality( self ) :
        self.click_webelement(self.moreoptions_button);
        self.click_webelement(self.settings_button);
        self.click_webelement(self.signout_button);
        self.click_webelement(self.confrim_signout_button);

    