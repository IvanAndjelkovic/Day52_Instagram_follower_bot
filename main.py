import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

#loading dotenv
load_dotenv()

#fetching data from .env

similar_account=os.getenv("SIMILAR_ACCOUNT")
inst_username=os.getenv("USERNAME")
inst_pass=os.getenv("PASSWORD")

# xpaths copy
decline_optional_cookies_xpath='/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]'
user_name_xpath='//*[@id="loginForm"]/div[1]/div[1]/div/label/input'
pass_xpath='//*[@id="loginForm"]/div[1]/div[2]/div/label/input'
log_in_xpath='//*[@id="loginForm"]/div[1]/div[3]/button/div'


class InstaFollower:
    def __init__ (self):
     self.driver = webdriver.Chrome()

    
    def log_in(self):
       
       self.driver.get("https://www.instagram.com/")

       wait  = WebDriverWait(self.driver,5)
       decline_optional_cookies_button=wait.until(EC.element_to_be_clickable((By.XPATH ,decline_optional_cookies_xpath)))
       decline_optional_cookies_button.click()

       wait1 = WebDriverWait(self.driver,5)
       user_name_input_field=wait1.until(EC.element_to_be_clickable((By.XPATH ,user_name_xpath)))
        # user_name_input_field.clear()
       user_name_input_field.send_keys(Keys.CONTROL + "a")  # Select all
       user_name_input_field.send_keys(Keys.DELETE)
       user_name_input_field.send_keys(inst_username)

       wait2 =WebDriverWait(self.driver,2)
       password_input_field=wait2.until(EC.element_to_be_clickable((By.XPATH ,pass_xpath)))
       password_input_field.send_keys(inst_pass)

       wait3 =WebDriverWait(self.driver,2)
       log_in_button=wait2.until(EC.element_to_be_clickable((By.XPATH ,log_in_xpath)))
       log_in_button.click()

    def find_followers(self):
       pass

    def follow(self):
       pass

follow = InstaFollower()
follow.log_in()







time.sleep(220)

