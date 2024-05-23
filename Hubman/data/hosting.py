import random


class HostingLinks:
    def __init__(self):
        self.links = ["https://www.bluehost.com", "https://www.siteground.com", "https://www.hostgator.com",
                      "https://www.inmotionhosting.com", "https://www.a2hosting.com", "https://www.dreamhost.com",
                      "https://www.greengeeks.com", "https://www.kinsta.com", "https://www.wpengine.com",
                      "https://www.hostinger.com", "https://www.cloudways.com", "https://www.liquidweb.com",
                      "https://www.iPage.com", "https://www.1and1.com", "https://www.namecheap.com/hosting",
                      "https://www.fastcomet.com", "https://www.scalahosting.com", "https://www.webhostingcom",
                      "https://www.hostpapa.com", "https://www.flywheel.com"]

    def get_link(self):
        return random.choice(self.links)
