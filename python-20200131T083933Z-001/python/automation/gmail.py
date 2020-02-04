from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import selenium
import time

browser = webdriver.Chrome(executable_path="/home/faiz/faiz/python/automation/chromedriver_linux64/chromedriver")
browser.get("https://mail.google.com/mail")


email = browser.find_element_by_id('identifierId').send_keys('faiz.hb@terralogic.com')
# time.sleep(1)
email_next = browser.find_element_by_id('identifierNext').click()

time.sleep(1)
password = browser.find_element_by_name('password').send_keys('sakirraja')
psw_next = browser.find_element_by_id('passwordNext').click()
# email.send_keys('123')
print("faiz");
