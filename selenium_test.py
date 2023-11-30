#import selenium libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## GLOBALS TESTING VARIABLE DECLARATIONS

# login info
ADMIN_NAME = "123@gmail.com"
ADMIN_PW = "123"

COMPANY_NAME = "m@email"
COMPANY_PW = "12345"

CONTRACTOR_NAME = "piklings2255@gmail.com"
CONTRACTOR_PW = "123"

INVALID_NAME = "hacker@gmial.com"
INVALID_PW = "givemeyourinfo"

# job creation info
COMPANY_JOB_NAME = "JobCompany"
PRIMARY_CONTACT_NAME = "Megan Gross"
PRIMARY_CONTACT_PHONE = "9164205555"
PRIMARY_CONTACT_EMAIL = "jobCreationEmail@gmail.com"
JOB_TITLE = "helping us code"
JOB_DESCRIPTION = "We are very behind in our workload, get paid to help us!"
LOCATION = "Remote"
TOOLS_PROVIDED = "Not Provided"
TRANSPORT_PROVIDED = "Not Provided"
LANGUAGE = "English"
SALARY = "$50/Year"
APP_DEADLINE = "6132023"

# link info
HOME_PAGE_NAV = "//a[@href='../home']"
ABOUT_PAGE_NAV = "//a[@href='../about']"
LOGIN_PAGE_NAV = "//a[@href='../login']"
CONTACT_PAGE_NAV = "//a[@href='../contact']"

# virtual environment 
VIRTUAL_ENVIRONMENT_ADDRESS = "http://127.0.0.1:8000/"

WAIT_DURATION = 5

# Path encoding, 'extend' variable in login function
# 0: Login only
# 1: Admin credentials
# 2: Company credentials
# 3: Contractor credentials

## END GLOBAL VARIABLE DECLARATIONS

def wait():
    # universal wait function to observe steps being taken throughout scripts
    time.sleep(WAIT_DURATION)

def login(email, password, extend):
    # initialize chrome driver context and open url
    driver = webdriver.Chrome()
    driver.get(VIRTUAL_ENVIRONMENT_ADDRESS)
    title = driver.title
    actions = ActionChains(driver)

    email_input = driver.find_element(By.NAME, 'email')
    email_input.send_keys(email)

    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(password)

    login_button = driver.find_element(By.CLASS_NAME, "btnLogin")
    actions.move_to_element(login_button).perform()

    ## conditional statements chcecking for 'extend == 0' only to execute if showing login functionality 
    ## meant to skip if navigating to other pages
    if (extend == 0):
        wait()  
    
    login_button.click()

    if (extend == 0):
        wait()
    if (extend == 1 and email == ADMIN_NAME and password == ADMIN_PW):
        adminAssignJob(driver, actions)
    if (extend == 2 and email == COMPANY_NAME and password == COMPANY_PW):
        companyCreateJob(driver, actions)   
    if (extend == 3 and email == CONTRACTOR_NAME and password == CONTRACTOR_PW):
        wait()

def register(fname, lname, email, password, phone, company, website, contractorChoice):
    # initialize chrome driver context and open url
    driver = webdriver.Chrome()
    driver.get(VIRTUAL_ENVIRONMENT_ADDRESS + "register")
    title = driver.title
    actions = ActionChains(driver)

    fname_input = driver.find_element(By.NAME, 'FirstName')
    fname_input.send_keys(fname)

    lname_input = driver.find_element(By.NAME, 'LastName')
    lname_input.send_keys(lname)

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

    dropdown_element = driver.find_element(By.ID, "Registration_Type__c")
    dropdown = Select(dropdown_element)
    dropdown.select_by_index(contractorChoice)
    # index 1 = "Interested in contracting Titan Construction Partners"
    # index 2 = "Interested in becomoing a Titan Construction Partner"

    time.sleep(5)

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

def adminAssignJob(driver, actions):
    assign_button = driver.find_element(By.CLASS_NAME, "assignButton")
    assign_button.click()
    wait()
    
    dropdown_element = driver.find_element(By.CLASS_NAME, "contractorsDropdown")
    dropdown = Select(dropdown_element)
    # index should be within the range of [0, # of contractors available - 1]
    dropdown.select_by_index(1)
    wait()

    confirm_button = driver.find_element(By.CLASS_NAME, "confirmButton")
    confirm_button.click()

    wait(); wait()

def companyCreateJob(driver, actions):
    company_name = driver.find_element(By.NAME, "comp_name")
    company_name.send_keys(COMPANY_JOB_NAME)

    primary_name = driver.find_element(By.NAME, "primary_name")
    primary_name.send_keys(PRIMARY_CONTACT_NAME) 

    primary_phone = driver.find_element(By.NAME, "comp_phone")
    primary_phone.send_keys(PRIMARY_CONTACT_PHONE) 

    primary_email = driver.find_element(By.NAME, "comp_email")
    primary_email.send_keys(PRIMARY_CONTACT_EMAIL)

    job_title = driver.find_element(By.NAME, "job_title")
    job_title.send_keys(JOB_TITLE)

    job_desc = driver.find_element(By.NAME, "job_description")
    job_desc.send_keys(JOB_DESCRIPTION)

    job_location = driver.find_element(By.NAME, "location")
    job_location.send_keys(LOCATION)

    tools_provided = driver.find_element(By.NAME, "tools")
    tools_provided.send_keys(TOOLS_PROVIDED)

    transport_provided = driver.find_element(By.NAME, "transport")
    transport_provided.send_keys(TRANSPORT_PROVIDED)

    language_requirements = driver.find_element(By.NAME, "language")
    language_requirements.send_keys(LANGUAGE)

    job_salary = driver.find_element(By.NAME, "salary")
    job_salary.send_keys(SALARY)

    application_deadline = driver.find_element(By.NAME, "application_deadline")
    application_deadline.send_keys(APP_DEADLINE)

    wait()

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

def dashboardClicks(navigateTo):
    # initialize chrome driver context and open url
    driver = webdriver.Chrome()
    driver.get(VIRTUAL_ENVIRONMENT_ADDRESS + "home")
    title = driver.title

    try:
        # Use WebDriverWait to wait until the element is clickable
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, navigateTo))
        )
        element.click()
    finally:
        wait()
        # Close the browser window
        driver.quit()

def contactSubmission(fname, lname, email, subject):
    # initialize chrome driver context and open url
    driver = webdriver.Chrome()
    driver.get(VIRTUAL_ENVIRONMENT_ADDRESS + "contact")
    title = driver.title
    actions = ActionChains(driver)

    first_name = driver.find_element(By.NAME, "firstname")
    first_name.send_keys(fname)

    last_name = driver.find_element(By.NAME, "lastname")
    last_name.send_keys(lname)

    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys(email)

    subject_field = driver.find_element(By.NAME, "subject")
    subject_field.send_keys(subject)

    wait()

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    wait()


## BEGIN TESTING ##

## BEGIN LOGIN TESTS ## 
# login(ADMIN_NAME, ADMIN_PW, 1) # admin login attempt
# login(COMPANY_NAME, COMPANY_PW, 2) # login attempt with valid company credentials
# login(CONTRACTOR_NAME, CONTRACTOR_PW, 3) # login attempt with valid contractor credentials
# login(COMPANY_NAME, "nicetry", 0) # login attempt with incorrect password
# login(INVALID_NAME, INVALID_PW, 0) # login attempt with invalid credentials
## END LOGIN ATTEMPTS ##


## BEGIN JOB POSTING TESTS ##
# login(ADMIN_NAME, ADMIN_PW, 1) # admin job assignment
# login(COMPANY_NAME, COMPANY_PW, 2) # company job posting
## END JOB POSTING TESTS ##

## BEGIN DASHBOARD NAVIGATION TESTS ##
# dashboardClicks(ABOUT_PAGE_NAV) # navigate to about page
# dashboardClicks(HOME_PAGE_NAV) # navigate to home page
# dashboardClicks(CONTACT_PAGE_NAV) # navigate to contact page
# dashboardClicks(LOGIN_PAGE_NAV) # navigate to login page
## END DASHBOARD NAVIGATION TESTS ##

## BEGIN REGISTRATION TESTS ##
# register("registerTestFname", "registerTestLname", "registerTestEmail@gmail.com", "registerTestPassword",
            # 9165550147, "registerTestCompany", "registerTestWebsite.com", 1)
            # registration attempt for new contractor
# register("testCompany", "One", "testCompany@gmail.com", "pw123", "9165550147", "testCompany", "testCompany.com", 2)
            # registration attempt for new contractor
## END REGISTRATION TESTS ##

## CONTACT FORM SUBMISSION TEST ##
# contactSubmission("Ryan", "Sarginson", "email@gmail.com", "How did you guys make this site so well?!")
## END CONTACT FORM SUBMISSION TEST ##