from actions.mobileapp_actions import Appium_Actions
from appium.webdriver.common.appiumby import AppiumBy

class  More_Options_Validation(Appium_Actions) :

    moreoptions_button = (AppiumBy.XPATH , "//android.widget.ImageView[@content-desc='More options']");
    title_text = (AppiumBy.XPATH,"//android.widget.TextView[@text='What to Make This week']")
    app_update_button = (AppiumBy.XPATH , "//android.widget.TextView[@text='App Update']");

    def __init__(self,driver) :
        super().__init__(driver);

    def click_on_moreoptions(self) :
        self.click_webelement(self.moreoptions_button);

    def moreoptions_validation(self ,element) :
        status = self.driver.find_element(AppiumBy.XPATH , "//android.widget.TextView[@text = '" + element + "']").is_enabled();
        return status;

    def click_on_app_update(self) :
        self.click_webelement(self.app_update_button);

