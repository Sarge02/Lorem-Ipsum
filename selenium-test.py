#import selenium libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#start selenium chrome driver
driver = webdriver.Chrome()

driver.get("http://localhost/Lorem-Ipsum-clean-up/Lorem-Ipsum-feature/register/registration.html")

title = driver.title

firstname = "Ryan"
lastname = "Sarginson"
email = "rsarginson@csus.edu"
password = "password"
phone = "4206969"
company = "onlybands"
website = "twitch.tv/steeps__"

fname_input = driver.find_element(By.NAME, 'FirstName')
fname_input.send_keys(firstname)
lname_input = driver.find_element(By.NAME, 'LastName')
lname_input.send_keys(lastname)
email_input = driver.find_element(By.NAME, 'Email')
email_input.send_keys(email)
password_input = driver.find_element(By.NAME, 'Password')
password_input.send_keys(password)
phone_input = driver.find_element(By.NAME, 'Phone')
phone_input.send_keys(phone)
company_input = driver.find_element(By.NAME, 'Company')
company_input.send_keys(company)
website_input = driver.find_element(By.NAME, 'Website')
website_input.send_keys(website)

#submit_button = driver.find_element(By.NAME, 'Submit')

import time
time.sleep(15)

#submit_button.click()


#driver.quit()