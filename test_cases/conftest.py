import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pytest_metadata.plugin import metadata_key

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Specify Browser Type chrome(Default) / firefox / edge"
    )

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver

    if browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError("Unspported browser type")
    return driver

def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Ecommerce Project, nopcommerce'
    config.stash[metadata_key]['Test Module Name '] = 'Admin Login Test'
    config.stash[metadata_key]['Tester Name'] = 'Pasha'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('Plugins',None)

