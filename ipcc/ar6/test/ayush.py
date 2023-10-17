from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from get_endpoint_html import setup_driver
import time
import os

# Author: Ayush Garg
# Start the browser and navigate to the page
driver = setup_driver()
driver.get("https://apps.ipcc.ch/glossary/")

# Define the expected page letters for pagination
page_letters = [
    "123",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "Y",
    "Z",
]

for letter in page_letters:
    # Find and click the desired page link
    page_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, f'a.page-link.prefixlink[data-prefix="{letter}"]')
        )
    )
    page_link.click()

    # Wait for the table to load
    time.sleep(3)

    # Find all the spans in the table
    spans = driver.find_elements(By.CSS_SELECTOR, "tbody tr td span.alllink")

    for span in spans:
        # Determine the title for the filename from the span text
        title = span.text.split(" «")[0]  # Extracting the part before the '«'
        safe_title = "".join(
            [c if c.isalnum() else "_" for c in title]
        )  # make it safe for a filename

        # Click the span to open the modal
        span.click()

        # Wait for the modal to load
        time.sleep(3)

        # Extract the modal content
        modal_content = driver.find_element(
            By.CSS_SELECTOR, ".modal-content"
        ).get_attribute("outerHTML")

        filename = f"{safe_title}_{letter}.html"

        # Save content to the file
        with open(os.path.join(filename), "w", encoding="utf-8") as f:
            f.write(modal_content)

        # Close the modal
        close_button = driver.find_element(
            By.CSS_SELECTOR, 'button.btn.btn-outline-primary[data-bs-dismiss="modal"]'
        )
        close_button.click()

        # Wait for the modal to close
        time.sleep(1)

driver.close()