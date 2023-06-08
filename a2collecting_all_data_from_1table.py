#https://m.cricbuzz.com/cricket-stats/icc-rankings/men/batting
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://m.cricbuzz.com/cricket-stats/icc-rankings/men/batting")
driver.maximize_window()
driver.implicitly_wait(5)

#collecting how many rows there are
rows = driver.find_elements(By.XPATH,'//*[@id="top"]/div/div[5]/div[2]/div/table/tbody/tr')
totoalrows = len(rows)

#collecting number of columns
column= driver.find_elements(By.XPATH,'//*[@id="top"]/div/div[5]/div[2]/div/table/tbody/tr[1]/td')
totalcols = len(column)
#final staements 
print(f"the total amount of rows in this website is {totoalrows} and the total columns in this website is {totalcols}")

#COLLECTING WHATS IN THOSE ROWS OD DATA - THE MAIN BIT OF THIS PRACTICAL
for i in rows:
    print (i.text)
time.sleep(3)
driver.quit()