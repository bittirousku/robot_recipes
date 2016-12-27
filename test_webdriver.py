"""
Test running a webdriver
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def test_chrome():
    """Test chromedriver."""
    options = webdriver.ChromeOptions()
#   Force chrome location:
#  options.binary_location = '/usr/bin/chromium-browser
#   Disable hardware acceleration
#  options.add_argument("disable-gpu")

    browser = webdriver.Chrome(
        chrome_options=options,
        service_args=["--verbose"],
        service_log_path="chromedriver.log"
    )

    browser.get("https://online.planmill.com/knowit/")

    title = browser.title
    print(title)
    browser.quit()
    assert title == "PlanMill - sign in"


def test_phantom():
    """PhantomJS doesn't support file download so this is useless."""
    browser = webdriver.PhantomJS("/home/robot/webdriver/phantomjs")

    browser.get("https://online.planmill.com/knowit/")
    print(browser.title)


test_chrome()
