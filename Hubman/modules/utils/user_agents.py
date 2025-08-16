import random
try:
    from .chrome_versions import chrome_linux_releases, chrome_ios_releases, chrome_mac_releases, \
        chrome_windows_releases
    from .apple_versions import ios_versions, macos_versions
except:
    from chrome_versions import chrome_linux_releases, chrome_ios_releases, chrome_mac_releases, \
        chrome_windows_releases
    from apple_versions import ios_versions, macos_versions

class UserAgents:
    def __init__(self):
        self.rand_ua = ""
        self.windows = "Windows NT 10.0"
        self.mozilla = "Mozilla/5.0 "
        self.iPhoneUserAgent = ""
        self.macUserAgent = ""
        self.windowsUserAgent = ""
        self.linuxUserAgent = ""
        self.chrome_linux_release = random.choice(chrome_linux_releases)
        self.chrome_linux_ver = self.chrome_linux_release[:3]
        self.chrome_ios_release = random.choice(chrome_ios_releases)
        self.chrome_ios_ver = self.chrome_ios_release[:3]
        self.ios_ver_str = random.choice(ios_versions)
        self.ios_version = self.ios_ver_str.replace('_','.')
        self.chrome_windows_release = random.choice(chrome_windows_releases)
        self.chrome_windows_version = self.chrome_windows_release[:3]
        self.chrome_mac_release = random.choice(chrome_mac_releases)
        self.mac_chrome_version = self.chrome_mac_release[:3]
        self.mac_version = random.choice(macos_versions)
        self.mac_version_dot = self.mac_version.replace('_','.')

        iType = ["iPhone", "iPad"]
        iPadDevice = f"CPU OS {self.ios_ver_str} like Mac OS X"
        iPhoneDevice = f"CPU iPhone OS {self.ios_ver_str} like Mac OS X"
        iphone = random.randint(0, len(iType) - 1)
        iDevice = iType[iphone]
        dModel = iPhoneDevice if iphone == 0 else iPadDevice
        self.device = iDevice
        phoneWebkit = f"AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{self.chrome_ios_release} Mobile/15E148 Safari/604.1"

        self.macUserAgent = f"Mozilla/5.0 (Macintosh; Intel Mac OS X {self.mac_version}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.mac_chrome_version}.0.0.0 Safari/537.36"
        self.iPhoneUserAgent = self.mozilla + "(" + iDevice + "; " + dModel + ") " + phoneWebkit
        self.windowsUserAgent = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.chrome_windows_version}.0.0.0 Safari/537.36"
        self.linuxUserAgent = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.chrome_linux_ver}.0.0.0 Safari/537.36"

    def get_iPhone_user_agent(self):
        return self.iPhoneUserAgent, self.chrome_ios_ver, self.chrome_ios_release, self.device, self.ios_version,

    def get_mac_user_agent(self):
        return self.macUserAgent, self.mac_chrome_version, self.chrome_mac_release, self.mac_version_dot

    def get_windows_user_agent(self):
        return self.windowsUserAgent, self.chrome_windows_version, self.chrome_windows_release

    def get_linux_user_agent(self):
        return self.linuxUserAgent, self.chrome_linux_ver, self.chrome_linux_release

"""ag = UserAgents()
print(ag.get_iPhone_user_agent())
print(ag.get_mac_user_agent())
print(ag.get_linux_user_agent())
print(ag.get_windows_user_agent())"""
