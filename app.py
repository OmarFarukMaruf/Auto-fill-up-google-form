'''
Name: Omar Faruk
Batch: 213-1
Class 23
'''


from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
load_dotenv()
import time


option = webdriver.ChromeOptions()
option.add_argument('-incognito')


path = os.path.join(os.getcwd(), 'chromedriver')
bot = webdriver.Chrome(executable_path=path)
bot.get('https://forms.gle/vWVmojtWdfFvEj8V6')
time.sleep(3)
name_field = bot.find_element_by_class_name('quantumWizTextinputPaperinputInput')
name_field.send_keys(os.getenv('name'))
# print(os.getenv('name'))
email_field = bot.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
email_field.send_keys(os.getenv('email'))
address_field = bot.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
address_field.send_keys(os.getenv('address'))
phone_field = bot.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
phone_field.send_keys(os.getenv('phone'))
comment_field = bot.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea')
comment_field.send_keys(os.getenv('comment'))
submition = bot.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
submition.click()

#env file
'''
name = Omar Faruk
email = omarfaruk@gmail.com
address = Earth
phone = 01723******
comment = for automated test
'''
