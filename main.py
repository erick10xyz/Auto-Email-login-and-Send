import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Email
email_username = "your email"
email_password = "your email password"
send_to = "recipient email"
subject = "Urgent"
body_content = "Create your own letter"

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("email provider")
time.sleep(5)
email = driver.find_element(By.NAME, "username")
email.send_keys(email_username)
email.send_keys(Keys.RETURN)

time.sleep(5)
password = driver.find_element(By.NAME, "password")
password.send_keys(email_password)
password.send_keys(Keys.ENTER)

time.sleep(5)
mail_button = driver.find_element(By.ID, "get corresponding ID in your email provider")
mail_button.click()

time.sleep(5)
compose_button = driver.find_element(By.XPATH, "get corresponding xpath in your email provider")
compose_button.click()

time.sleep(5)
email_add = driver.find_element(By.XPATH, "get corresponding xpath in your email provider")
email_add.send_keys(send_to)

time.sleep(5)
email_subject = driver.find_element(By.XPATH, "get corresponding xpath in your email provider")
email_subject.send_keys(subject)

time.sleep(5)
content = driver.find_element(By.XPATH, "get corresponding xpath in your email provider")
content.send_keys(body_content)

time.sleep(5)
send_button = driver.find_element(By.XPATH, "get corresponding xpath in your email provider")
send_button.click()

time.sleep(5)
exit_email_button = driver.find_element(By.XPATH, "get corresponding xpath in your email provider")
exit_email_button.click()

time.sleep(5)
sign_out_button = driver.find_element(By.XPATH, "get corresponding xpath in your email provider")
sign_out_button.click()

driver.quit()