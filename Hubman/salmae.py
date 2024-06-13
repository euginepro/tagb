import random
import time
import traceback

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from salma_muragon.salma_links import SalmaLinkManager
from eurofutbol.proxies import ProxyManager
from eurofutbol.link_rand import Rand
from eurofutbol.link_router import Router
from utils.user_agents import UserAgents
from utils.android_user_agents import UserAgentManager

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from selenium import webdriver


def loop():
    try:
        while True:
            run_browser()
    except:
        loop()


def click_ad(m_browser):
    ad_random = random.randint(1, 100)
    """Using CTR 8%"""
    ctr = 35
    if ad_random <= ctr:
        actions = ActionChains(m_browser)
        try:
            div = WebDriverWait(m_browser, 15).until(EC.presence_of_element_located((By.ID, "epad")))
            print("div found")
            actions.move_to_element(div).perform()
            print("Moved to div")
        except Exception as e:
            print("div not found")

        try:
            element_to_click = WebDriverWait(m_browser, 40).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#epad .adsbygoogle")))

            actions.move_to_element(element_to_click).perform()
            print("moved to ad")
            time.sleep(1)
            x_offset = random.randint(5, 15)
            y_offset = random.randint(5, 15)
            actions.move_by_offset(x_offset, y_offset).perform()
            actions.click().perform()
            print("clicked")
            print("\nwaiting page load before scroll\n")
            time.sleep(random.randint(10, 15))
            actions.send_keys(Keys.PAGE_DOWN).perform()
            print("scrolled\n")
            time.sleep(random.randint(1, 6))
            actions.send_keys(Keys.PAGE_DOWN).perform()
        except Exception as e:
            print("Ad Was not found")
            traceback.print_exc()

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


def load_site(time_out, driver, salma_url):
    try:
        driver.set_page_load_timeout(time_out)
        print(f'Using Timeout: {time_out}')
        driver.get(salma_url)
    except TimeoutException as e:
        time_out *= 2.5
        time.sleep(2)
        if time_out < 500:
            load_site(time_out, driver, salma_url)
        else:
            print("Max Timeout Exceeded! Retrying")
            driver.quit()

    except Exception as e:
        traceback.print_exc()
        driver.quit()
        print("Possible Proxy Or Network error")
        raise Exception("Custom Exception to skip exec")


def visit_site_direct(d_browser, page_views):
    print("Direct Visit")
    print(f'To make {page_views} page views')
    try:
        print("=====session start ..direct visit=====")

        load_site(30, d_browser, SalmaLinkManager().get_link())
        print("waiting 5s")
        time.sleep(5)

        got = False
        runs = 0
        while not got and runs < 20:
            try:
                consent_ok = d_browser.find_element(By.XPATH,
                                                    f"/html/body/div[{runs}]/div[2]/div[1]/div[3]/div[2]/button[1]")
                if consent_ok is not None:
                    got = True
                    consent_ok.click()
                    print(f"Consent dismissed! at div {runs}")

            except Exception as e:
                print(f"Runs: {runs} but Consent button not found")
            runs += 1

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
                    sleep_time = random.randint(5, 20)
                    print("Waiting " + str(sleep_time) + " Seconds after page down")
                    time.sleep(sleep_time)
                else:
                    page_finished = True
                    print("Scrolled To Bottom")
            """Scroll Back to top"""
            ActionChains(d_browser).send_keys(Keys.HOME).perform()
            print("waiting 2 to 5 seconds")
            time.sleep(random.randint(2, 5))

            page_views -= 1
            if page_views > 0:
                visit_site_direct(d_browser, page_views)
            else:
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
    try:
        print("=====session start ... google search=====")

        search_url = Router().get_search_link()
        g_browser.get(search_url)
        g_wait = random.randint(2, 5)
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
            google_consent = WebDriverWait(g_browser, 2).until(EC.presence_of_element_located(
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
        o_wait = random.randint(1, 5)
        print(f"waiting {o_wait}s")
        time.sleep(o_wait)

        visit_site_direct(o_browser, random.randint(1, 3))

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
    proxy_string = ProxyManager().get_proxy()
    print(f'Using Proxy: {proxy_string}')
    chrome_options = Options()
    chrome_options.add_argument(f"--proxy-server=socks5://{proxy_string}")
    chrome_options.add_argument(f"user-agent={custom_ua}")
    browser = webdriver.ChromiumEdge(service=EdgeService(EdgeChromiumDriverManager().install()),
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
            visit_site_direct(browser, random.randint(1, 3))

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        browser.quit()


loop()
