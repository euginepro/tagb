import shutil
import socket
import traceback

import requests
import random
import os
import time


class ProxyManager:
    def __init__(self, url=None, local_file='proxy_data/saved_proxies.txt',
                 last_updated_file='proxy_data/last_updated.txt',
                 refresh_interval=300):
        self.url = url or "https://raw.githubusercontent.com/larrybender930/wbmov/refs/heads/main/p.txt"
        self.local_file = local_file
        self.last_updated_file = last_updated_file
        self.refresh_interval = refresh_interval
        self.ensure_directory_exists()
        self.last_updated = self.load_last_updated()
        self.proxies = self.load_proxies()

    def ensure_directory_exists(self):
        directory = os.path.dirname(self.local_file)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print('Dir created.')

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
            self.save_last_updated(self.last_updated)  # Update last updated time in the file
        except Exception as e:
            print("Unable to refresh proxies.\n")
            print("sleep 1min")
            traceback.print_exc()
            try:
                print("removing proxy data")
                shutil.rmtree('proxy_data')
                print('====done====')
                self.ensure_directory_exists()
                print('New proxy_data folder created')

            except Exception as e:
                print(f'Error {e}')
            time.sleep(10)
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
