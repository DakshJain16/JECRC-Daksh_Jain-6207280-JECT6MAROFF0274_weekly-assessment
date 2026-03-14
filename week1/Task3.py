from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

'''
Write a Selenium script that opens multiple websites sequentially, including 
a few e-commerce sites [souled store, nike... any], a news website, and the official 
Python website. The script should wait for 3 seconds before opening and later should 
print the title of each page. finally close the browser.
'''
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.maximize_window()
print("Browser started")

# List of websites
sites = [
    "https://www.nike.in/",
    "https://www.shoppersstop.com/",
    "https://www.hindustantimes.com/",
    "https://www.python.org/"
]

for site in sites:
    sleep(3)
    driver.get(site)
    print("Page Title: ", driver.title)
    print()

sleep(3)
driver.quit()
