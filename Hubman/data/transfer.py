import random


class TransferLinks:
    def __init__(self):
        self.links = ["https://www.westernunion.com", "https://www.moneygram.com/intl/", "https://www.transferwise.com",
                      "https://www.xoom.com", "https://www.riamoneytransfer.com", "https://www.remitly.com",
                      "https://www.worldremit.com", "https://www.revolut.com", "https://www.paypal.com",
                      "https://www.skrill.com", "https://www.venmo.com", "https://www.payoneer.com",
                      "https://www.travelex.com", "https://www.sendvalu.com",
                      "https://www.instarem.com",
                      "https://www.transfast.com"]

    def get_link(self):
        return random.choice(self.links)
