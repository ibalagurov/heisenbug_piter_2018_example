from appium.webdriver.common.mobileby import MobileBy
from selene.support import by


def accessibility_id(_id):
    return MobileBy.ACCESSIBILITY_ID, _id


css = by.css
xpath = by.xpath
