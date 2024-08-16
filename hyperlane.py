import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

def function():
    addresses = [
    'adres1',
    'adres2',
    'adres3', ##istediğin kadar ekle
]

    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True) 
    options.add_argument("start-maximized")
    options.add_argument("window-size=1920,1080")
    options.add_argument("--lang=en")
    options.add_argument("--headless")
    options.add_argument("disable-infobars")
    options.add_argument("disable-popup-blocking")
    options.add_argument('log-level=3')
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    driver = webdriver.Chrome(options=options)

    m = 0
    for addr in addresses:
        try:
            driver.get(f"https://explorer.hyperlane.xyz/?search={addr}")
            wait = WebDriverWait(driver,3)
            time.sleep(random.uniform(5,6))
            xxx = wait.until(EC.presence_of_element_located((By.XPATH,"//th[contains(text(), 'Destination')]")))
            dates = driver.find_elements(By.XPATH,"//a[contains(text(), '/')]")
            agos = driver.find_elements(By.XPATH,"//a[contains(text(), 'ago')]")
            ago_list = []
            date_list = []

            if dates:
                for date in dates:
                    date_list.append(date.text)
                unique_date_list = set(date_list)

            if agos:
                for ago in agos:
                    ago_list.append(ago.text)
            total_tx = len(date_list) + len(ago_list)

            if not ago_list:
                last_tx = date_list[0]
            else:
                last_tx = ago_list[0]

            if not agos:
                unique_days = len(unique_date_list)
            else:
                unique_days = len(unique_date_list) + 1       

            print(f"Address:{m}, Total TX:{total_tx}, Unique Days:{unique_days}, Last tX:{last_tx}")
        except Exception as e:
            print(f"Address:{m} An err occured {e}")
        m = m + 1
#driver.quit()

function()