import random
import time
import traceback
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from eurofutbol.link_rand import Rand
from eurofutbol.link_router import Router
from user_agents import UserAgents
from android_user_agents import UserAgentManager

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from selenium import webdriver

from eurofutbol.links import LinkManager


def loop():
    try:
        while True:
            run_browser()
    except:
        loop()


def click_ad(m_browser):
    ad_random = random.randint(1, 100)
    """Using CTR 6%"""
    ctr = 8
    if ad_random <= ctr:
        actions = ActionChains(m_browser)
        actions.move_by_offset(10, 20)
        actions.click()
        actions.perform()
        print("Ad Clicked")
    else:
        print("Not to click this round")
        wait = random.randint(25, 60)
        print("waiting: " + str(wait))
        time.sleep(wait)
        m_browser.quit()
        print("====End Session====")
        time.sleep(random.randint(2, 5))

    print("Session Ended")


def visit_site_direct():
    print("Direct Visit")
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
        browser.set_window_size(random.randint(900, 2000), random.randint(900, 1080))
        browser.get(LinkManager().get_link())
        print("waiting 5s")
        time.sleep(5)

        """Interaction with site"""
        print("Interaction..")
        """Scrolling to bottom using pg down, then back to top"""
        try:
            """Slowly scroll to bottom
            time between 30s and 3m"""
            page_finished = False
            while not page_finished:
                if not browser.execute_script(
                        "return (window.innerHeight + window.scrollY) >= document.body.scrollHeight - 1000;"):
                    print("Still Scrolling")

                    ActionChains(browser).send_keys(Keys.PAGE_DOWN).perform()
                    sleep_time = random.randint(5, 10)
                    print("Waiting " + str(sleep_time) + " Seconds after page down")
                    time.sleep(sleep_time)
                else:
                    page_finished = True
                    print("Scrolled To Bottom")
            """Scroll Back to top"""
            ActionChains(browser).send_keys(Keys.HOME).perform()
            click_ad(browser)
        except Exception as e:
            print("Error occurred. Retrying")
            traceback.print_exc()
            browser.quit()

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        browser.quit()


def visit_site_with_google():
    print("Doing Google Search")
    print("Direct Visit --- Other site")
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
        browser.set_window_size(random.randint(900, 2000), random.randint(900, 1080))

        search_url = Router().get_search_link()
        browser.get(search_url)

        print("waiting 5s")
        time.sleep(5)

        """Interaction with other site"""
        print("Interaction..")
        """Scrolling to bottom using pg down, then back to top"""
        try:
            """Slowly scroll to bottom
            time between 30s and 3m"""
            page_finished = False
            while not page_finished:
                if not browser.execute_script(
                        "return (window.innerHeight + window.scrollY) >= document.body.scrollHeight - 1000;"):
                    print("Still Scrolling")

                    ActionChains(browser).send_keys(Keys.PAGE_DOWN).perform()
                    sleep_time = random.randint(5, 10)
                    print("Waiting " + str(sleep_time) + " Seconds after page down")
                    time.sleep(sleep_time)
                else:
                    page_finished = True
                    print("Scrolled To Bottom")
            """Page Up"""
            ActionChains(browser).send_keys(Keys.PAGE_UP).perform()
            ActionChains(browser).send_keys(Keys.PAGE_UP).perform()
            visit_other_site_direct()

        except Exception as e:
            print("Error occurred. Retrying")
            traceback.print_exc()
            browser.quit()

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        browser.quit()


def visit_other_site_direct():
    print("Direct Visit --- Other site")
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
        browser.set_window_size(random.randint(900, 2000), random.randint(900, 1080))

        browser.get(Rand().get_other_site_link())

        print("waiting 5s")
        time.sleep(5)

        """Interaction with other site"""
        print("Interaction..")
        """Scrolling to bottom using pg down, then back to top"""
        try:
            """Slowly scroll to bottom
            time between 30s and 3m"""
            page_finished = False
            while not page_finished:
                if not browser.execute_script(
                        "return (window.innerHeight + window.scrollY) >= document.body.scrollHeight - 1000;"):
                    print("Still Scrolling")

                    ActionChains(browser).send_keys(Keys.PAGE_DOWN).perform()
                    sleep_time = random.randint(5, 10)
                    print("Waiting " + str(sleep_time) + " Seconds after page down")
                    time.sleep(sleep_time)
                else:
                    page_finished = True
                    print("Scrolled To Bottom")
            """Page Up"""
            ActionChains(browser).send_keys(Keys.PAGE_UP).perform()
            ActionChains(browser).send_keys(Keys.PAGE_UP).perform()
            visit_site_direct()

        except Exception as e:
            print("Error occurred. Retrying")
            traceback.print_exc()
            browser.quit()

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        browser.quit()


def run_browser():
    try:
        # choice to visit other site
        random_num = random.randint(1, 5)
        if random_num <= 4:
            """now visit other site"""
            print("Visiting other site")
            google_random = random.randint(1, 4)
            if google_random <= 4:
                visit_site_with_google()
            else:
                visit_other_site_direct()

        else:
            """go direct to target"""
            visit_site_direct()

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        browser.quit()


loop()
