import random


class InsuranceLinks:
    def __init__(self):
        self.links = ["https://www.insurance.com", "https://www.insure.com", "https://www.policygenius.com",
                      "https://www.everquote.com", "https://www.insurify.com",
                      "https://www.coverhound.com", "https://www.gabi.com", "https://www.quotesmatch.com",
                      "https://www.smartfinancial.com", "https://www.netquote.com",
                      "https://www.einsurance.com", "https://www.compare.com",
                      "https://www.carinsurance.com", "https://www.iselect.com.au",
                      "https://www.insurancehotline.com", "https://rates.ca/"]

    def get_link(self):
        return random.choice(self.links)
