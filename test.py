import os
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Create Chrome options
# options = uc.ChromeOptions()

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\\Users\\hanss\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--profile-directory=Profile 2")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")  # Ensure remote debugging is enabled

# Initialize the Chrome driver with the specified options
service = Service(executable_path=os.getcwd()+'/chromedriver.exe')
driver = webdriver.Chrome(options=options,service=service)

try:
    # Open a website to test
    driver.get('http://www.google.com')

    # Example: Wait for the search box to be present and print the page title
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
    print("Page title is:", driver.title)

    # Perform additional actions if needed
    # ...

except Exception as e:
    print("Exception occurred:")
    print(str(e))
finally:
    # Ensure the browser is closed properly
    driver.quit()
    print("Browser closed.")
