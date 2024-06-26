import random
import time
import traceback
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from utils.user_agents import UserAgents
from utils.android_user_agents import UserAgentManager

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from selenium import webdriver
from links import LinkManager

siteLinkMain = "https://euginetech.com/"


def loop():
    try:
        while True:
            run_browser()
    except:
        loop()


def run_browser():
    global custom_ua, browser
    try:

        print("=====session start=====")
        numb = random.choice([0, 1])
        print("Selected Choice: " + str(numb))
        if numb == 0:
            custom_ua = UserAgentManager().get_phone_user_agent()
            print("Using Android Mobile: " + custom_ua)
        else:
            custom_ua = UserAgents().get_user_agent()
            print("Using PC / iOS: " + custom_ua)

        chrome_options = Options()
        chrome_options.add_argument(f"user-agent={custom_ua}")
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

        actions = ActionChains(browser)
        browser.set_window_size(random.randint(900, 2000), random.randint(900, 1080))
        browser.get(LinkManager().get_link())

        print("> Wait 5 seconds")
        time.sleep(5)
        print("> Done")

        print("Current Page: " + browser.title)

        body = browser.find_element(By.TAG_NAME, "body")
        bottom_reached = False
        while not bottom_reached:
            if not browser.execute_script("return (window.innerHeight + window.scrollY) >= document.body.scrollHeight"):
                body.send_keys(Keys.PAGE_DOWN)
                time.sleep(random.randint(4, 7))
            else:
                body.send_keys(Keys.HOME)
                bottom_reached = True

        print("Going for click")
        '''x = str(random.randint(0, 450))
        y = str(random.randint(0, 450))
        browser.execute_script("window.scrollBy(" + x + ", " + y + ");")'''

        actions.move_by_offset(random.randint(5, 20), random.randint(3, 20))
        actions.click()
        actions.perform()

        time.sleep(random.randint(25, 120))
        browser.quit()
        print("====End Session====")
        time.sleep(random.randint(2, 10))

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        browser.quit()


loop()
