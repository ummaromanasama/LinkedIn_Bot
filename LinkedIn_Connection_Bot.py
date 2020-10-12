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
names = ['Insert name']

#Lookup names, add a note, and send connection request
for name in names:

    #Lookup name
    browser.find_element_by_xpath("//input[@type = 'text']").send_keys(name)
    sleep(1.5)
    browser.find_element_by_xpath("//input[@type = 'text']").send_keys(Keys.RETURN)
    sleep(1.5)
    
    #Add a Note
    browser.find_element_by_xpath("//button[text() = 'Connect']").click()
    sleep(1.5)
    browser.find_element_by_xpath("//span[text()='Add a note']").click()
    sleep(1.5)

    message = "Hi " + name.strip().split(' ')[0] + ",\n\nHope all is well!\n\nBest regards,\nUmmaromana Sama"

    browser.find_element_by_xpath("//textarea").send_keys(message)
    sleep(1.5)

    browser.find_element_by_xpath("//span[text()='Done']").click()
    sleep(1.5)

    browser.find_element_by_xpath("//input[@type = 'text']").clear()
    sleep(1.5)

   