from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# 1. Go to https://the-internet.herokuapp.com/login.
driver.get('https://the-internet.herokuapp.com/login')
driver.maximize_window()
sleep(1)

# 2. Locate the username field using CSS Selector with Tag and name attribute.
username = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
print('working')

# 3. Locate the password field using CSS Selector with Tag and id attribute.
password = driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
print('working')

# 4.Locate the "Login" button using CSS Selector with Tag and type attribute.
login = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
print('working')

# 5. Locate the footer link ("Elemental Selenium") using CSS Selector(descendant).
footer = driver.find_element(By.CSS_SELECTOR, 'div[style="text-align: center;"] a')
print('working')

driver.quit()