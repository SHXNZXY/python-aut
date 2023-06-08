import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://alnafi.com")
driver.maximize_window()
time.sleep(5)
print(driver.title)
driver.get("https://google.com")
print(driver.title)
time.sleep(5)
driver.quit()