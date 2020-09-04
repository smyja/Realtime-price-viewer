import os
os.chmod('./chromedriver', 0o755)
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def scrape():

    opt = Options()
    opt.add_argument('--headless')
    opt.add_argument("--remote-debugging-port=9222")
    opt.add_argument("--no-sandbox")
    opt.add_argument("--disable-gpu")
    opt.add_argument("--disable-dev-shm-usage")
    opt.add_argument("--start-maximized")
    opt.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opt, 
    executable_path='./chromedriver')
    driver.get('https://www.ig.com/en/forex/markets-forex')


    timeout = 10

    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(
                (By.XPATH,
                "//div[@class='dynamic-table__cell']")
            )
        )
    except TimeoutException:
        print("Struggling to get the page....Have faith in this buggy script!")
        
    data = []

    while not data:
        for elm in driver.find_elements(By.CSS_SELECTOR, "span[data-field=V2-F-BID]"):
            if elm.text and elm.text != '-': # Maybe check on contains digit
                data.append(elm.text)
        time.sleep(7)

        
    tet =[]
    while not tet:
        for em in driver.find_elements(By.CSS_SELECTOR, "span[data-field=OFR]"):
            if em.text and em.text != '-': # Maybe check on contains digit
                tet.append(em.text)
        time.sleep(7)
    print(data)
    
    
