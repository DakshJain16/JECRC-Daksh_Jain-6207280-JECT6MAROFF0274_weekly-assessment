# 1. Write a Python script using Selenium.
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# 2. Navigate to https://www.wikipedia.org/
driver.get('https://www.wikipedia.org/')
driver.maximize_window()
sleep(1)

# 3. Find the search input field.
search = driver.find_element(By.XPATH, '//input[@id="searchInput"]')
print('Search input field found')

# 4. Find the "English" language.
eng = driver.find_element(By.XPATH, '//a[text()="English"]')
print('English language link found')

# 5. Find the main Wikipedia logo image.
logo = driver.find_element(By.CSS_SELECTOR, "div.central-textlogo img")
print("Wikipedia logo found")

# 6. Count language links in central block
languages = driver.find_elements(By.CSS_SELECTOR, 'div.central-featured-lang a')
print(f'Number of language links: {len(languages)}')

# 7. Navigate back to the previous page
driver.back()
print("Navigated back")
sleep(2)

# 8. Navigate forward
driver.forward()
print("Navigated forward")
sleep(2)

# 9. Refresh the page
driver.refresh()
print('Page Refreshed')
sleep(2)

# 10. Print the final page title
print("Final Page Title:", driver.title)

# 11. Quit the browser
driver.quit()