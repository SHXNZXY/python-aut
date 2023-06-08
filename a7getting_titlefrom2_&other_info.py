import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://alnafi.com")
driver.maximize_window()
time.sleep(5)
driver.execute_script("window.open('https://google.com','new window')")
wins = driver.window_handles
time.sleep(2)
driver.switch_to.window(wins[0])
print("\n=================This is my zero index (alnafi)==============\n"+ driver.title)
mylanfi=driver.find_element(by=By.XPATH, value='//*[@id="__nuxt"]/div/div[4]/section[1]/section[2]/section/div/span')
print(mylanfi.text)
time.sleep(2)
driver.switch_to.window(wins[1])
print("\n=====================This is my first index(google)=====================\n " + driver.title)
mygoogle = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[5]/div[2]/div[2]/a')
print(mygoogle.text)
time.sleep(5)
driver.quit()