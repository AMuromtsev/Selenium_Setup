import pytest
import os
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--protocol', default = 'https', choices = ['http','https'])
    parser.addoption('--baseurl', default='opencart.com')


DRIVERS = (os.path.abspath("..\drivers"))


@pytest.fixture
def driver(request):
    browser = request.config.getoption('browser')
    base_url = request.config.getoption('baseurl')
    protocol = request.config.getoption('protocol')
    _driver = None
    if browser == 'chrome':
        _driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver.exe")
    elif browser == 'firefox':
        _driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver.exe")
    elif browser == 'opera':
        _driver = webdriver.Opera(executable_path=f"{DRIVERS}/geckodriver.exe")
    elif browser == 'edge':
        _driver = webdriver.Edge(executable_path=f"{DRIVERS}/msedgedriver.exe")
    elif browser == 'yandex':
        _driver = webdriver.Edge(executable_path=f"{DRIVERS}\yandexdriver.exe")

    _driver.base_url = base_url
    _driver.protocol = protocol



    yield _driver

    _driver.quit()
