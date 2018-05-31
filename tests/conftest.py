import pytest
from selene import factory

import config
from testlib.ui import driver, application


@pytest.fixture(scope='session' if config.test_run.ONE_SESSION else 'function')
def app():
    ui_driver = driver.get()
    factory.set_shared_driver(ui_driver)

    yield application

    driver.close(ui_driver)


@pytest.fixture(autouse=config.test_run.BROWSER_LOGS and config.test_run.IS_WEB)
def browser_log(app):
    """Printing browser logs for web tests"""
    yield

    print("\n\tBROWSER CONSOLE LOGS:")
    for log in app.driver.get_log('browser'):
        print(f'\n{log}\n')
