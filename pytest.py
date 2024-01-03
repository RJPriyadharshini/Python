# test_example.py
import pytest

# Start with or ends with "Test" word
# Files name also contain "Test" in starting or in ending
"""
def test_m1():
    a=1
    b=2
    assert a+b==3,  "test passed" # msg only print test is failed

def test_m2():
    assert 3 - 1 == 4, "TEST FAILED"


# py.test -k login -v
# give detail explanation
def test_login():
    assert "admin"=="admin"


# DAY - 2

# Marker
@pytest.mark.login
def test_login():
    assert "admin"=="admin"

@pytest.mark.login
def test_m1():
    assert 5+5==10
def test_m2():
    assert 11==11


# In Console -  pytest -m login    only select the mark as login

# pip install pytest.xdist  for parallel mode

def test_google():
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver=webdriver.Chrome()
    driver.get("https://www.google.com")
    assert driver.title =="Google"
    driver.quit()

def test_orangehrm():
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver=webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    assert driver.title =="OrangeHR",   "Test faailed"
    driver.quit()

# pytest -n 5

# ( 5 said about 5 diff browser opening at the same time)
# Run in parallel mode means



# DAY-3

from selenium import webdriver

driver =None

def setup_module(module):
    global driver
    driver=webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")

def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title=="Google"

def test_google_url():
    assert driver.current_url=="google.com", "TEST"


# pip install pytest-html   "1st install the html"

# pytest -v -s --html=google_test_report.html    download the report

"""

from selenium import webdriver

driver =None
@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("Setup")
    driver=webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")

    yield
    print("....Tear down")
    driver.quit()

def test_m1(init_driver):
    assert driver.title=='Google'

def test_m2():
    assert 1+4==5

# -v more ellaborate ans
# -s print in console
