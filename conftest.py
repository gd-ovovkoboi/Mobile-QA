import os
from configparser import ConfigParser

import pytest
from appium import webdriver

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

parser = ConfigParser()
parser.read(os.path.join(ROOT_DIR, 'config.ini'))


@pytest.fixture()
def driver_setup(request):
    desired_caps = {
        'platformName': parser.get('driver', 'platform_name'),
        'deviceName': parser.get('driver', 'device_name'),
        'appPackage': parser.get('driver', 'app_package'),
        'appActivity': parser.get('driver', 'app_activity'),
        'app': os.path.join(ROOT_DIR, parser.get('driver', 'app'))
    }
    request.instance.driver = webdriver.Remote(parser.get('driver', 'server_address'), desired_caps)

    def tear_down():
        request.instance.driver.quit()

    request.addfinalizer(tear_down)
