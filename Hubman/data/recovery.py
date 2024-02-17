import random


class RecoveryLinks:
    def __init__(self):
        self.links = ["https://www.mentalhealthamerica.net", "https://www.samhsa.gov",
                      "https://www.psychcentral.com", "https://www.addictioncenter.com",
                      "https://www.thehotline.org",
                      "https://www.anxiety.org", "https://www.aa.org",
                      "https://www.smartrecovery.org", "https://www.eatingdisorderhope.com",
                      "https://www.livestrong.org",
                      "https://www.debtorsanonymous.org",
                      "https://www.creditkarma.com/"]

    def get_link(self):
        return random.choice(self.links)
