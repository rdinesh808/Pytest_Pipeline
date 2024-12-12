import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    """Set up the WebDriver instance."""
    browser = request.config.getoption("--browser")
    driver = None

    # Browser selection logic
    if browser == "chrome":
        from selenium.webdriver.chrome.service import Service
        service = Service("../drivers/chromedriver/chromedriver.exe")
        option = webdriver.ChromeOptions()
        option.add_argument("--start-maximized")
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        driver = webdriver.Chrome(service=service, options=option)
    elif browser == "edge":
        from selenium.webdriver.edge.service import Service
        service = Service("../drivers/edgedriver/msedgedriver.exe")
        option = webdriver.EdgeOptions()
        option.add_argument("--start-maximized")
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        driver = webdriver.Edge(service=service, options=option)
    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        service = Service("../drivers/firefoxdriver/geckodriver.exe")
        option = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=option)
    else:
        raise ValueError("Your selected browser is not available. Please select Chrome, Edge, or Firefox driver.")

    # Attach the driver to the test class
    request.cls.driver = driver
    yield driver
    driver.quit()  # Quit the browser after all tests in the class


def pytest_addoption(parser):
    """Add custom options for pytest."""
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use for testing")
