from selene.support.jquery_style_selectors import s, ss
# from selene.conditions import enabled
import config


def locator_for_platform(selectors):
    return selectors.get(config.test_run.PLATFORM, 'Undefined Selector')


def element(selectors):
    return s(locator_for_platform(selectors))


def elements(selectors):
    return ss(locator_for_platform(selectors))


# def hacked_click(by_element):
#     # 11.3 mac os problems with enabled, but not visible elements
#     by_element.should_be(enabled)
#     selenium_element = by_element.__delegate__
#     selenium_element.click()
#     return by_element
