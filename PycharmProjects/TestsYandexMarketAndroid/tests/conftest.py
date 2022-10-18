import pytest as pytest
from appium import webdriver

desired_capabilities = {
    'platformName': "Android",
    'platformVersion': "12.0",
    'deviceName': "Pixel 5",
    'app': "ПУТЬ К APK ФАЙЛУ"
}


@pytest.fixture
def mobile_driver(request):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    yield driver
    driver.quit()
