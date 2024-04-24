from actions.saucedemo_actions import SauceDemo_Actions 
from selenium.webdriver.common.by import By

class SideBarValidation(SauceDemo_Actions) :

    sidebarBtn = (By.ID,"react-burger-menu-btn");
    closeSidebarBtn = (By.ID , "react-burger-cross-btn");

    def __init__(self,driver) :
        super().__init__(driver);
    
    def clickOn_sidebarBtn(self) :
        self.webElement_click(self.sidebarBtn);

    def sideBar_validation(self,element) :
       status = self.driver.find_element(By.ID , element).is_displayed();
       return status;

    def clickOn_closeBtn(self) :
        self.webElement_click(self.closeSidebarBtn);