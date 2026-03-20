from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# Open Amazon
driver.get('https://www.amazon.in/')
driver.maximize_window()

print(driver.title)
# Verify page title and current URL
assert 'Amazon' in driver.title, 'Incorrect Title!'
print('Title Verified!')

assert 'amazon' in driver.current_url, 'Incorrect URL!'
print('URL Verified!')

# Locate the category dropdown (next to search bar)
wait = WebDriverWait(driver, 10)
cat = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@id="searchDropdownBox"]')))

# Select "Books" using Select class
select = Select(cat)
select.select_by_visible_text('Books')

# Enter "Harry Potter" in search and press Enter
# Use explicit wait to wait until results are visible
search = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="twotabsearchtextbox"]')))
search.send_keys('Harry Potter', Keys.ENTER)

# Get all product titles using find_elements
titles = driver.find_elements(By.XPATH, '//div[@class="a-section a-spacing-small a-spacing-top-small"]/div/a/h2/span')

# Print first 5 product names
count = 0
for title in titles:
    if count < 5:
        print(title.text)
        count += 1

# Click on the first product
first_prod = wait.until(EC.element_to_be_clickable((By.XPATH, '(//div[@class="a-section a-spacing-small a-spacing-top-small"]/div/a/h2/span)[1]')))
first_prod.click()
