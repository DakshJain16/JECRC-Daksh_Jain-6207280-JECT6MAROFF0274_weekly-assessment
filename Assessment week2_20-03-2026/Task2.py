from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# Open signup page `https://automationexercise.com/signup`
driver.get('https://automationexercise.com/signup')
driver.maximize_window()

# Enter name & email
wait = WebDriverWait(driver, 6)
home = wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Home")]')))
home.click()

signup = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Signup")]')))
signup.click()

name = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="name"]')))
name.send_keys("Harsh Rao")

email = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@data-qa="signup-email"]')))
email.send_keys("harsh123rao@gmail.com")

signup_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-qa="signup-button"]')))
signup_button.click()

# Select Title (Mr/Mrs) → Radio button
gender = driver.find_element(By.ID,'id_gender2')
gender.click()
sleep(2)

# Select checkboxes: `Newsletter`, `Special offers`
news = driver.find_element(By.ID,'newsletter')
news.click()
sleep(2)

offer = driver.find_element(By.ID,'optin')
offer.click()
sleep(2)

# Use get_attribute("checked") to verify selection
print(f'Newsletter checked:',news.get_attribute('checked'))
print(f'Offer checked:',offer.get_attribute('checked'))
