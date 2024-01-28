import random


class DonateLinks:
    def __init__(self):
        self.links = ["https://www.gofundme.com", "https://www.indiegogo.com", "https://www.kickstarter.com",
                      "https://www.patreon.com", "https://www.justgiving.com",
                      "https://www.charitynavigator.org", "https://www.globalgiving.org",
                      "https://www.crowdfunder.co.uk", "https://www.causes.com", "https://www.crowdrise.com",
                      "https://www.donorschoose.org", "https://www.giveindia.org",
                      "https://www.mightycause.com",
                      "https://www.chuffed.org", "https://www.fundly.com", "https://www.classy.org"]

    def get_link(self):
        return random.choice(self.links)
