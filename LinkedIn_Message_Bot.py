#Import modules
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#Open LinkedIn in Chrome browser
browser = webdriver.Chrome('/Users/ummaromanasama/Desktop/chromedriver85')
browser.get('https://www.linkedin.com')

#Log into LinkedIn
browser.find_element_by_link_text('Sign in').click()
sleep(1.5)
browser.find_element_by_id('username').send_keys('Email')
sleep(1.5)
browser.find_element_by_id('password').send_keys('Password')
sleep(1.5)
browser.find_element_by_xpath("//button[@type = 'submit']").click()
sleep(1.5)

#Search for people
names = ['Insert names']
ctr = 0

#Customize message
message = 'Insert message'

#Lookup names and send messages
for name in names:

    browser.find_element_by_xpath("//input[@type = 'text']").send_keys(name)
    sleep(1.5)
    browser.find_element_by_xpath("//input[@type = 'text']").send_keys(Keys.RETURN)
    sleep(1.5)

    browser.find_element_by_xpath("//button[text() = 'Message']").click()
    sleep(1)

    if ctr == 0:
        browser.find_element_by_xpath("//div[@role = 'textbox']").send_keys(message)
    else:
        browser.find_elements_by_xpath("//div[@role = 'textbox']")[ctr].send_keys(message)
    sleep(1.5)

    if ctr == 0:
        browser.find_element_by_xpath("//button[@type = 'submit']").click()
    else:
        browser.find_elements_by_xpath("//button[@type = 'submit']")[ctr].click()

    ctr += 1

    sleep(1)

    browser.find_element_by_xpath("//input[@type = 'text']").clear()
