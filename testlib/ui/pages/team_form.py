from .. import by, ui

url = ui.element({
    'IOS': by.accessibility_id('teamname-text-input'),
    'ANDROID': by.xpath('//android.support.v4.widget.DrawerLayout//android.widget.EditText')
})

next_button = ui.element({
    'IOS': by.accessibility_id("team-select-next-button"),
    'ANDROID': by.xpath(
        '//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'
    )
})


def type_url(text):
    url.set(text)
    next_button.click()
