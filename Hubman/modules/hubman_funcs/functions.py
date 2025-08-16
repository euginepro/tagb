import random
import time
import traceback

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..eurofutbol.link_router import Router
from ..link_rand import Rand

SITE_LINKS_MANAGER = None
def set_site_links_manager(manager):
    global SITE_LINKS_MANAGER
    SITE_LINKS_MANAGER = manager
    
def close_browser(driver):
    try:
        window_handles = driver.window_handles
        print(f"Number of open windows: {len(window_handles)}")
        for handle in window_handles:
            driver.switch_to.window(handle)
            time.sleep(2)
            driver.close()
        print("Closed All Windows")
        driver.quit()
    except Exception as e:
        print(f'Error closing browser: {e}')
        driver.quit()


def get_last_opened_tab(driver, current_handles):
    new_handles = driver.window_handles
    print(f"Current tabs: {len(new_handles)}")
    if len(new_handles) > len(current_handles):
        latest_tab_handle = new_handles[-1]  # The last handle in the list is the most recently opened tab
        driver.switch_to.window(latest_tab_handle)
        print(f"Switched to new tab: {driver.current_url}")
        return new_handles  # Return updated list of handles
    print('No new tab.')
    return current_handles  # No new tab, return current list of handles


def click_ad(m_browser):
    current_handles = m_browser.window_handles
    print(f"Current tabs: {len(current_handles)}")
    ad_random = random.randint(1, 100)
    """Using CTR 8%"""
    ctr = 0 #not clicking
    if ad_random <= ctr:
        actions = ActionChains(m_browser)
        try:
            div = WebDriverWait(m_browser, 15).until(EC.presence_of_element_located((By.ID, "epad")))
            print("div found")
            actions.scroll_to_element(div).perform()
            print("Scrolled to div")
            actions.move_to_element(div).perform()
            print("Moved to div")
        except Exception as e:
            print("div not found")

        try:
            element_to_click = WebDriverWait(m_browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#epad .adsbygoogle"))
            )

            print("Ad exists")
            actions.scroll_to_element(element_to_click).perform()
            print("Scrolled to ad")
            actions.move_to_element(element_to_click).perform()
            print("moved to ad")
            time.sleep(1)
            x_offset = random.randint(5, 15)
            y_offset = random.randint(5, 15)
            actions.move_by_offset(x_offset, y_offset).perform()
            actions.click().perform()
            print("clicked")

            print('Sleep: 1')
            time.sleep(1)

            print('\nCheck For New Tab')
            current_handles = get_last_opened_tab(m_browser, current_handles)

            print('Sleep: 2')
            time.sleep(2)

            print("Waiting 1 to 4s")
            time.sleep(random.randint(1, 4))
            actions.send_keys(Keys.PAGE_DOWN).perform()
            print("Scrolled")

            """Slowly scroll to bottom of ad landing page"""
            page_finished = False
            scroll_times = 0
            while not page_finished:
                if not m_browser.execute_script(
                        "return (window.innerHeight + window.scrollY) >= document.body.scrollHeight - 1000;"):
                    print("Still Scrolling Ad L Page")

                    actions.send_keys(Keys.PAGE_DOWN).perform()
                    scroll_times += 1
                    sleep_time = random.randint(8, 18)
                    print("Waiting " + str(sleep_time) + " Seconds after L page down")
                    time.sleep(sleep_time)
                    if scroll_times >= 10:
                        page_finished = True
                else:
                    page_finished = True
                    print("Scrolled To Bottom Of Ad L Page")
            """Scroll Back to top"""
            actions.send_keys(Keys.HOME).perform()

            print("waiting 1 to 3 seconds")
            time.sleep(random.randint(1, 3))

            print('can wait 10s')
            wait = WebDriverWait(m_browser, 10)
            try:
                links = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))
                if links:
                    print(f"{len(links)} links found.")
                    time.sleep(2)
                    link_tries = 0
                    while link_tries < 5:
                        try:
                            link_tries += 1
                            random_link = random.choice(links)
                            print(f'Random Link Chosen: {link_tries}')
                            actions.scroll_to_element(random_link).perform()
                            print('Scrolled to link')
                            actions.move_to_element(random_link).perform()
                            print('Moved to link')
                            actions.click(random_link).perform()
                            print('Link Clicked')
                            break
                        except Exception as e:
                            # Exception Ignored
                            print('Error With Chosen Link')

                    print('Check if there is a new tab')
                    current_handles = get_last_opened_tab(m_browser, current_handles)
                    print('Engage with Loaded Page..')
                    print('\nSleep: 1 to 4')
                    time.sleep(random.randint(1, 4))
                    actions.send_keys(Keys.PAGE_DOWN).perform()
                    wt2 = random.randint(1, 10)
                    print(f' Waiting {wt2} before scroll')
                    time.sleep(wt2)
                    actions.send_keys(Keys.PAGE_DOWN).perform()
                    print('Scrolled')

                    third_page_random = random.randint(0, 5)
                    if third_page_random > 3:
                        print('Engaging third page')
                        try:
                            links = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))
                            if links:
                                print(f"{len(links)} links found on third page.")
                                time.sleep(2)
                                link_tries = 0
                                while link_tries < 5:
                                    try:
                                        link_tries += 1
                                        random_link = random.choice(links)
                                        print(f'P#3 Random Link Chosen: {link_tries}')
                                        actions.scroll_to_element(random_link).perform()
                                        print('P#3 Scrolled to link')
                                        actions.move_to_element(random_link).perform()
                                        print('P#3 Moved to link')
                                        actions.click(random_link).perform()
                                        print('P#3 Link Clicked')
                                        break
                                    except Exception as e:
                                        # Exception Ignored
                                        print('Error With Chosen Link')

                                print('Check if there is a new tab')
                                current_handles = get_last_opened_tab(m_browser, current_handles)
                                print('Engage with Loaded Page..')
                                print('\nSleep: 1 to 4')
                                time.sleep(random.randint(1, 4))
                                actions.send_keys(Keys.PAGE_DOWN).perform()
                                wt2 = random.randint(1, 10)
                                print(f' Waiting {wt2} before scroll')
                                time.sleep(wt2)
                                actions.send_keys(Keys.PAGE_DOWN).perform()
                                print('Scrolled')
                            else:
                                print("No links found on the page.")
                        except Exception as e:
                            print("Error in third engagement")
                            traceback.print_exc()

                else:
                    print("No links found on the page.")
            except Exception as e:
                print('Error Getting Links')
                traceback.print_exc()
        except Exception as e:
            print("Ad Was not found")
            traceback.print_exc()

        wait = random.randint(1, 5)
        print("waiting: " + str(wait))
        time.sleep(wait)
        close_browser(m_browser)
        print("====End Session====")
        time.sleep(1)
    else:
        print("Not to click this round")
        wait = random.randint(2, 5)
        print("waiting: " + str(wait))
        time.sleep(wait)
        close_browser(m_browser)
        print("====End Session====")
        time.sleep(2)

    print("Session Ended")


def visit_site_direct(d_browser, page_views):
    print("Direct Visit")
    print(f'To make {page_views} page views')
    try:
        print("=====session start ..direct visit=====")

        d_browser.get(SITE_LINKS_MANAGER.get_link())
        print("waiting 5s")
        time.sleep(5)

        got = False
        runs = 0
        while not got and runs < 20:
            try:
                consent_ok = d_browser.find_element(By.XPATH,
                                                    f"/html/body/div[{runs}]/div[2]/div[2]/div[3]/div[2]/button[1]")
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
                    sleep_time = random.randint(10, 25)
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
            close_browser(d_browser)

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        close_browser(d_browser)


def visit_site_with_google(g_browser):
    print("Doing Google Search")
    try:
        print("=====session start ... google search=====")

        search_url = Router().get_search_link()
        g_browser.get(search_url)
        g_wait = random.randint(1, 5)
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

        time.sleep(1)
        visit_other_site_direct(g_browser, random.randint(1, 2))

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        close_browser(g_browser)


def visit_other_site_direct(o_browser, visits):
    print("Direct Visit --- Other site")
    print(f'To make {visits} other visits')
    try:
        print("=====session start =====")

        o_browser.get(Rand().get_other_site_link())
        o_wait = random.randint(1, 3)
        print(f"waiting {o_wait}s")
        time.sleep(o_wait)

        visits -= 1
        if visits > 0:
            visit_other_site_direct(o_browser, visits)
        else:
            visit_site_direct(o_browser, random.randint(1, 3))

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        close_browser(o_browser)