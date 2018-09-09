import pytest
from base.webdriverfactory import WebDriverFactory


##BeforeMethod and aftermethod
@pytest.yield_fixture()
def setUp():
    print("Running Method level setup")
    yield
    print("Running method level teardown")

##beforeclass and after class
@pytest.yield_fixture(scope= "class")
def oneTimeSetUp(request, browser):
    print("Running one time setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Driver is closed as part of tear down")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")