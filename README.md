# e-commerce-backoffice

Python Playwright Automation

This repository contains a Python project using Playwright to automate web browsers for tasks like web scraping, end-to-end testing, and more.

Prerequisites

Before you begin, make sure you have the following installed:

Python 3.7 or later

pip (Python's package installer)

Installation

Clone this repository to your local machine:

git clone https://github.com/yourusername/python-playwright.git
cd python-playwright


Install the necessary dependencies:

pip install -r requirements.txt


Install Playwright and its browser dependencies:

python -m playwright install

Project Structure

Here's an overview of the project structure:

python-playwright/
├── tests/              # Directory containing all your test scripts
│   ├── test_example.py  # Sample test script
│   └── ...
├── requirements.txt     # Python dependencies
├── playwright.config.py # Playwright configuration file
└── README.md            # This file

Usage
Running Tests

To run the automated tests, you can use the following command:

python -m pytest


This will automatically discover and run all the test files located in the tests/ directory.

Sample Script

Here’s an example of a simple test that opens a website and verifies its title:

from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")
        assert page.title() == "Example Domain"
        browser.close()

if __name__ == "__main__":
    run()

Running the Script

You can execute the script with:

python test_example.py

Configuration

You can configure the browser context, launch options, and other settings by modifying the playwright.config.py file.

Example Configuration:
from playwright.sync_api import sync_playwright

def config_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch in headless mode (False to see the browser)
        page = browser.new_page()
        page.goto("https://example.com")
        # Do your automation here
        browser.close()

config_browser()

Dependencies

Playwright: A library to automate browser actions, handle multiple browser contexts, and more.

pytest: A framework to easily write test cases and run them.

To install all dependencies at once:

pip install -r requirements.txt


requirements.txt example:

playwright
pytest

Troubleshooting

If you encounter an error related to missing browsers, run:

python -m playwright install


If you're running into issues with the version of Playwright, try updating it:

pip install --upgrade playwright

Contributing

If you'd like to contribute to this project, please fork the repository, create a new branch, and submit a pull request with your changes.

Steps to Contribute:

Fork this repository

Create a new branch: git checkout -b feature-branch

Make your changes

Commit your changes: git commit -m 'Add feature or fix issue'

Push to the branch: git push origin feature-branch

Create a pull request

License

This project is licensed under the MIT License - see the LICENSE
 file for details.
