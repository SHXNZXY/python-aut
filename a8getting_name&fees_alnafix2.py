#the by syntac has changed from when wathching lectures so its a bit different now .
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://alnafi.com/courses/python")
driver.maximize_window()
time.sleep(5)

driver.execute_script("window.open('https://alnafi.com/courses/sysops','new window')")
wins = driver.window_handles
time.sleep(5)

course=[]
fees = []

driver.switch_to.window(wins[0])
course_name=driver.find_element(by=By.XPATH, value='//*[@id="__nuxt"]/div/div[4]/div[1]/section[1]/div[1]/div/aside[1]/div/h1').text
course_fees= driver.find_element(by=By.XPATH, value='//*[@id="__nuxt"]/div/div[4]/div[1]/section[1]/div[1]/div/aside[2]/section/div[1]/div[2]/div[3]/span').text
course.append(course_name)
fees.append(course_fees)

driver.switch_to.window(wins[1])
time.sleep(8)
course_name=driver.find_element(by=By.XPATH, value='//*[@id="__nuxt"]/div/div[4]/div[1]/section[1]/div[1]/div/aside[1]/div/h1').text
course_fees= driver.find_element(by=By.XPATH, value='//*[@id="__nuxt"]/div/div[4]/div[1]/section[1]/div[1]/div/aside[2]/section/div[1]/div[2]/div[3]/span').text
course.append(course_name)
fees.append(course_fees)
print(course)
print(fees)

time.sleep(5)
driver.quit()