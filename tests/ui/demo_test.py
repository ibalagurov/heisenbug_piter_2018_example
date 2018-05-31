from selene.conditions import visible

import config


def test_login_with_login_and_password(app):
    app.visit_page(page_name='login')

    app.login_form.login_with(
        email=config.auth.DEFAULT_LOGIN,
        password=config.auth.DEFAULT_PASSWORD
    )

    app.navigation_button.page.should_be(visible)


def test_login_by_default_user(app):
    app.visit_page(page_name='login')

    app.login_as(as_user='default')

    app.navigation_button.page.should_be(visible)
