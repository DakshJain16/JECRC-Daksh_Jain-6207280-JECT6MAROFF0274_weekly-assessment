from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# Open Google
driver.get('https://www.google.com/')
driver.maximize_window()

# Enter "Selenium Python"
search1=driver.find_element(By.ID,'APjFqb')
search1.send_keys('Selenium Python')

# Use explicit wait for suggestions
# Capture all suggestions using find_elements
wait = WebDriverWait(driver, 10)
suggestion=wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//ul[@role="listbox"]/child::li')))

# Print them
for item in suggestion:
    print(item.text)

# Click one suggestion
click_item=wait.until(EC.element_to_be_clickable((By.XPATH,'//ul[@role="listbox"]/child::li[3]')))
click_item.click()

