from actions.mobileapp_actions import Appium_Actions
from appium.webdriver.common.appiumby import AppiumBy

class Click_All_Navigation_Elements(Appium_Actions) :

    get_items_elemet = (AppiumBy.XPATH , "//android.widget.LinearLayout[@content-desc='Get Ideas']");
    my_recipies_element = (AppiumBy.XPATH , "//android.widget.LinearLayout[@content-desc='My Recipes']");
    videos_element = (AppiumBy.XPATH , "//android.widget.LinearLayout[@content-desc='Videos']");
    editorials_element = (AppiumBy.XPATH , "//android.widget.LinearLayout[@content-desc='Editorials']");
    activity_element = (AppiumBy.XPATH , "//android.widget.LinearLayout[@content-desc='Activity']/android.widget.FrameLayout");
    grocery_list_element = (AppiumBy.XPATH , "//android.widget.LinearLayout[@content-desc='Grocery List']");
    meal_planner_element = (AppiumBy.XPATH , "//android.widget.LinearLayout[@content-desc='Meal Planner']");

    def __init__(self,driver) :
        super().__init__(driver);

    def click_all_elements(self) :
        self.click_webelement(self.get_items_elemet);
        self.click_webelement(self.my_recipies_element);
        self.click_webelement(self.videos_element);
        self.click_webelement(self.editorials_element);
        self.click_webelement(self.activity_element);
        self.click_webelement(self.grocery_list_element);
        self.click_webelement(self.meal_planner_element);