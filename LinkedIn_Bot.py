#Import modules
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#Open LinkedIn website in Chrome
browser = webdriver.Chrome('/Users/ummaromanasama/Desktop/chromedriver85')
browser.get('https://www.linkedin.com')

#Log into LinkedIn
def logIn():
    sleep(1)
    browser.find_element_by_link_text('Sign in').click()
    sleep(2)
    browser.find_element_by_id('username').send_keys('Email')
    sleep(1)
    browser.find_element_by_id('password').send_keys('Password')
    sleep(1)
    browser.find_element_by_xpath("//button[@type = 'submit']").click()
    sleep(1.5)

logIn()

# #-------------------------------------Send Multiple People Messages-----------------------------------------------------
# #Search for people
# names = ['Rakib Rary', 'Jorge Gallardo', 'Ruby Reilly']
# ctr = 0

# for name in names:

#     browser.find_element_by_xpath("//input[@type = 'text']").send_keys(name)
#     browser.find_element_by_xpath("//input[@type = 'text']").send_keys(Keys.RETURN)
#     sleep(2)

#     #Send message
#     browser.find_element_by_xpath("//button[text() = 'Message']").click()
#     message = 'I updated the chromedriver and now my code works -via LinkedIn Bot'
#     sleep(1)

#     if ctr == 0:
#         browser.find_element_by_xpath("//div[@role = 'textbox']").send_keys(message)
#     else:
#         browser.find_elements_by_xpath("//div[@role = 'textbox']")[ctr].send_keys(message)
#     sleep(1.5)

#     if ctr == 0:
#         browser.find_element_by_xpath("//button[@type = 'submit']").click()
#     else:
#         browser.find_elements_by_xpath("//button[@type = 'submit']")[ctr].click()

#     ctr += 1

#     sleep(1)

#     browser.find_element_by_xpath("//input[@type = 'text']").clear()

#---------------------------Connect & Add a note--------------------------------------------------
#Search for people
names = ['Joanna Mira-Villa', 'Jorge Gallardo']
 
#Need to send message with just first name
firstName = []
for i in range(0,len(names)):
    firstName.append(names[i].split()[0])
sleep(1.5)

for name in names:

    #Lookup name
    browser.find_element_by_xpath("//input[@type = 'text']").send_keys(name)
    browser.find_element_by_xpath("//input[@type = 'text']").send_keys(Keys.RETURN)
    sleep(2)
    
    #Add a Note
    browser.find_element_by_xpath("//button[text() = 'Connect']").click()
    browser.find_element_by_xpath("//span[text()='Add a note']").click()
    sleep(1.5)

    message = "Hi " + name.strip().split(' ')[0] + ",\n\nI'm testing out my LinkedIn Bot!\n\nBest regards,\nUmmaromana Sama"

    browser.find_element_by_xpath("//textarea").send_keys(message)

    browser.find_element_by_xpath("//span[text()='Done']").click()

    browser.find_element_by_xpath("//input[@type = 'text']").clear()

   