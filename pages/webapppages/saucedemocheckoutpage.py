from actions.saucedemo_actions import SauceDemo_Actions
from selenium.webdriver.common.by import By

class SauceDemoCheckOutPage(SauceDemo_Actions) :

    addToCartBackPack = (By.ID, "add-to-cart-sauce-labs-backpack");
    addToCartLogo = (By.CLASS_NAME,"shopping_cart_link");
    checkOutBtn = (By.ID,"checkout");
    firstnameInput = (By.ID,"first-name");
    lastnameInput = (By.ID , "last-name");
    postalCodeInput = (By.ID , "postal-code");
    continueBtn = (By.ID , "continue");
    finishBtn = (By.ID , "finish");
    backToProductsBtn = (By.ID, "back-to-products");

    def __init__(self,driver) :
        super().__init__(driver);

    def checkOut_functionality(self,firstname,lastname,pincode) :
        self.webElement_click(self.addToCartBackPack);
        self.webElement_click(self.addToCartLogo);
        self.webElement_click(self.checkOutBtn);
        self.webElement_input(self.firstnameInput,firstname);
        self.webElement_input(self.lastnameInput,lastname);
        self.webElement_input(self.postalCodeInput,pincode);
        self.webElement_click(self.continueBtn);
        self.webElement_click(self.finishBtn);
        self.webElement_click(self.backToProductsBtn);