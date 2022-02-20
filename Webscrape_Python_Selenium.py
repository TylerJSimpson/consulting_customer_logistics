#import packages
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import csv


#create filepath for correct chrome webdriver
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

#user login details
my_username = "REDACTED"
my_password = "REDACTED"

#log in on parent website
driver.get("https://www.loadmatch.com/login.cfm?returnURL=DD/directory/results.cfm?city%3DSAV%26added%3DNewest")
wait=WebDriverWait(driver,5)
#push login details
driver.find_element_by_name("contact_username").send_keys(my_username)
driver.find_element_by_name("contact_password").send_keys(my_password)
driver.find_element_by_name("login_user").click()
wait=WebDriverWait(driver,3)


wait=WebDriverWait(driver,10)
#switch to correct subsite
driver.get("https://www.drayage.com/directory/results.cfm?city=SAV&port=y&OceanCntrs=y&drvrs=y&showClicks=y")
#iterate through the "details" popup
trs = wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//html/body/table/tbody/tr/td/table[1]//tr[position()>2]")))
window_before = driver.window_handles[0]
full_list = []
for tr in trs:
    try:
        #find popup button and click it
        detail = tr.find_element(By.XPATH,".//a[contains(.,'detail')]")
        detail.click()
        wait = WebDriverWait(driver,5)
        
        #handle the tab switch
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        
        #extracting text of table 1
        #sleep used to avoid 404 errors
        sleep(2)
        my_list = []
        new_text = driver.find_elements_by_xpath("/html/body/table[1]")
        for text in new_text:
            my_list.append(text.text)
            
        #check if items are being extracted
        print(my_list)
        
        #append my_list to full_list to compile all
        full_list.append(my_list)
        driver.close()
        driver.switch_to.window(window_before)
        
    except:
        #handle if there is an empty detail
        print("No detail")

sleep(2)
#check if items are being extracted
print(full_list)

#Write to CSV
with open("output.csv", "w") as f:
    writer = csv.writer(f, delimiter=" ", quotechar="-")
    for items in full_list:
        writer.writerows(items)