print("Importing requirements...")
import random
import time
import traceback

from modules.hubman_funcs.functions import *
from modules.gimme.life_links import LifeLinkManager
from modules.utils.iphone_names import IOSNameMgr
import undetected_chromedriver as uc

from modules.eurofutbol.lugamovies_proxies import LugaMoviesProxyManager
from modules.selenium_stealth import stealth
import requests
from requests import Timeout, RequestException
from socks import ProxyError
import socket

from modules.utils.proxy_timezone import ProxyUtils
from modules.utils.user_agents import UserAgents
from modules.utils.android_user_agents import UserAgentManager
from selenium.webdriver import ChromeService as ch_service
from modules.device_util.devices import random_device_name, random_mac_address
from modules.hubman_funcs.spoof_script import get_spoof_script
from modules.hubman_funcs.prevent_new_tabs import get_prevent_new_tabs_script
from modules.hubman_funcs.grease import random_grease_brand

print("Importing done...")

def loop():
    while True:
        try:
            run_browser()
        except Exception as e:
            traceback.print_exc()
            time.sleep(1)

def set_custom_headers(browser, headers):
    browser.execute_cdp_cmd('Network.enable', {})
    # Set custom headers for all requests
    header_list = []
    for name, value in headers.items():
        if name.lower() != 'user-agent':  # Don't duplicate user-agent
            header_list.append({'name': name, 'value': value})

    if header_list:
        browser.execute_cdp_cmd('Network.setExtraHTTPHeaders', {
            'headers': {h['name']: h['value'] for h in header_list}
        })
    print(f"Set {len(header_list)} custom HTTP headers")

def run_browser():
    print("++++Run Browser+++++")
    s_proxy = LugaMoviesProxyManager().get_proxy()
    s_proxy = "74.81.81.81:824"
    pturl = "http://www.google.com"
    proxy = s_proxy
    proxies = {
        "http": f"socks5://{proxy}",
        "https": f"socks5://{proxy}",
    }
    print(f"Check: {proxy}")
    try:
        response = requests.get(pturl, proxies=proxies, timeout=10)  # Increased timeout
        if response.status_code == 200:
            print("OK...\n\n")

    except (ProxyError, Timeout, socket.error, RequestException) as e:
        print("Dead===")
        raise Exception("Proxy Not Ok..")

    print(f'Using Proxy: {s_proxy}')

    '''
    0. Linux
    1, 9. Android
    2, 10. iOS device
    3, 4, 5. Win
    6, 7, 8. Mac

    int os_id
    '''
    # My Vars
    is_phone = False
    android_ua_mgr = UserAgentManager()
    ua_mgr = UserAgents()

    os_id = random.randint(0, 30)

    # init
    mac_addr = ''
    device_name = ''
    n_platform = ''
    n_user_agent = ''
    n_appVersion = n_user_agent.replace('Mozilla/', '')
    n_vendor = ''
    s_renderer = ''
    s_webgl = ''
    grease_brand = random_grease_brand()

    if os_id == 0:
        # Linux Chrome Headers
        linux_ua, browser_ver, browser_full_ver = ua_mgr.get_linux_user_agent()
        linux_wg_vendors = ['NVIDIA Corporation', 'Intel', 'AMD']
        linux_wg_renderers = ['NVIDIA GeForce GTX 1050 Ti/PCIe/SSE2', 'Intel(R) HD Graphics 630', 'AMD Radeon RX 570']
        n_platform = 'Linux x86_64'
        n_user_agent = linux_ua
        n_appVersion = n_user_agent.replace('Mozilla/', '')
        n_vendor = 'Google Inc.'
        n_language = 'en-US'
        s_webgl = random.choice(linux_wg_vendors)
        s_renderer = linux_wg_renderers[linux_wg_vendors.index(s_webgl)]
        mac_addr = random_mac_address('linux')
        device_name = random_device_name('linux')
        screen_color_depth = 24
        screen_pixel_depth = 24

        # HTTP Headers for Linux Chrome
        http_headers = {
            'sec-ch-ua': f'"Chromium";v="{browser_ver}", "Google Chrome";v="{browser_ver}", "{grease_brand}";v="{browser_ver}"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-ch-ua-arch': '"x86_64"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-full-version-list': f'"Chromium";v="{browser_full_ver}", "Google Chrome";v="{browser_full_ver}", "{grease_brand}";v="{browser_full_ver}"',
            'upgrade-insecure-requests': '1',
            'dnt': '1',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document'
        }
        print(f'Using Linux: {linux_ua}')

    elif os_id == 1 or os_id == 9 or (10 < os_id < 25):
        # Android Chrome Headers
        android_ua, browser_ver, full_browser_ver, android_version, phone_model = android_ua_mgr.get_android_user_agent()
        is_phone = True
        android_wgv = ['Qualcomm', 'ARM', 'Imagination Technologies']
        android_wgr = ['Adreno (TM) 630', 'Mali-G76', 'PowerVR Rogue GE8320']
        n_platform = random.choice(["Linux armv7l", "Linux armv8l"])
        n_user_agent = android_ua
        n_appVersion = n_user_agent.replace('Mozilla/', '')
        n_vendor = 'Google Inc.'
        n_language = 'en-US'
        s_webgl = random.choice(android_wgv)
        s_renderer = android_wgr[android_wgv.index(s_webgl)]
        screen_color_depth = 24
        screen_pixel_depth = 24

        # HTTP Headers for Android Chrome
        http_headers = {
            'sec-ch-ua': f'"Chromium";v="{browser_ver}", "Google Chrome";v="{browser_ver}", "{grease_brand}";v="{browser_ver}"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': f'"{android_version}.0"',
            'sec-ch-ua-arch': '"arm64"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-model': f'"{phone_model}"',
            'sec-ch-ua-full-version-list': f'"Chromium";v="{full_browser_ver}", "Google Chrome";v="{full_browser_ver}", "{grease_brand}";v="{full_browser_ver}"',
            'upgrade-insecure-requests': '1',
            'dnt': '1',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document'
        }
        print(f'Using Android: {android_ua}')

    elif os_id == 2 or os_id == 10 or os_id >= 25:
        # iOS Chrome Headers (Chrome on iOS)
        iosMgr = IOSNameMgr()
        ios_ua, browser_ver, full_browser_ver, device, ios_version = ua_mgr.get_iPhone_user_agent()
        is_phone = True
        n_platform = device
        n_user_agent = ios_ua
        n_appVersion = n_user_agent.replace('Mozilla/', '')
        n_vendor = 'Apple Computer, Inc.'
        n_language = 'en-US'
        s_webgl = 'Apple Inc.'
        s_renderer = 'Apple GPU'
        device_name = iosMgr.get_iphone_name() if "iphone" in n_user_agent.lower() else iosMgr.get_ipad_name()
        screen_color_depth = 24
        screen_pixel_depth = 24

        # HTTP Headers for iOS Chrome
        device_model = iosMgr.get_device_model(device_name)
        http_headers = {
            'sec-ch-ua': f'"Google Chrome";v="{browser_ver}", "{grease_brand}";v="{browser_ver}", "Chromium";v="{browser_ver}"',
            'sec-ch-ua-mobile': '?1' if 'iPhone' in n_platform else '?0',
            'sec-ch-ua-platform': '"iOS"',
            'sec-ch-ua-platform-version': f'"{ios_version}"',
            'sec-ch-ua-model': f'"{device_model}"',
            'upgrade-insecure-requests': '1',
            'dnt': '1',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document'
        }

        print(f'Using iDevice: {ios_ua}')

    elif os_id == 3 or os_id == 5 or os_id == 6:
        # Windows Chrome Headers
        win_ua, browser_ver, full_browser_ver = ua_mgr.get_windows_user_agent()
        win_wgv = ['Google Inc. (Intel)', 'NVIDIA Corporation', 'Intel', 'AMD']
        win_wgr = ['ANGLE (Intel, Intel(R) HD Graphics 620 Direct3D11 vs_5_0 ps_5_0)',
                   'NVIDIA GeForce GTX 1080/PCIe/SSE2', 'Intel(R) HD Graphics 620', 'AMD Radeon RX 580']
        n_platform = 'Win32'
        n_user_agent = win_ua
        n_appVersion = n_user_agent.replace('Mozilla/', '')
        n_vendor = 'Google Inc.'
        n_language = 'en-US'
        s_webgl = random.choice(win_wgv)
        s_renderer = win_wgr[win_wgv.index(s_webgl)]
        mac_addr = random_mac_address('win')
        device_name = random_device_name('win')
        screen_color_depth = 24
        screen_pixel_depth = 24

        # HTTP Headers for Windows Chrome
        win_version = "10.0"
        http_headers = {
            'sec-ch-ua': f'"{grease_brand}";v="{browser_ver}", "Chromium";v="{browser_ver}", "Google Chrome";v="{browser_ver}"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': f'"{win_version}"',
            'sec-ch-ua-arch': '"x86_64"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-full-version-list': f'"{grease_brand}";v="{full_browser_ver}", "Chromium";v="{full_browser_ver}", "Google Chrome";v="{full_browser_ver}"',
            'upgrade-insecure-requests': '1',
            'dnt': '1',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document'
        }
        print(f'Using Win: {win_ua}')


    else:
        # macOS Chrome Headers
        mac_ua, browser_ver, full_browser_ver, mac_version = ua_mgr.get_mac_user_agent()
        mac_wgv = ['Apple Inc.', 'Intel Inc.', 'AMD']
        mac_wgr = ['Apple M1', 'Intel Iris Pro', 'AMD Radeon Pro 5500M']
        n_platform = 'MacIntel'
        n_user_agent = mac_ua
        n_appVersion = n_user_agent.replace('Mozilla/', '')
        n_vendor = 'Apple Computer, Inc.'
        n_language = 'en-US'
        s_webgl = random.choice(mac_wgv)
        s_renderer = mac_wgr[mac_wgv.index(s_webgl)]
        mac_addr = random_mac_address('mac')
        device_name = random_device_name('mac')
        screen_color_depth = 24
        screen_pixel_depth = 24

        # HTTP Headers for macOS Chrome
        http_headers = {
            'sec-ch-ua': f'"{grease_brand}";v="{browser_ver}","Chromium";v="{browser_ver}", "Google Chrome";v="{browser_ver}"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-ch-ua-platform-version': f'"{mac_version}"',
            'sec-ch-ua-arch': '"arm"' if 'M1' in s_renderer else '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-full-version-list': f'"{grease_brand}";v="{full_browser_ver}", "Chromium";v="{full_browser_ver}", "Google Chrome";v="{full_browser_ver}"',
            'upgrade-insecure-requests': '1',
            'dnt': '1',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document'
        }
        print(f'Using Mac: {mac_ua}')

    tizone = ProxyUtils().get_timezone_from_proxy(proxy)
    print(f'Got TimeZone: {tizone}')

    chrome_options = uc.ChromeOptions()
    #chrome_options.add_argument(f"--proxy-server=socks5://{proxy}")
    chrome_options.add_argument(f'--user-agent={n_user_agent}')
    chrome_options.add_argument("--disable-popup-blocking")
    # Disable WebDriver flags
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--no-sandbox")

    #Extra
    chrome_options.add_argument('--disable-features=VizDisplayCompositor')
    chrome_options.add_argument('--disable-ipc-flooding-protection')
    chrome_options.add_argument('--disable-extensions-file-access-check')
    chrome_options.add_argument('--disable-extensions-http-throttling')
    chrome_options.add_argument('--disable-plugins-discovery')

    # partially disable webrtc
    preferences = {
        "webrtc.ip_handling_policy": "disable_non_proxied_udp",
        "webrtc.multiple_routes_enabled": False,
        "webrtc.nonproxied_udp_enabled": False
    }
    chrome_options.add_experimental_option("prefs", preferences)

    width = random.randint(900, 2000)
    height = random.randint(900, 1080)

    cores = random.choice(range(2, 8, 2))
    ram = random.choice([2, 4, 8, 16, 32, 64])

    chrome_binary = r'chrome/chrome.exe'

    chrome_options.binary_location = chrome_binary
    service = ch_service(executable_path="chrome_driver/chromedriver.exe")

    print(f"======DEVICE DETAILS======\nName: {device_name}\nMac Addr: {mac_addr}")

    print('Init wd')
    browser = uc.Chrome(use_subprocess=True, options=chrome_options, service=service,
                        driver_executable_path="chrome_driver/chromedriver.exe")
    print('ok')

    if tizone:
        tz_params = {'timezoneId': tizone}
        browser.execute_cdp_cmd('Emulation.setTimezoneOverride', tz_params)
        print(f'Set TimeZone: {tizone}')

    if is_phone:

        cores = 0
        ram = random.choice([2, 3, 4, 6, 8, 12])
        print("====== Using mobile Device ======")
        dimens = [[375, 800], [415, 800], [375, 667], [414, 896], [390, 844], [430, 932],
                  [412, 915], [360, 740], [412, 915], [768, 1024], [820, 1180], [1024, 1366],
                  [912, 1368], [540, 720], [344, 882], [853, 1280], [412, 914], [1024, 600], [1280, 800]]

        index = random.randint(0, len(dimens) - 1)
        width = dimens[index][0]
        print(f"Width: {width}")
        height = dimens[index][1]
        print(f"Height: {height}")
        pixel_ratio = random.choice([1.0, 1.25, 1.5, 2.0, 3.0])
        arch = ''
        avail_height = height
        avail_width = width
        max_touch_points = 5
        spoof_script = f"""
            Object.defineProperty(navigator, 'maxTouchPoints', {{get: () => {max_touch_points}}});
            Object.defineProperty(window, 'devicePixelRatio', {{get: () => {pixel_ratio} }});
            window.ontouchstart = true;
            console.log("end mobile spooff!")
            """
        browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": spoof_script
        })

    else:
        avail_height = height - random.randint(40, 80)  # Taskbar height
        avail_width = width

    fingerprint_spoof_script = get_spoof_script(n_platform, n_appVersion, n_vendor,n_user_agent, n_language, ram, cores, screen_color_depth, screen_pixel_depth, avail_height,
                     avail_width, width, height,s_webgl, s_renderer, device_name, mac_addr)
    prevent_new_tabs_script = get_prevent_new_tabs_script()

    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": fingerprint_spoof_script
    })
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": prevent_new_tabs_script
    })

    stealth(browser,
            languages=["en-US", "en"],
            vendor=n_vendor,
            platform=n_platform,
            webgl_vendor=s_webgl,
            renderer=s_renderer,
            fix_hairline=True,
            )

    browser.set_window_size(width, height)
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
                visit_other_site_direct(browser, random.randint(1, 2))

        else:
            """go direct to target"""
            visit_site_direct(browser, random.randint(1, 3))

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        close_browser(browser)
    finally:
        close_browser(browser)
        print("Ended Finally.")


print("Program Start")
set_site_links_manager(LifeLinkManager())
loop()
