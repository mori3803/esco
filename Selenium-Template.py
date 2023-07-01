from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
import os
import time
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

username = os.environ["username"]
password = os.environ["password"]

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

driver.get('https://food.esfahansteel.ir/Lego.Web/Kevlar/Account/Login')
#print(driver.title)
driver.find_element("id", "UserName").send_keys(username)
driver.find_element("id", "Password").send_keys(password)
driver.find_element("id", "btnSubmit").click()
time.sleep(10)
txt = driver.find_elements_by_class_name("text-title")
#text = driver.find_element("class", "text-title")
driver.quit()
with open('./GitHub_Action_Results.txt', 'w') as f:
    f.write(f"This was written with a GitHub action {txt.text}")

