import random


class RehabLinks:
    def __init__(self):
        self.links = ["https://www.hazeldenbettyford.org",
                      "https://www.promisesbehavioralhealth.com", "https://www.therecoveryvillage.com",
                      "https://www.sunshinebehavioralhealth.com", "https://www.rehabs.com",
                      "https://www.treatmentadvocacycenter.org", "https://www.addictioncenter.com",
                      "https://www.sobernation.com", "https://www.luxuryrehabs.com",
                      "https://www.therapyroute.com", "https://www.addictionhope.com",
                      "https://www.alcoholrehabguide.org", "https://www.recoveryconnection.com",
                      "https://www.psycom.net",
                      "https://www.addictionrehabcenters.com", "https://www.drugrehab.com",
                      "https://www.addictionresource.com"]

    def get_link(self):
        return random.choice(self.links)
