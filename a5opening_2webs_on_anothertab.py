import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(5)
#get al nafi and maximixe window
driver.get("https://alnafi.com")
driver.maximize_window()
time.sleep(5)
print(driver.title)

#for google
driver.execute_script("window.open('https://google.com','new window')")
print(driver.title)
#the output for this is wrong but we will look into this after
time.sleep(5)
driver.quit()