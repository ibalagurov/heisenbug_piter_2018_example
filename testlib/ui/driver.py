from appium import webdriver as appium_driver
from selenium import webdriver as selenium_driver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

import config

_capabilities = {
    'IOS': {
        'version': '1.8.0',
        'platformName': 'iOS',
        'platformVersion': config.test_run.IOS_VERSION,
        'deviceName': config.test_run.IOS_DEVICE_NAME,
        'app': config.test_run.MOBILE_APP,
        'noReset': False,
        'fullReset': False,
        'newCommandTimeout': config.test_run.APPIUM_TIMEOUT,
    },
    'ANDROID': {
        'version': '1.8.0',
        'platformName': 'Android',
        'platformVersion': config.test_run.ANDROID_VERSION,
        'deviceName': config.test_run.ANDROID_DEVICE_NAME,
        'app': config.test_run.MOBILE_APP,
        'noReset': False,
        'fullReset': False,
        'newCommandTimeout': config.test_run.APPIUM_TIMEOUT,
        "automationName": "UiAutomator2",
        "browserName": ""
    },
    'WEB': {
        **DesiredCapabilities.CHROME,
        'loggingPrefs': {'browser': 'ALL'}
    }
}


def get():
    caps = _capabilities[config.test_run.PLATFORM]
    if config.test_run.IS_MOBILE:
        return appium_driver.Remote(
            command_executor=config.test_run.APPIUM_SERVER,
            desired_capabilities=caps
        )

    return selenium_driver.Chrome(
        executable_path=ChromeDriverManager().install(),
        desired_capabilities=caps
    )


def close(driver):
    driver.close_app() if config.test_run.IS_MOBILE else driver.quit()
