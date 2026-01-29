import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

#loading dotenv
load_dotenv()

#fetching data from .env

SIMILAR_ACCOUNT=os.getenv("SIMILAR_ACCOUNT")
inst_username=os.getenv("USERNAME")
inst_pass=os.getenv("PASSWORD")

# xpaths copy
decline_optional_cookies_xpath='/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]'
user_name_xpath='//*[@id="loginForm"]/div[1]/div[1]/div/label/input'
pass_xpath='//*[@id="loginForm"]/div[1]/div[2]/div/label/input'
log_in_xpath='//*[@id="loginForm"]/div[1]/div[3]/button/div'
save_info_path='//*[@id="mount_0_0_ZI"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div' #Button with the name Not now



class InstaFollower:
    def __init__ (self):
     self.driver = webdriver.Chrome()

    
    def log_in(self):
       
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4.2)

        # Check if the cookie warning is present on the page
        decline_cookies_xpath = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Allow all cookies')]")

        cookie_warning = self.driver.find_elements(By.XPATH, decline_optional_cookies_xpath)
    
        if cookie_warning:
            # Dismiss the cookie warning by clicking an element or button
            cookie_warning.click()

        time.sleep(120)

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")


        username.send_keys(inst_username)
        password.send_keys(inst_pass)

        time.sleep(2.1)
        password.send_keys(Keys.ENTER)

        time.sleep(4.3)
        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()
        else:
            print("not found Log in prompt")
            print(save_login_prompt)

        time.sleep(3.7)
        # Click "not now" on notifications prompt
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()


    #    wait3 =WebDriverWait(self.driver,5)
    #    log_in_button=wait3.until(EC.element_to_be_clickable((By.XPATH ,log_in_xpath)))
    #    log_in_button.click()

    #    wait4 =WebDriverWait(self.driver,2)
    #    log_in_button=wait4.until(EC.element_to_be_clickable((By.XPATH ,save_info_path)))
    #    log_in_button.click()


       
    #    try:
    #         # not_now_btn = wait.until(
    #         #     EC.element_to_be_clickable((
    #         #         By.XPATH,
    #         #         "//button[contains(., 'Not now') or contains(., \"Nicht jetzt\")]"
    #         #     ))
    #         # )
    #         # not_now_btn.click()
    #         wait  = WebDriverWait(self.driver,7)
    #         not_now_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not now')]")))
    #         not_now_btn.click()
    #    except Exception:
            
    #         # Dialog may not appear; ignore if not found
    #         pass



    def find_followers(self):
        time.sleep(5)
        # Show followers of the selected account. 
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(5.2)
        # The xpath of the modal that shows the followers will change over time. Update yours accordingly.
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
       # Check and update the (CSS) Selector for the "Follow" buttons as required. 
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

follow = InstaFollower()
follow.log_in()







time.sleep(1220)

