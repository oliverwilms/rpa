# validate_chromedriver.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import sys

def main():
    try:
        # Optional: set Chrome options (headless mode for no UI)
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Uncomment for headless mode

        # Path to your ChromeDriver (if not in PATH, set full path here)
        service = Service(executable_path="chromedriver")

        # Start Chrome
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open a test page
        driver.get("https://www.example.com")

        # Print the page title to confirm success
        print("Page title is:", driver.title)

        # Close browser
        driver.quit()

        print("✅ ChromeDriver setup is working correctly.")

    except WebDriverException as e:
        print("❌ ChromeDriver test failed:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
