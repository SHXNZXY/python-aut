#https://m.cricbuzz.com/cricket-stats/icc-rankings/men/batting
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
#this means no synchronisation issue when it comes to if chrome and chrome manager same version , add line 4 as import to support
driver.get("https://m.cricbuzz.com/cricket-stats/icc-rankings/men/batting")
driver.maximize_window()
driver.implicitly_wait(5)

#collecting how many rows there are
rows = driver.find_elements(By.XPATH,'//*[@id="top"]/div/div[5]/div[2]/div/table/tbody/tr')
#went to only the header of the table and copied the XPATH but took the last [1] out because that specified that row only
#the pressed ctrl f and pasted the XPath and played around with it //*[@id="top"]/div/div[5]/div[2]/div/table/tbody/tr[1] , play around with it
totoalrows = len(rows)
#collecting colums numbers
column= driver.find_elements(By.XPATH,'//*[@id="top"]/div/div[5]/div[2]/div/table/tbody/tr[1]/td')
totalcols = len(column)
#final staement for better output
print(f"the total amount of rows in this website is {totoalrows} and the total columns in this website is {totalcols}")
time.sleep(3)
driver.quit()