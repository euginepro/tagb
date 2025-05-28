import requests
import socks
import socket
from requests.exceptions import RequestException


class ProxyUtils:
    def __init__(self):
        # Save the original socket object
        self.original_socket = socket.socket

    def _configure_proxy(self, proxy_ip_port):
        try:
            # Split proxy into IP and port
            proxy_ip, proxy_port = proxy_ip_port.split(':')
            proxy_port = int(proxy_port)

            # Configure SOCKS5 proxy
            socks.set_default_proxy(socks.SOCKS5, proxy_ip, proxy_port)
            socket.socket = socks.socksocket
        except Exception as e:
            print(f"Failed to configure proxy: {e}")
            raise

    def _reset_proxy(self):
        # Restore the original socket object
        socket.socket = self.original_socket

    def _get_real_ip(self, proxy_ip_port):
        try:
            # Configure proxy and get real IP
            self._configure_proxy(proxy_ip_port)
            response = requests.get("https://api.ipify.org?format=json", timeout=10)
            response.raise_for_status()

            return response.json().get('ip', 'Unknown')
        except (RequestException, socket.error) as e:
            print(f"Failed to get real IP: {e}")
            return None
        finally:
            # Ensure proxy is reset even if an exception occurs
            self._reset_proxy()

    def get_timezone_from_ip(self, ip_address):
        try:
            # Fetch timezone information from IP
            response = requests.get(f"https://ipinfo.io/{ip_address}/json", timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get('timezone', 'Unknown')
        except RequestException as e:
            print(f"Failed to get timezone from IP: {e}")
            return 'Unknown'

    def get_timezone_from_proxy(self, proxy_ip_port):
        # Get real IP from the proxy and then get timezone
        real_ip = self._get_real_ip(proxy_ip_port)
        if real_ip:
            timezone = self.get_timezone_from_ip(real_ip)
            if timezone == 'Unknown':
                return None
            return timezone
        else:
            return None


# Example usage
'''proxy_ip_port = "148.21.5.30:824"
proxy_utils = ProxyUtils()
timezone = proxy_utils.get_timezone_from_proxy(proxy_ip_port)
print(f"Time Zone: {timezone}")'''
