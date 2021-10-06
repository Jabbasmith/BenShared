from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

EXTENSION_PATH =r"C:\Users\jimle\OneDrive\Desktop\metamask-chrome-10.2.0.crx"

chop = webdriver.ChromeOptions()
chop.add_extension(EXTENSION_PATH)
driver = webdriver.chrome(options=chop)

driver.get("https://techwithtim.net")
