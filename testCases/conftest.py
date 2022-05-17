import pytest
from selenium import webdriver


# @pytest.fixture()
# def setup(browser):
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#         print("Starting Chrome Browser ............")
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#         print("Starting Firefox Browser ..........")
#     else:
#         driver = webdriver.Edge()
#     return driver


def pytest_addoption(parser):  # this will get the value from CLI/Hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


# Hooks for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = "Selenium Hybrid Framework"
    config._metadata['Module Name'] = "Customers"
    config._metadata['Tester Name'] = "Prashant"


# Hooks for delete modify env info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


@pytest.fixture(params=["chrome"], scope="function")
def setup(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    if request.param == "firefox":
        driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
