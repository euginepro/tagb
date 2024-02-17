import random


class LoansLinks:
    def __init__(self):
        self.links = ["https://www.bankrate.com", "https://www.lendingtree.com", "https://www.quickenloans.com",
                      "https://www.wellsfargo.com/personal-loans", "https://www.lightstream.com",
                      "https://www.sofi.com", "https://www.prosper.com",
                      "https://www.avant.com", "https://www.lendingclub.com",
                      "https://www.fundingcircle.com",
                      "https://www.penfed.org", "https://www.discover.com/personal-loans", "https://www.navient.com",
                      "https://www.marinerfinance.com", "https://www.suntrust.com/loans/personal-loans",
                      "https://www.td.com/", "https://www.towerloan.com",
                      "https://www.usbank.com/", "https://www.Upgrade.com",
                      "https://www.zionsbank.com/", "https://www.arrowheadcu.org/",
                      "https://www.firsttechfed.com", "https://www.citizensbank.com/",
                      "https://www.marcus.com/us/en", "https://www.titlemax.com",
                      "https://www.bluevine.com", "https://www.kabbage.com",
                      "https://www.evenfinancial.com",
                      "https://www.payoff.com", "https://www.lendingpoint.com", "https://www.bestegg.com",
                      "https://www.monevo.com", "https://www.lendup.com", "https://www.self.inc",
                      "https://www.figure.com",
                      "https://www.flexwage.com", "https://www.stilt.com",
                      "https://www.rategenius.com", "https://www.greenlightloans.com",
                      "https://www.lendvious.com", "https://www.myclimb.com", "https://www.ondeck.com",
                      "https://www.kabbage.com",
                      "https://www.loansolutionsnow.com",
                      "https://www.lendingone.com", "https://www.fundation.com",
                      "https://www.heartlandpaymentsystems.com", "https://www.lendistry.com",
                      "https://www.quickspark.com",
                      "https://www.paypal.com/",
                      "https://www.nav.com",
                      "https://www.rapidfinance.com",
                      "https://www.expresscapitalfinancing.com",
                      "https://www.zipcapitalgroup.com", "https://www.mulliganfunding.com",
                      "https://www.forwardline.com", "https://www.fundingwellcapital.com",
                      "https://www.sba7a.loans",
                      "https://www.lendgenius.com",
                      "https://www.finimpact.com", "https://www.lendistry.com", "https://www.factorfunding.com",
                      "https://www.fundera.com"]

    def get_link(self):
        return random.choice(self.links)
