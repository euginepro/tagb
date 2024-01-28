import random


class MortgageLinks:
    def __init__(self):
        self.links = ["https://www.zillow.com/mortgage-rates", "https://www.bankrate.com/mortgages",
                      "https://www.wellsfargo.com/mortgage", "https://www.chase.com/personal/mortgage",
                      "https://www.quickenloans.com/mortgage-rates", "https://www.lendingtree.com/mortgage",
                      "https://www.mortgagecalculator.org", "https://www.mortgagenewsdaily.com",
                      "https://www.redfin.com/mortgage", "https://www.usbank.com/home-loans/mortgage",
                      "https://www.navyfederal.org/loans-cards/mortgage", "https://www.rocketmortgage.com",
                      "https://www.realtor.com/mortgage", "https://www.suntrust.com/home-mortgages",
                      "https://www.mortgagecalculator.org", "https://www.fanniemae.com/singlefamily/mortgage",
                      "https://www.freddiemac.com/pmms", "https://www.mortgagecalculator.net",
                      "https://www.nerdwallet.com/mortgages"]

    def get_link(self):
        return random.choice(self.links)
