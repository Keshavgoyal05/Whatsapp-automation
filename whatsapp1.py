from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib.parse
from webdriver_manager.chrome import ChromeDriverManager

CHROME_PROFILE_PATH="user-data-dir=C:\\Users\\kesha\\AppData\\Local\\Google\\Chrome\\User Data\\Wtsp"

Link = "https://web.whatsapp.com/"
wait = None

def whatsapp_login():
    global wait, driver, Link
    #chrome_options = Options()
    
    chrome_options = webdriver.ChromeOptions(); 
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_argument(CHROME_PROFILE_PATH)
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

    #driver = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait(driver, 20)
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB IF DISPLAYED")
    driver.get(Link)
    driver.maximize_window()
    print("QR CODE SCANNED")

def send_message(name,msg,count):
    user_group_xpath = '//span[@title = "{}"]'.format(name)
    
    for retry in range(3):
        try:
            sleep(3)
            wait.until(EC.presence_of_element_located((By.XPATH, user_group_xpath))).click()
            break
        except Exception:
            print("retry:{} {} not found in your contact list".format(retry,name))
            if retry==2:return
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
    for index in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button/span').click()
    print("Message send successfully.")

def send_attachment(name, file_name):
    user_group_xpath = '//span[@title = "{}"]'.format(name)
    print("in send_attachment method")
    for retry in range(3):
        try:
            sleep(3)
            wait.until(EC.presence_of_element_located((By.XPATH, user_group_xpath))).click()
            break
        except Exception:
            print("retry:{} {} not found in your contact list".format(retry,name))
            if retry==2:return
    attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()
    attachment = driver.find_element_by_xpath(
        '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    attachment.send_keys(file_name)
    sleep(5)
    #send = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send-light"]')))
    #send.click()
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/span/div/div/span').click()
    print("File send successfully.")

def send_message_to_unsavaed_contact(number,msg,count):
    # Reference : https://faq.whatsapp.com/en/android/26000030/
    print("In send_message_to_unsavaed_contact method")
    params = {'phone': str(number), 'text': str(msg)}
    end = urllib.parse.urlencode(params)
    final_url = Link + 'send?' + end
    print(final_url)
    driver.get(final_url)
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Menu"]')))
    print("Page loaded successfully.")
    '''
    for retry in range(3):
        try:
            #sleep(5)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[3]/button'))).click()
            break
        except Exception as e:
            print("Fail during click on send button.")
            if retry==2:return
    '''
    sleep(2)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[2]/button/span').click()

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
    for index in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[2]/button/span').click()
    print("Message sent successfully.")

def send_attachment_to_unsavaed_contact(number, file_name):
    print("In send_attachment_to_unsavaed_contact method")
    params = {'phone': str(number)}
    end = urllib.parse.urlencode(params)
    final_url = Link + 'send?' + end
    print(final_url)
    driver.get(final_url)
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Menu"]')))
    print("Page loaded successfully.")
    for retry in range(3):
        try:
            sleep(5)
            wait.until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Attach"]'))).click()
            break
        except Exception as e:
            print("Fail during click on Attachment button.")
            if retry==2:return
    attachment = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    attachment.send_keys(file_name)
    sleep(5)
    #send = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send-light"]')))
    #send.click()
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/span/div/div/span').click()
    print("File send successfully.")

    print("File sent successfully.")


if __name__ == "__main__":

    print("Web Page Open")
    # Let us login and Scan
    whatsapp_login()
    #send_message("Bittu", "Hello", 2)
    sleep(1)
    #send_attachment("Mummy", r"E:\cognizant_internship\js\NALA.jpg")
    #send_attachment("Mummy", r"E:\PPT and DOCX\smart india hackthon\SIH.pdf")
    sleep(5)
    # Please Update Contact Number And Attachment Path
    send_message_to_unsavaed_contact("919829867516", "Hi There", 5)
    #sleep(1)
    #send_attachment_to_unsavaed_contact("919829867516", r"E:\cognizant_internship\js\NALA.jpg")
    sleep(5)
    driver.close() # Close the Open tab
    driver.quit()
