import random
import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.chrome import ChromeDriverManager

from android_user_agents import UserAgentManager
from eurofutbol.proxies import ProxyManager
from user_agents import UserAgents

# Set the proxy server details
proxy_address = "ca.smartproxy.com"
proxy_port = "20005"

user = "spxzdnr5g6"
password = "7xvb44wYnaJi_1rHdA"


# Set up proxy settings
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = f"{proxy_address}:{proxy_port}"

proxy_address1 = f"{proxy_address}:{proxy_port}"

# If the proxy requires authentication, set the credentials
# proxy.add_argument(f"--proxy-auth={proxy_username}:{proxy_password}")

numb = random.choice([0, 1])
print("Selected Choice: " + str(numb))
if numb == 0:
    custom_ua = UserAgentManager().get_phone_user_agent()
    print("Using Android Mobile: " + custom_ua)
else:
    custom_ua = UserAgents().get_user_agent()
    print("Using PC / iOS: " + custom_ua)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-agent={custom_ua}")

# Set up Chrome options


chrome_options.add_argument("--ignore-certificate-errors")  # Optional: Ignore certificate errors

# Add the proxy settings to Chrome options
# chrome_options.add_argument("--proxy-server=http://{}".format(proxy_address1))

s_proxy = ProxyManager().get_proxy()
print(s_proxy)
chrome_options.add_argument(f"--proxy-server=socks5://{s_proxy}")

# Specify the path to your Chrome driver


# Initialize the Chrome driver with the proxy settings and options
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                           options=chrome_options)
browser.set_window_size(random.randint(900, 2000), random.randint(900, 1080))


# Example usage: Open a website
browser.get("https://ipinfo.io/json")

# Do your selenium actions here...
time.sleep(5000)
# Close the browser session

