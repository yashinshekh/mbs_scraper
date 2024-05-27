import os
import platform

if platform.system() == "Windows":
    try:
        import undetected_chromedriver
        from parsel import Selector
        from selenium import webdriver
        import pyautogui
    except ImportError:
        os.system('python -m pip install parsel')
        os.system('python -m pip install selenium')
        os.system('python -m pip install undetected_chromedriver')
        os.system('python -m pip install pyautogui')

else:
    try:
        import undetected_chromedriver
        from parsel import Selector
        from selenium import webdriver
        import pyautogui
    except ImportError:
        os.system('python3 -m pip install parsel')
        os.system('python3 -m pip install selenium')
        os.system('python3 -m pip install undetected_chromedriver')
        os.system('python3 -m pip install pyautogui')


from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from parsel import Selector
import pyautogui
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def waituntil(string):
    if string not in str(driver.page_source):
        time.sleep(3)
        print("Waiting!!")
        return waituntil(string)
    return


def getdata():

    datas = Selector(text=driver.page_source).xpath('.//*[@class="mbs-window-content next-page-loaded"]//tbody/tr').extract()
    for data in datas:
        sel = Selector(text=data)

        title = sel.xpath('.//td[2]//a/text()').extract_first()
        link = sel.xpath('.//td[2]//a/@href').extract_first()
        image = sel.xpath('.//td[2]//img/@src').extract_first()
        brand = sel.xpath('.//td[3]/span/text()').extract_first()
        price = sel.xpath('.//td[4]/div/b/text()').extract_first()
        category = sel.xpath('.//td[5]/span/text()').extract_first()
        rank = sel.xpath('.//td[6]/div/b/text()').extract_first()
        monthly_sales = sel.xpath('.//td[7]/text()').extract_first()
        revenue = sel.xpath('.//td[8]/text()').extract_first()
        reviews = sel.xpath('.//td[9]/div/span/text()').extract_first()
        rating = sel.xpath('.//td[10]/div/text()').extract_first()

        with open(category+'.txt','a') as f:
            f.write(f"Title : {title}\nPrice : {price}\nImage URL : {image}\nBSR : {monthly_sales}\nCategory : {category}\nLink : {link}")


        if 'Load next page' in str(driver.page_source):
            driver.find_element(By.XPATH,'.//button[contains(.,"Load next page")]').click()
            time.sleep(20)
            getdata()



if __name__ == '__main__':

    CHROME_PROFILE_PATH = r"C:\\Users\\hanss\\AppData\Local\\Google\\Chrome\\User Data\\Default"
    SEARCH_URL = "https://www.amazon.com/s?k=VUOAISJDIOJW&crid=K8RTEIQ80HZJ&sprefix=vuoaisjdiojw%2Caps%2C315&ref=nb_sb_noss"

    options = uc.ChromeOptions()
    # options = Options()
    if platform.system() == "Linux":
        options.add_argument("--user-data-dir=/home/yashin/.config/google-chrome/Default")
        driver = uc.Chrome(options=options,version_main=123)

    else:
        newpath = os.getenv('LOCALAPPDATA')+"\\Google\\Chrome\\User Data\\Profile 1\\Default"

        path = r"C:\Users\hanss\AppData\Local\Google\Chrome\User Data\Profile 2"
        options.add_argument(f"--user-data-dir=C:\\Users\\hanss\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")

        # options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
        # options.add_argument("profile-directory=Default")
        driver = uc.Chrome(options=options, version_main=125)

    time.sleep(3)
    driver.get("https://amazon.com")

    input("Ready...")
    waituntil('nav-global-location-popover-link')
    driver.find_element(By.XPATH,'.//*[@id="nav-global-location-popover-link"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'.//input[@id="GLUXZipUpdateInput"]').send_keys("10001")
    time.sleep(3)
    driver.find_element(By.XPATH,'.//span[contains(.,"Apply")]').click()
    time.sleep(3)

    driver.get(SEARCH_URL)
    print("Waiting for 15 seconds to make the MBS ready.")
    time.sleep(15)
    # input("make mbs ready ...")
    try:
        pyautogui.click(pyautogui.locateCenterOnScreen('mbs_extension.png'),button="left")
    except:
        print("MBS extension not found.")

    driver.find_element(By.XPATH,'.//button[contains(.,"Filters")]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'.//span[@class="header-title-text"][contains(.,"Rank")]/following-sibling::div/input[1]').send_keys(100)
    time.sleep(1)
    driver.find_element(By.XPATH,'.//span[@class="header-title-text"][contains(.,"Weight")]/following-sibling::div/input[2]').send_keys(5)
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    getdata()








