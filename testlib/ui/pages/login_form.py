from .. import by, ui

user_email = ui.element({
    'IOS': by.accessibility_id('emailInput'),
    'WEB': by.css('[type=login]'),
    'ANDROID': by.xpath('(//android.widget.EditText)[1]')
})

user_password = ui.element({
    'IOS': by.accessibility_id('passwordInput'),
    'WEB': by.css('[type=password]'),
    'ANDROID': by.xpath('(//android.widget.EditText)[2]')
})

submit_button = ui.element({
    'IOS': by.accessibility_id('signin-button'),
    'WEB': by.css('[type="submit"]'),
    'ANDROID': by.xpath('//android.widget.FrameLayout/android.view.ViewGroup[2]//android.widget.TextView')
})


def login_with(email, password):
    user_email.set(email)
    user_password.set(password)
    submit_button.click()
