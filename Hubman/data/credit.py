import random


class CreditLinks:
    def __init__(self):
        self.links = ["https://www.equifax.com", "https://www.transunion.com", "https://www.experian.com",
                      "https://www.creditkarma.com", "https://www.myfico.com",
                      "https://www.quizzle.com", "https://www.annualcreditreport.com",
                      "https://www.smartcredit.com",
                      "https://www.creditsesame.com", "https://www.trueidentity.com",
                      "https://www.lifelock.com", "https://www.myprivacymatters.com", "https://www.guardwellid.com"]

    def get_link(self):
        return random.choice(self.links)
