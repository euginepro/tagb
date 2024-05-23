import random
import time
import traceback
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.options import Options

from user_agents import UserAgents
from android_user_agents import UserAgentManager

from selenium.webdriver import ActionChains
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
        browser = webdriver.ChromiumEdge(service=EdgeService(EdgeChromiumDriverManager().install()),
                                         options=chrome_options)

        actions = ActionChains(browser)
        browser.set_window_size(random.randint(900, 2000), random.randint(900, 1080))
        browser.get(LinkManager().get_link())

        print("> Wait 5 seconds")
        time.sleep(5)
        print("> Done")

        print("Current Page: " + browser.title)

        print("Going for popunder")
        x = str(random.randint(0, 450))
        y = str(random.randint(0, 450))
        browser.execute_script("window.scrollBy(" + x + ", " + y + ");")

        actions.move_by_offset(random.randint(0, 400), random.randint(0, 290))
        actions.click()
        actions.perform()

        time.sleep(random.randint(25, 240))
        browser.quit()
        print("====End Session====")
        time.sleep(random.randint(2, 10))

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        browser.quit()


loop()
