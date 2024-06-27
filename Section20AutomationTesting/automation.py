from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_service = Service(executable_path='chromedriver.exe')
chrome_browser = webdriver.Chrome(options = options, service=chrome_service)

chrome_browser.maximize_window()
chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')

assert "Show Message" in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, "user-message")
user_message.clear()
user_message.send_keys("I AM EXTRA COOOOOL")

show_message_button.click()

output_message = chrome_browser.find_element(By.ID, "display")

assert "I AM EXTRA COOOOOL" in output_message.text

chrome_browser.quit()
