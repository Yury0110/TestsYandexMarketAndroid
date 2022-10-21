import pytest as pytest
from appium import webdriver

desired_capabilities = {
    'platformName': "Android",
    'platformVersion': "12.0",
    'deviceName': "Pixel 5",
    'app': "/Users/sadness_azathoth/Library/Android/yandex_market.v4.33.3028.apk"
}


@pytest.fixture
def mobile_driver(request):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    yield driver
    driver.quit()
