from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = Service("C:\Dev\chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://orteil.dashnet.org/cookieclicker/")
#t_end = time.time() + 5
game = True
clicks = 0

time_start = time.time()
time_end = 10



#def power_up_checker():
def timer():
    time_start = time.time()
    time_end = 5
    while time.gmtime()[5] % 5 == 0:
        return True

upgrade_list = driver.find_element(By.ID, "products")
print(upgrade_list.text)

def clicker():
    cookie_click = driver.find_element(By.ID, "bigCookie").click()
    global clicks
    clicks += 1

lang_select = driver.find_element(By.ID, "langSelect-EN").click()

while game == True:
    clicker()
    if timer():
        print(time.gmtime())
        #upgrade_list = driver.find_element(By.ID, "products")
        #print()
        for n in range(0, 10):
            try:
                button = f"product{n}"
                driver.find_element(By.ID, button).click()
            except ElementNotInteractableException:
                pass




        #cursor = driver.find_element(By.ID, "product0")
        #grandma = driver.find_element(By.ID, "product1")
        #if int(driver.find_element(By.ID, "productPrice0").text) <= int(driver.find_element(By.ID, "productPrice1").text):
        #cursor.click()
        #else:
            #grandma.click()






