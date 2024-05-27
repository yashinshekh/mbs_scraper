from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Create Chrome options
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\\Users\\hanss\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("profile-directory=Profile 2")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")

# Initialize the Chrome driver with the specified options
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

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
