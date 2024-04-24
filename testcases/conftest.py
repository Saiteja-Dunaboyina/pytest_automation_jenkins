import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from datetime import datetime
from pathlib import Path
import json
import allure
import configparser
import os
import requests
from allure_commons.types import AttachmentType
from typing import Any, Dict
from appium.webdriver.appium_service import AppiumService
from appium.options.common import AppiumOptions


current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir,'..','config', 'config.ini')

#this fixture will provide the driver for the web application
@pytest.fixture(scope= "session")
def browser_setup() :
    global driver;
    service = Service(ChromeDriverManager().install());
    chrome_options = Options();
    chrome_options.add_experimental_option("detach",True);
    driver = webdriver.Chrome(service= service,options= chrome_options);
    driver.maximize_window();
    config = read_config();
    baseUrl = config["base_url"]
    driver.get(baseUrl);
    yield driver;
    driver.quit();

#this fixture will take the screenshot of the failed test cases
@pytest.fixture(autouse= True)
def log_on_failure(request):
    yield
    item = request.node
    if hasattr(item, "rep_call") and hasattr(item.rep_call, "failed") and item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=allure.attachment_type.PNG)

#this fixture will provide the html report for the test cases
@pytest.hookimpl(hookwrapper= True , tryfirst= True)
def pytest_runtest_makereport(item,call) :
    outcome = yield;
    rep = outcome.get_result();
    setattr(item,"rep_"+rep.when,rep)
    return rep

#this fixture will provide the html report for the test cases
@pytest.hookimpl(tryfirst= True)
def  pytest_configure(config) :
    today = datetime.now();
    report_dir = Path("reports",today.strftime('%Y%m%d'));
    report_dir.mkdir(parents= True,exist_ok= True);
    pytest_html = report_dir / f"report_{today.strftime('%Y%m%d%H%M')}.html" ;
    config.option.htmlpath = pytest_html;
    config.option.self_contained_html = True;

#this fixture will provide the title for the html report
def pytest_html_report_title(report) :
    report.title = "SauceDemo Test Report";

#this fixture will read the data from the json file for the UI section
@pytest.fixture()
def ui_json_data() :
    with open("./data/saucedemodata.json","r") as file :
        data = json.load(file)
    return data;

# this function will read the data in UI section in config file
def read_config(ui_path=config_path, section='UI'):
    parser = configparser.ConfigParser();
    parser.read(ui_path, encoding='utf-8');
    if parser.has_section(section):
        config = dict(parser.items(section));
    else:
        raise ValueError(f"Section '{section}' not found in the config file.");
    return config;

#this fixture will provide the data in API section in config file
@pytest.fixture()
def read_config_api(api_path=config_path, section='API') :
    parser = configparser.ConfigParser();
    parser.read(api_path, encoding='utf-8');
    if parser.has_section(section):
        config = dict(parser.items(section));
    else:
        raise ValueError(f"Section '{section}' not found in the config file.");
    return config;

#this fixture will read the data from the json file for the API section
@pytest.fixture()
def api_data() :
    with open("./data/apidata.json", "r") as file :
        data = json.load(file);
    return data;

#this fixture will provide the auth token for the API
@pytest.fixture()
def auth_token(api_data, read_config_api) :
    api_config = read_config_api
    response = requests.post(api_config["api_url"] + api_config["auth_end_point"],
                             json= api_data.get("auth_payload", {}))
    return response.json()["token"]

#this fixture will provide the booking id for the API
@pytest.fixture()
def post_booking_details(api_data,read_config_api,auth_token) :
    api_config = read_config_api
    response = requests.post(api_config["api_url"] + api_config["booking_base_endpoint"],
                             json = api_data.get("bookingdetails", {}), headers= { 'Cookie' : 'token=' + auth_token})
    assert response.status_code == 200 , f"Failed to create booking. Status  code : {response.status_code}"
    return response.json().get("bookingid" ,'')

#this function will provide the data in Mobile section in config file 
def read_mobile_config() :
    config = configparser.ConfigParser();
    config.read(config_path);
    if 'Mobile' in config:
        mobile_config = config['Mobile']
        return mobile_config
    else:
        raise Exception("Mobile section not found in config.ini")

#this fixture will provide the driver for the mobile application
@pytest.fixture(scope= "session")
def appium_driver_setup(request) :
    mobile_config  = read_mobile_config();
    appium_server = AppiumService();
    appium_server.start();

    cap : Dict[str, Any] = {
        "platformName": mobile_config["platformName"],
        "appium:deviceName": mobile_config["deviceName"],
        "appium:automationName": mobile_config["automationName"],
        "appium:appPackage": mobile_config["appPackage"],
        "appium:appActivity": mobile_config["appActivity"],
        "appium:platformVersion": mobile_config["platformVersion"]
    }

    driver = webdriver.Remote(mobile_config["appium_server_url"],options=AppiumOptions().load_capabilities(cap));
    yield driver
    driver.quit();
    appium_server.stop();

#this fixture will provide the data from the json file for the mobile application
@pytest.fixture()
def mobile_json_data() :
    with open("./data/mobileapp.json","r") as file :
        data = json.load(file)
    return data;