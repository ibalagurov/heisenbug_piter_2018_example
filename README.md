# Demo example for [presentation](https://2018.heisenbug-piter.ru/en/talks/2018/spb/6plww0slg8akuymkumm4iq/) [[video]](https://www.youtube.com/watch?v=YoMt08OcxMI)
target OS - Mac, so detailed install information provided only for it.
What is it? 
Demo login test for "one test for several platforms" approach

What do you need?
.app or/and .apk applications or/and web versions your application 

# Setup tools (if you don't have some of them)
1. Install brew `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
2. Install Python 3.6+: `brew install python3`
3. Install npm: `brew install npm`
4. Install Appium server: `npm install -g appium` or look [here](http://appium.io/)
5. For better debugging you can install [Appium inspector](https://github.com/appium/appium-desktop/releases)
6. Install Carthage: `brew install carthage`
7. Install chrome browser (or use some other - look at [driver configuration](testlib/ui/driver.py))
8. Install xcode (for ios simulator)
9. Install [android studio](https://developer.android.com/studio/) or any android simulator
10. Install Python dependencies: `. ./scripts/install_deps.sh `(Terminal from root project folder)
11. I can miss something: you can try for example [this](https://medium.com/@appiummanager/appium-setup-from-scratch-6388f5e6caee)

# Customize for your application:
1. Put ".app" or/and ".apk" into [mobile app](mobile_app) directory
2. Add application names in [config](config/test_run.py) or environment variables:
    * `export IOS_APP_NAME=my_app.app`
    * `export ANDROID_APP_NAME=my_app.apk`
    * `export LOGIN_PAGE_URL=https://my-app.com` for web version
3. Change locators for (there are some examples):
    * [login page](testlib/ui/pages/login_form.py)
    * [navigation page](testlib/ui/pages/navigation_button.py) - any element for assert success login
4. Configure through env variables or [configuration files](config/):
    * `export DEFAULT_LOGIN=admin`
    * `export DEFAULT_PASSWORD=1234`
5. If mobile app have environment choosing screen:
    * Uncomment [few lines](testlib/ui/application.py)
    * Set environment variable ORGANIZATION_URL
    * Add locators for [login page](testlib/ui/pages/team_form.py)
    
# Customize for your environment:
1. You also can [configure](config/test_run.py) devices, collecting browser logs and etc 
(through ANDROID_VERSION, ANDROID_DEVICE_NAME, IOS_VERSION, IOS_DEVICE_NAME variables) 

# Run tests:
1. Run appium server `appium` for iOS or Android
2. Choose platform `export PLATFORM='WEB'` or `IOS` or `ANDROID`
3. Activate virtual environment with dependencies: `pipenv shell`
4. Run tests `python3 -m pytest tests/ui` or just:
    * `. ./scripts/run_ios_tests.sh`
    * `. ./scripts/run_android_tests.sh`
    * `. ./scripts/run_web_tests.sh`

# Useful links:
1. [Appium-python documentation](https://github.com/appium/python-client)
2. [Selene](https://github.com/yashaka/selene)
3. [Pytest](https://docs.pytest.org/en/latest/)
4. If you want to interact with some elements through pure selenium / appium look at [commented method as example](testlib/ui/ui.py)
