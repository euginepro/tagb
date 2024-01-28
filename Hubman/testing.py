import time

from selenium import webdriver

# Create a new instance of the Chrome driver (you can use other drivers as well)
driver = webdriver.Chrome()

# Open the initial URL in the first tab
driver.get("https://www.euginetech.com")
time.sleep(5)
# Open a new tab with a new URL
new_url = "https://hub.euginetech.com"
driver.execute_script(f"window.open('{new_url}', '_blank');")

# Switch to the new tab (assuming it's the last opened tab)
driver.switch_to.window(driver.window_handles[-1])

# Do some actions on the second tab if needed

# Switch back to the first tab
driver.switch_to.window(driver.window_handles[0])

# Do some actions on the first tab if needed

# Close the browser window
driver.quit()
