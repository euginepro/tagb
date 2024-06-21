import requests
import random
import os
import time


class ProxyManager:
    def __init__(self, url=None, local_file='saved_proxies.txt', last_updated_file='last_updated.txt',
                 refresh_interval=300):
        self.url = url or "https://raw.githubusercontent.com/euginepro/tagbb/main/p.txt"
        self.local_file = local_file
        self.last_updated_file = last_updated_file
        self.refresh_interval = refresh_interval
        self.last_updated = self.load_last_updated()
        self.proxies = self.load_proxies()

    def load_last_updated(self):
        if os.path.exists(self.last_updated_file):
            with open(self.last_updated_file, 'r') as f:
                return float(f.read().strip())
        return 0

    def save_last_updated(self, timestamp):
        with open(self.last_updated_file, 'w') as f:
            f.write(str(timestamp))

    def load_proxies(self):
        if self.should_refresh():
            self.refresh_proxies()
        return self.read_local_proxies()

    def should_refresh(self):
        if not os.path.exists(self.local_file) or not os.path.exists(self.last_updated_file):
            return True
        if time.time() - self.last_updated > self.refresh_interval:
            return True
        return False

    def refresh_proxies(self):
        try:
            print("Refreshing Proxies")
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.text
            proxies = [proxy.strip() for proxy in data.split('\n') if proxy.strip()]
            self.write_local_proxies(proxies)
            self.last_updated = time.time()
            self.save_last_updated(self.last_updated)  # Update last updated time in the fil
        except Exception as e:
            print("Unable to refresh proxies.\n")
            print("sleep 1min")
            time.sleep(60)
            print("Retrying")
            self.refresh_proxies()

    def read_local_proxies(self):
        with open(self.local_file, 'r') as f:
            proxies = [line.strip() for line in f.readlines()]
        return proxies

    def write_local_proxies(self, proxies):
        with open(self.local_file, 'w') as f:
            for proxy in proxies:
                f.write(f"{proxy}\n")

    def get_proxy(self):
        return random.choice(self.proxies)


# Example usage
proxy_manager = ProxyManager()
print(f'Proxy: {proxy_manager.get_proxy()}')
