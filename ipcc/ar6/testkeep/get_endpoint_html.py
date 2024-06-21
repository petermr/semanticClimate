import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import logging


def setup_driver():
    """
    The function `setup_driver` returns a Chrome WebDriver instance with specified options and settings.
    :return: The function `setup_driver()` returns a Chrome WebDriver instance.
    """
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.page_load_strategy = "none"
    chrome_path = ChromeDriverManager().install()
    chrome_service = Service(chrome_path)
    driver = Chrome(options=options, service=chrome_service)
    return driver


def safe_click_element(driver, element):
    """
    The `safe_click_element` function is a Python code snippet that attempts to click on a web element
    in a safe manner, handling potential exceptions and using different strategies if necessary.

    :param driver: The "driver" parameter is an instance of a WebDriver, which is used to interact with
    a web browser. It allows you to navigate to web pages, interact with elements on the page, and
    perform various actions
    :param element: The `element` parameter is the web element that you want to click on. It can be any
    valid web element object, such as an instance of `WebElement` class in Selenium
    """
    try:
        # Wait for the element to be clickable
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, element.get_attribute("outerHTML")))
        )
        element.click()
    except ElementClickInterceptedException:
        # If the element is not clickable, scroll to it and try again
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    except:
        # If it still doesn't work, use JavaScript to click on the element
        driver.execute_script("arguments[0].click();", element)


def get_page_source(driver, url):
    """
    The function `get_page_source` takes a web driver and a URL as input, navigates to the URL using the
    driver, waits for 3 seconds, and returns the page source code.

    :param driver: The driver parameter is an instance of a web driver, such as Selenium's WebDriver. It
    is used to control the web browser and perform actions like navigating to a URL, interacting with
    elements on the page, and retrieving the page source
    :param url: The URL of the webpage you want to retrieve the source code from
    :return: the page source of the website after the driver navigates to the specified URL.
    """
    driver.get(url)
    time.sleep(3)
    return driver.page_source


def click_expand_buttons(driver):
    """
    The function `click_expand_buttons` clicks on "Expand section" buttons and "Read more" paragraphs on
    a webpage using Selenium.

    :param driver: The "driver" parameter is an instance of a web driver, such as Selenium's WebDriver,
    that is used to interact with a web page. It is responsible for finding elements on the page and
    performing actions like clicking on buttons or links
    """
    # Clicking "Expand section" buttons
    expand_buttons = driver.find_elements(
        By.XPATH,
        '//button[contains(@class, "chapter-expand") and contains(text(), "Expand section")]',
    )
    for button in expand_buttons:
        safe_click_element(driver, button)
        time.sleep(1)  # Wait for the section to expand

    # Clicking "Read more" paragraphs
    read_more_elements = driver.find_elements(
        By.XPATH,
        '//p[contains(@class, "expand-paras") and contains(text(), "Read more...")]',
    )
    for element in read_more_elements:
        safe_click_element(driver, element)
        time.sleep(1)  # Wait for the section to expand


def extract_text_from_elements(driver, tag_name):
    """
    The function extracts text from elements with a specified tag name using a Selenium WebDriver.

    :param driver: The "driver" parameter is an instance of a web driver, such as Selenium WebDriver,
    that is used to interact with a web page. It is responsible for navigating to the page, finding
    elements, and performing actions on them
    :param tag_name: The tag name is a string that represents the HTML tag name of the elements you want
    to extract text from. For example, if you want to extract text from all the <p> tags on a webpage,
    you would pass "p" as the tag_name parameter
    :return: a list of text extracted from elements found by the given tag name.
    """
    elements = driver.find_elements(By.TAG_NAME, tag_name)
    return [element.text.strip() for element in elements if element.text.strip()]


def save_to_file(filename, content):
    """
    The function `save_to_file` saves the given content to a file with the specified filename.

    :param filename: The filename parameter is a string that represents the name of the file you want to
    save the content to
    :param content: The content parameter is the data that you want to save to the file. It can be a
    string, a list of strings, or any other data type that can be converted to a string
    """
    with open(filename, "w") as f:
        f.write(content)


def main():
    print("Starting the main function...")
    driver = setup_driver()
    url = "https://www.ipcc.ch/report/ar6/syr/longer-report/"
    print(f"Fetching page source from URL: {url}")
    html_source = get_page_source(driver, url)
    print("Clicking expand buttons...")
    click_expand_buttons(driver)
    print("Extracting text from elements...")
    # all_text = []
    # all_text.extend(extract_text_from_elements(driver, "span"))
    # all_text.extend(extract_text_from_elements(driver, "p"))
    # result_text = "\n".join(all_text)
    print("Saving to files...")
    save_to_file("complete_text.html", html_source)
    # save_to_file("only_text.txt", result_text)
    print("Quitting the driver...")
    driver.quit()
    print("Done.")


if __name__ == "__main__":
    main()


"""
Added by Ayush Garg to expand the buttons in IPCC html endpoints.
"""
