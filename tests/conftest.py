"""
This module contains shared fixtures.
"""

import json
import pytest
import selenium.webdriver
from selenium.webdriver.firefox import options as FirefoxOptions


@pytest.fixture
def config(scope="session"):
    # Read the file
    with open("config.json") as config_file:
        config = json.load(config_file)

    # Asset values are acceptable
    assert config["browser"] in ["Firefox", "Chrome", "Headless Chrome", "Headless Firefox"]
    assert isinstance(config["implicit_wait"], int)
    assert config["implicit_wait"] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # Initialize the ChromeDriver instance
    if config["browser"] == "Firefox":
        b = selenium.webdriver.Firefox()
        b.maximize_window()
    elif config["browser"] == "Chrome":
        b = selenium.webdriver.Chrome()
        b.maximize_window()
    elif config["browser"] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("headless")
        b = selenium.webdriver.Chrome(options=opts)
    elif config["browser"] == "Headless Firefox":
        opts = selenium.webdriver.FirefoxOptions()
        opts.add_argument("--headless")
        b = selenium.webdriver.Firefox(options=opts)
    else:
        raise Exception(f'Browser "{config['browser']}" is not supported')

    # Make its calls wait up to 10 sencods for elements to appear
    b.implicitly_wait(config["implicit_wait"])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
