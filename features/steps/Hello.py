from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/")
print(driver.title)

search_bar = driver.find_element(By.NAME, "q")
search_bar.clear()
search_bar.send_keys("python")
search_bar.send_keys(Keys.ENTER)

print(driver.current_url)
