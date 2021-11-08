import os
import time
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium import webdriver
load_dotenv()
option = webdriver.ChromeOptions()
option.add_argument('-incognito')

#print(os.getenv('password'))


class G_form:
    def __init__(self):
        path = os.path.join(os.getcwd(), 'chromedriver')
        self.bot = webdriver.Chrome(executable_path=path)

    def fill_up(self, name, email, adress, phone, comment):
        self.bot.get("https://forms.gle/vWVmojtWdfFvEj8V6")
        time.sleep(3)
        name_field = self.bot.find_element_by_class_name('quantumWizTextinputPaperinputInput')
        name_field.send_keys(name)
        #time.sleep(3)
        email_field = self.bot.find_element_by_class_name('quantumWizTextinputPaperinputInput')
        email_field.send_keys(email)
        #time.sleep(3)
        address_field=self.bot.find_element_by_class_name('quantumWizTextinputPapertextareaInput')
        address_field.send_keys(address)
        #time.sleep(3)
        phone_field=self.bot.find_element_by_class_name('quantumWizTextinputPaperinputInput')
        phone_field.send_keys(phone)
        #time.sleep(3)
        comment_field=self.bot.find_element_by_class_name('quantumWizTextinputPapertextareaInput')
        comment_field.send_keys(comment)
        time.sleep(3)
        #submit = self.bot.find_element_by_xpath()


def main():
    Google_form = G_form()
    Google_form.fill_up(os.getenv('name'), os.getenv('email'), os.getenv('adress'), os.getenv('phone'), os.getenv('comment'))


if __name__ == '__main__':
    main()

#env file
'''
name = Omar Faruk
email = omarfaruk4543@gmail.com
address = Earth
phone = 01723878787
comment = for automated testS

'''