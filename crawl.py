from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import utils

def init():
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications");
    driver = webdriver.Chrome('driver/chromedriver', chrome_options=chrome_options)

def login_cred(email = "", password = ""):
    LOGIN_URL = "https://uwealthmktg.com/members/login"
    EMAIL_XPATH = '//*[@id="scroll-to"]/div/div/table/tbody/tr/td[2]/div/form/div[1]/div[2]/input'
    PASS_XPATH = '//*[@id="scroll-to"]/div/div/table/tbody/tr/td[2]/div/form/div[2]/div[2]/input'
    BTN_XPATH = '//*[@id="scroll-to"]/div/div/table/tbody/tr/td[2]/div/form/div[3]/div/div/button'

    driver.get(LOGIN_URL)

    driver.find_element(By.XPATH, EMAIL_XPATH).send_keys(email)
    driver.find_element(By.XPATH, PASS_XPATH).send_keys(password)
    driver.find_element(By.XPATH, BTN_XPATH).click()

    print("Current URL: " ,driver.current_url)

def go_to_captcha():
    CAPTCHA_URL = "https://uwealthmktg.com/members/captcha"
    CAPTCHA_BTN_XPATH = '//*[@id="scroll-to"]/div/div[1]/div/div[3]/div/div/form/div[2]/button'

    driver.get(CAPTCHA_URL)

    driver.find_element(By.XPATH, CAPTCHA_BTN_XPATH).click()

    print("Current URL: ", driver.current_url)

def crawl_captcha(list_of_captcha):

    def close_windows():
        tabs = driver.window_handles
        for tab in tabs:
            if tabs[0] != tab:
                driver.switch_to_window(tab)
                driver.close()
        driver.switch_to_window(tabs[0])
        driver.switch_to.default_content()

    CAPTCHA_IMG_XPATH = '/html/body/div/div/div[4]/form/div[1]/div[1]/img'
    CAPTCHA_INPUT_XPATH = '//*[@id="captcha_answer"]'
    CAPTCHA_SUBMIT = '/html/body/div/div/div[4]/form/div[2]/div/button'
    CAPTCHA_ANOTHER = '/html/body/div/div/div[2]/button'
    try:
        img = driver.find_element(By.XPATH, CAPTCHA_IMG_XPATH).get_attribute("src")
        f = img.split('/')[-1].split('.')[0]

        driver.find_element(By.XPATH, CAPTCHA_INPUT_XPATH).clear()
        driver.find_element(By.XPATH, CAPTCHA_INPUT_XPATH).send_keys(list_of_captcha[int(f)])
        driver.find_element(By.XPATH, CAPTCHA_SUBMIT).click()


    except Exception as e:
        driver.find_element(By.XPATH, CAPTCHA_ANOTHER).click()

    close_windows()
