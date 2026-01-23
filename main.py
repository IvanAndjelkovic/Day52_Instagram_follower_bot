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
save_info_path='//*[@id="mount_0_0_ZI"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div' #Button with the name Not now



class InstaFollower:
    def __init__ (self):
     self.driver = webdriver.Chrome()

    
    def log_in(self):
       
       self.driver.get("https://www.instagram.com/")

    #    wait  = WebDriverWait(self.driver,5)
    #    decline_optional_cookies_button=wait.until(EC.element_to_be_clickable((By.XPATH ,decline_optional_cookies_xpath)))
    #    decline_optional_cookies_button.click()


       try:
          wait  = WebDriverWait(self.driver,5)
          decline_optional_cookies_button=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Decline optional')]")))
          decline_optional_cookies_button.click()

       except:
          pass

       wait1 = WebDriverWait(self.driver,5)
       user_name_input_field=wait1.until(EC.element_to_be_clickable((By.XPATH ,user_name_xpath)))
        # user_name_input_field.clear()
       user_name_input_field.send_keys(Keys.CONTROL + "a")  # Select all
       user_name_input_field.send_keys(Keys.DELETE)
       user_name_input_field.send_keys(inst_username)

       wait2 =WebDriverWait(self.driver,2)
       password_input_field=wait2.until(EC.element_to_be_clickable((By.XPATH ,pass_xpath)))
       password_input_field.send_keys(inst_pass)

       wait3 =WebDriverWait(self.driver,5)
       log_in_button=wait3.until(EC.element_to_be_clickable((By.XPATH ,log_in_xpath)))
       log_in_button.click()

    #    wait4 =WebDriverWait(self.driver,2)
    #    log_in_button=wait4.until(EC.element_to_be_clickable((By.XPATH ,save_info_path)))
    #    log_in_button.click()


       
       try:
            # not_now_btn = wait.until(
            #     EC.element_to_be_clickable((
            #         By.XPATH,
            #         "//button[contains(., 'Not now') or contains(., \"Nicht jetzt\")]"
            #     ))
            # )
            # not_now_btn.click()
            wait  = WebDriverWait(self.driver,7)
            not_now_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not now')]")))
            not_now_btn.click()
       except Exception:
            
            # Dialog may not appear; ignore if not found
            pass



    def find_followers(self):
       pass

    def follow(self):
       pass

follow = InstaFollower()
follow.log_in()







time.sleep(1220)

