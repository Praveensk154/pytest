from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup():
    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    else :
        chrome_options = webdriver.ChromeOptions
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.ebay.com/")
    driver.maximize_window()
    return driver
