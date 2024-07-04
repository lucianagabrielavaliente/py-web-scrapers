from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
import os
import json

CHROME_DRIVER_PATH = r"C:\Users\lucia\Desktop\Desktop\Portfolio\py-web-scrapers\web_bot\chromedriver.exe"
s = Service(CHROME_DRIVER_PATH)
OP = webdriver.ChromeOptions()
OP.add_argument('--headless')
DRIVER = webdriver.Chrome(service=s)

def screenshotPage():
    time.sleep(5)
    date_str = date.today().strftime("%Y-%m-%d")  
    output_file_name = f'screenshot-{date_str}.png'
    fpath = os.path.join(os.getcwd(), 'downloads', output_file_name)
    DRIVER.get_screenshot_as_file(fpath)

def login():
    DRIVER.maximize_window()
    with open('config.json') as configFile:
        credentials = json.load(configFile)
        time.sleep(5)
        DRIVER.find_element(By.XPATH, value="//a[@href='https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3Fdisplay%3DeyJ2ZXJpZmljYXRpb25TdHJhdGVneSI6InNvZnQifQ%253D%253D&display=eyJ2ZXJpZmljYXRpb25TdHJhdGVneSI6InNvZnQifQ%3D%3D']").click()
        time.sleep(2)
        username = DRIVER.find_element(By.CSS_SELECTOR,value="input[name='username']")
        username.clear()
        username.send_keys(credentials["USERNAME"])
        DRIVER.find_element(By.XPATH, value="//button[@id='login-submit']").click()
        time.sleep(5)
        password = DRIVER.find_element(By.CSS_SELECTOR,value="input[name='password']")
        password.clear()
        password.send_keys(credentials["PASSWORD"])
        DRIVER.find_element(By.XPATH, value="//button[@id='login-submit']").click()
        time.sleep(5)

def navigateToBoard():
    time.sleep(5)
    DRIVER.find_element(By.XPATH, value="//div[@title='{}']/ancestor::a".format('Mi tablero de Trello')).click()
    time.sleep(5)

def addTask():
    time.sleep(2)
    DRIVER.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/main/div/div/div[2]/div/div/div[1]/div[2]/div/ol/li[1]/div/div[3]/button[1]").click()
    time.sleep(5)
    task_text_area = DRIVER.find_element(By.XPATH, value="//textarea[contains(@class, 'qJv26NWQGVKzI9')]")
    task_text_area.clear()
    task_text_area.send_keys("Bot added task")
    time.sleep(5)
    DRIVER.find_element(By.XPATH,value="//button[contains(@class, 'SdamsUKjxSBwGb')]").click()
    time.sleep(5)
 
  
def main():
    try:
        DRIVER.get("https://trello.com")
        login()
        navigateToBoard()
        addTask()
        screenshotPage()
        input("Bot Operation Completed. Press any key...")
        DRIVER.close()
    except Exception as e:
        print(e)    
        DRIVER.close()


if __name__ == "__main__":
    main()