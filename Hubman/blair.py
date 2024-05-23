import random
import time
import traceback
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from eurofutbol.proxies import ProxyManager
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
    """Using CTR 8%"""
    ctr = 15
    if ad_random <= ctr:
        actions = ActionChains(m_browser)
        a = random.randint(10, 15)
        b = random.randint(15, 25)
        actions.move_by_offset(a, b)
        actions.click()
        actions.perform()
        print("Ad Clicked")
        print("\nwaiting page load before scroll\n")
        time.sleep(random.randint(10, 15))
        actions.send_keys(Keys.PAGE_DOWN).perform()
        print("scrolled\n")
        time.sleep(random.randint(1, 6))
        actions.send_keys(Keys.PAGE_DOWN).perform()
        wait = random.randint(15, 45)
        print("waiting: " + str(wait))
        time.sleep(wait)
        m_browser.quit()
        print("====End Session====")
        time.sleep(random.randint(2, 5))
    else:
        print("Not to click this round")
        wait = random.randint(25, 60)
        print("waiting: " + str(wait))
        time.sleep(wait)
        m_browser.quit()
        print("====End Session====")
        time.sleep(random.randint(2, 5))

    print("Session Ended")


def visit_site_direct(d_browser):
    print("Direct Visit")
    try:
        print("=====session start ..direct visit=====")

        d_browser.get(LinkManager().get_link())
        print("waiting 5s")
        time.sleep(5)
        try:
            cookie_ok = d_browser.find_element(By.XPATH, "//*[@id=\"cookieChoiceDismiss\"]")
            if cookie_ok is not None:
                cookie_ok.click()
                print("Cookie dismissed!")
        except Exception as e:
            print("Error getting cookie button")

        time.sleep(1)

        """Interaction with site"""
        print("Interaction..")
        """Scrolling to bottom using pg down, then back to top"""
        try:
            """Slowly scroll to bottom
            time between 30s and 3m"""
            page_finished = False
            while not page_finished:
                if not d_browser.execute_script(
                        "return (window.innerHeight + window.scrollY) >= document.body.scrollHeight - 1000;"):
                    print("Still Scrolling")

                    ActionChains(d_browser).send_keys(Keys.PAGE_DOWN).perform()
                    sleep_time = random.randint(5, 30)
                    print("Waiting " + str(sleep_time) + " Seconds after page down")
                    time.sleep(sleep_time)
                else:
                    page_finished = True
                    print("Scrolled To Bottom")
            """Scroll Back to top"""
            ActionChains(d_browser).send_keys(Keys.HOME).perform()
            print("waiting 2 to 8 seconds")
            time.sleep(random.randint(2, 8))
            click_ad(d_browser)
        except Exception as e:
            print("Error occurred. Retrying")
            traceback.print_exc()
            d_browser.quit()

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        d_browser.quit()


def visit_site_with_google(g_browser):
    print("Doing Google Search")
    print("Direct Visit --- Other site")
    try:
        print("=====session start ... google search=====")

        search_url = Router().get_search_link()
        g_browser.get(search_url)
        g_wait = random.randint(5, 15)
        print(f"waiting {g_wait}s")
        time.sleep(g_wait)

        try:
            google_read_more = WebDriverWait(g_browser, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id=\"KByQx\"]/div")))

            if google_read_more is not None:
                google_read_more.click()
                print("Google read more ok!\n")
        except Exception as e:
            print("Error getting google read more\n")

        time.sleep(2)

        try:
            google_consent = WebDriverWait(g_browser, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id=\"L2AGLb\"]/div")))

            if google_consent is not None:
                google_consent.click()
                print("Google consent ok!\n")
        except Exception as e:
            print("Error getting google consent\n")

        time.sleep(2)
        visit_other_site_direct(g_browser)

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        g_browser.quit()


def visit_other_site_direct(o_browser):
    print("Direct Visit --- Other site")
    try:
        print("=====session start =====")

        o_browser.get(Rand().get_other_site_link())
        o_wait = random.randint(5, 15)
        print(f"waiting {o_wait}s")
        time.sleep(o_wait)

        visit_site_direct(o_browser)

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        o_browser.quit()


def run_browser():
    numb = random.choice([0, 1])
    print("Selected Choice: " + str(numb))
    if numb == 0:
        custom_ua = UserAgentManager().get_phone_user_agent()
        print("Using Android Mobile: " + custom_ua)
    else:
        custom_ua = UserAgents().get_user_agent()
        print("Using PC / iOS: " + custom_ua)

    s_proxy = ProxyManager().get_proxy()
    print(f'Using Proxy: {s_proxy}')

    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={custom_ua}")
    chrome_options.add_argument(f"--proxy-server=socks5://{s_proxy}")
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                               options=chrome_options)
    browser.set_window_size(random.randint(900, 2000), random.randint(900, 1080))
    try:
        # choice to visit other site
        random_num = random.randint(1, 5)
        if random_num <= 4:
            """now visit other site"""
            print("Visiting other site")
            google_random = random.randint(1, 4)
            if google_random <= 4:
                visit_site_with_google(browser)
            else:
                visit_other_site_direct(browser)

        else:
            """go direct to target"""
            visit_site_direct(browser)

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        browser.quit()


loop()
