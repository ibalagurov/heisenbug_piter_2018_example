import config
from selene import browser
from .pages import login_form
from .pages import team_form
from .pages import navigation_button

login_form = login_form
team_form = team_form
navigation_button = navigation_button


def login_as(as_user):
    user = config.auth.get_user(as_user)
    login_form.login_with(email=user['email'], password=user['password'])


def assert_page_name(page_name):
    pages = ['login']
    if page_name not in pages:
        raise ValueError(f'Undefined {page_name} page name. Should be in {pages} pages')


def visit_page(page_name):
    page = page_name.lower()
    assert_page_name(page)
    if config.test_run.IS_WEB:
        browser.open_url(config.routing.LOGIN_PAGE_URL)
    # uncomment if your mobile app have environment choosing screen
    # if page_name.lower() == 'login':
    #     if config.test_run.IS_MOBILE:
    #         team_form.type_url(text=config.routing.ORGANIZATION_URL)
