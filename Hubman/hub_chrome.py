import random
import time
import traceback
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from user_agents import UserAgents
from android_user_agents import UserAgentManager

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


siteLinkMain = "https://euginetech.com/"


def loop():
    try:
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
        browser = webdriver.Chrome(options=chrome_options)

        actions = ActionChains(browser)
        browser.set_window_size(random.randint(500, 2000), random.randint(400, 1080))
        # browser.get(LinkManager().get_link())
        browser.get(siteLinkMain)
        print("> Wait 5 seconds")
        time.sleep(1)
        print("> Done")
        print("> Start assigning values..")
        try:
            big_popup = WebDriverWait(browser, 2).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//*[@id=\"_gp4ecvq\"]/div/div/div[1]/div/div/div")
                                               ))

        except:
            big_popup = None
            print("No Big Popup Found")

        try:
            small_popup_ok = browser.find_element(By.XPATH, "/html/body/div/div/div")
        except:
            small_popup_ok = None
            print("No Small Popup Found")

        try:
            top_popup = browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]")
        except:
            top_popup = None
            print("Top Popup 1 not found")

        try:
            second_top_popup = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]")
        except:
            second_top_popup = None
            print("Second Top Popup not found")

        print("> Assigned values successfully")

        print("Current Page: " + browser.title)

        if big_popup is not None:
            print("> Big PopUp")
            try:
                actions.click(big_popup)
                actions.perform()
            except:
                print("Error clicking big popup")
                return
        elif small_popup_ok is not None:
            print("> Small PopUp OK")
            try:
                actions.click(small_popup_ok)
                actions.perform()
            except:
                print("Eooro clicking small popup")
        elif top_popup is not None:
            print("> Top PopUp")
            try:
                actions.click(top_popup)
                actions.perform()
            except:
                print("Error clicking top_popup")
                return

        elif second_top_popup is not None:
            print("> Second Top PopUp")
            try:
                actions.click(second_top_popup)
                actions.perform()
            except:
                print("Error clicking second top popup")
                return
        else:
            try:
                print("Going for popunder")
                x = str(random.randint(0, 450))
                y = str(random.randint(0, 450))
                browser.execute_script("window.scrollBy(" + x + ", " + y + ");")

                actions.move_by_offset(random.randint(0, 290), random.randint(0, 290))
                actions.click()
                actions.perform()
            except:
                print("Error on pop under")

        time.sleep(random.randint(25, 35))
        browser.quit()
        print("====End Session====")
        time.sleep(2)
        run_browser()
    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        browser.quit()
        time.sleep(2)
        run_browser()


run_browser()
