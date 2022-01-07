from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib.parse
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

CHROME_PROFILE_PATH="user-data-dir=C:\\Users\\kesha\\AppData\\Local\\Google\\Chrome\\User Data\\Wtsp"

Link = "https://web.whatsapp.com/"
wait = None

def whatsapp_login():
    global wait, driver, Link
    chrome_options = webdriver.ChromeOptions(); 
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_argument(CHROME_PROFILE_PATH)
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    wait = WebDriverWait(driver, 20)
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB IF DISPLAYED")
    driver.get(Link)
    driver.maximize_window()
    print("QR CODE SCANNED")

def send_message_to_unsavaed_contact(number,msg):
    print("In send_message_to_unsavaed_contact method")
    params = {'phone': str(number), 'text': str(msg)}
    end = urllib.parse.urlencode(params)
    final_url = Link + 'send?' + end
    print(final_url)
    driver.get(final_url)
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Menu"]')))
    print("Page loaded successfully.")
    action = ActionChains(driver)
    sleep(8)
    action.send_keys(Keys.ENTER)
    action.perform()
    sleep(5)
    print("Message sent successfully.")
    driver.close()
    driver.quit()

whatsapp_login()
send_message_to_unsavaed_contact("919829867516", "Hi There")