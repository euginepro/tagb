import random


class UserAgents:
    def __init__(self):
        self.rand_ua = ""
        self.windows = ["Windows NT 10.0"]
        self.mozilla = "Mozilla/5.0 "
        self.iPhoneUserAgent = ""
        self.macUserAgent = ""
        self.windowsUserAgent = ""
        self.linuxUserAgent = ""

        windowsNT = random.choice(self.windows)
        iType = ["iPhone", "iPad", "iPod touch"]
        p1 = str(random.randint(12, 17))
        p2 = str(random.randint(0, 9))
        p3 = str(random.randint(0, 9))
        mac = str(random.randint(11, 14))

        iPadDevice = "CPU OS " + p1 + "_" + p2 + "_" + p3 + " like Mac OS X"
        iPhoneDevice = "CPU iPhone OS " + p1 + "_" + p2 + "_" + p3 + " like Mac OS X"
        iPodDevice = "CPU " + p1 + "_" + p2 + "_" + p3 + " like Mac OS X"
        macId = "Intel Mac OS X " + mac + "_" + p2
        iphone = random.randint(0, len(iType) - 1)
        iDevice = iType[iphone]
        dModel = iPhoneDevice if iphone == 0 else iPadDevice if iphone == 1 else iPodDevice

        wn = str(random.randint(500, 606))
        sn = str(random.randint(500, 606))
        version = str(random.randint(15, 30))
        phoneWebkit = "AppleWebKit/" + wn + ".1.15 " + "(KHTML, like Gecko) Version/" + version + " Mobile/15E148 Safari/" + sn + ".1"
        macWebkit = "AppleWebKit/" + wn + ".1.15 " + "(KHTML, like Gecko) Version/" + version + " Safari/" + sn + ".1"
        wkitVersion = str(random.randint(530, 606))
        chromeVer = str(random.randint(90, 119))
        decimal = str(random.randint(0, 40))
        safariVer = str(random.randint(537, 606))
        operaVer = str(random.randint(90, 120))
        firefoxVersion = str(random.randint(90, 120))
        geckoVersion = str(random.randint(20000000, 30000000))

        webOpera = "Mozilla/5.0 (" + windowsNT + "; Win64; x64) AppleWebKit/" + wkitVersion + "." + decimal + " (KHTML, like Gecko) Chrome/" + chromeVer + ".0.0.0 Safari/" + safariVer + "." + decimal + " OPR/" + operaVer + ".0.0.84"
        webChrome = "Mozilla/5.0 (" + windowsNT + "; Win64; x64) AppleWebKit/" + wkitVersion + "." + decimal + " (KHTML, like Gecko) Chrome/" + chromeVer + ".0.0.0 Safari/" + safariVer + "." + decimal
        webFirefox = "Mozilla/5.0 (" + windowsNT + "; Win64; x64; rv:" + firefoxVersion + ") Gecko/" + geckoVersion + " Firefox/" + firefoxVersion
        web = [webOpera, webChrome, webFirefox]

        fireFoxUbuntu = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:" + firefoxVersion + ") Gecko/" + geckoVersion + " Firefox/" + firefoxVersion
        fireFoxLinux = "Mozilla/5.0 (X11; Linux x86_64; rv:" + firefoxVersion + ") Gecko/" + geckoVersion + " Firefox/" + firefoxVersion
        fireFoxDebian = "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:" + firefoxVersion + ") Gecko/" + geckoVersion + " Firefox/" + firefoxVersion
        fireFoxFedora = "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:" + firefoxVersion + ") Gecko/" + geckoVersion + " Firefox/" + firefoxVersion
        chromeLinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/" + wkitVersion + "." + decimal + " (KHTML, like Gecko) Chrome/" + chromeVer + ".0.0.0 Safari/" + safariVer + "." + decimal
        chromeDebian = "Mozilla/5.0 (X11; Debian; Linux x86_64) AppleWebKit/" + wkitVersion + "." + decimal + " (KHTML, like Gecko) Chrome/" + chromeVer + ".0.0.0 Safari/" + safariVer + "." + decimal
        chromeUbuntu = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/" + wkitVersion + "." + decimal + " (KHTML, like Gecko) Chrome/" + chromeVer + ".0.0.0 Safari/" + safariVer + "." + decimal
        chromeKali = "Mozilla/5.0 (X11; Kali; Linux x86_64) AppleWebKit/" + wkitVersion + "." + decimal + " (KHTML, like Gecko) Chrome/" + chromeVer + ".0.0.0 Safari/" + safariVer + "." + decimal
        chromeFedora = "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/" + wkitVersion + "." + decimal + " (KHTML, like Gecko) Chrome/" + chromeVer + ".0.0.0 Safari/" + safariVer + "." + decimal

        linuxes = [fireFoxUbuntu, chromeLinux, chromeDebian, chromeUbuntu, fireFoxDebian, fireFoxLinux, fireFoxFedora,
                   chromeKali, chromeFedora]

        self.macUserAgent = self.mozilla + "(Macintosh; " + macId + ") " + macWebkit
        self.iPhoneUserAgent = self.mozilla + "(" + iDevice + "; " + dModel + ") " + phoneWebkit
        self.windowsUserAgent = random.choice(web)
        self.linuxUserAgent = random.choice(linuxes)

    def get_iPhone_user_agent(self):
        return self.iPhoneUserAgent

    def get_web_user_agent(self):
        web_uas = [self.macUserAgent, self.windowsUserAgent, self.linuxUserAgent]
        return random.choice(web_uas)

    def get_mac_user_agent(self):
        return self.macUserAgent

    def get_windows_user_agent(self):
        return self.windowsUserAgent

    def get_linux_user_agent(self):
        return self.linuxUserAgent

    def get_user_agent(self):
        all_ua = [self.macUserAgent, self.windowsUserAgent, self.linuxUserAgent, self.iPhoneUserAgent]
        self.rand_ua = random.choice(all_ua)
        return self.rand_ua


# print(UserAgents().get_user_agent())
