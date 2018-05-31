from .. import by, ui

page = ui.element({
    'IOS': by.accessibility_id('uptick.DrawerMenu'),
    'WEB': by.css('[data-testid="menu-toggler-block"]'),
    'ANDROID': by.xpath(
        '//android.support.v4.widget.DrawerLayout//android.widget.LinearLayout//android.widget.ImageButton'
    )
})
