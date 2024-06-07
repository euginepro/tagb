import random
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def loadSite(time_out):
    try:
        driver.set_page_load_timeout(time_out)
        print(f'Using Timeout: {time_out}')
        driver.get('https://jbtips.muragon.com/entry/37.html')
    except Exception as e:
        time_out *= 2.5
        time.sleep(2)
        loadSite(time_out)


# Set up the WebDriver (using Chrome in this example)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
actions = ActionChains(driver)
loadSite(30)

# Locate the div by its id
try:
    div = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "epad")))
    print("div found")
    actions.move_to_element(div).perform()
    print("Moved to div")
except Exception as e:
    print("div not found")

try:
    element_to_click = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#epad .adsbygoogle")))

    actions.move_to_element(element_to_click).perform()
    print("moved to ad")
    time.sleep(1)
    x_offset = random.randint(5, 15)
    y_offset = random.randint(5, 15)
    actions.move_by_offset(x_offset, y_offset).perform()
    actions.click().perform()
    print("clicked")
except Exception as e:
    print("Ad Was not found")
    traceback.print_exc()

print("Sleep")
time.sleep(5000)
driver.quit()
