import random

from data.attorney import AttorneyLinks
from data.claim import ClaimLinks
from data.classes import ClassLinks
from data.conference_call import ConferenceCallLinks
from data.credit import CreditLinks
from data.degree import DegreeLinks
from data.donate import DonateLinks
from data.electricity import ElectricityLinks
from data.hosting import HostingLinks
from data.insurance import InsuranceLinks
from data.lawyer import LawyerLinks
from data.loans import LoansLinks
from data.mortgage import MortgageLinks
from data.recovery import RecoveryLinks
from data.rehab import RehabLinks
from data.software import SoftwareLinks
from data.trading import TradingLinks
from data.transfer import TransferLinks
from data.treatment import TreatmentLinks
from data.high_profile import HighLinks


class Rand:
    def __init__(self):
        self.site = "random site"

    def get_other_site_link(self):
        print(self.site)
        link = ""

        dip = random.randint(1, 200)
        if dip == 1:
            link = AttorneyLinks().get_link()
        elif dip == 2:
            link = ClaimLinks().get_link()
        elif dip == 3:
            link = ClassLinks().get_link()
        elif dip == 4:
            link = ConferenceCallLinks().get_link()
        elif dip == 5:
            link = CreditLinks().get_link()
        elif dip == 6:
            link = DegreeLinks().get_link()
        elif dip == 7:
            link = DonateLinks().get_link()
        elif dip == 8:
            link = ElectricityLinks().get_link()
        elif dip == 9:
            link = HostingLinks().get_link()
        elif dip == 10:
            link = InsuranceLinks().get_link()
        elif dip == 11:
            link = LawyerLinks().get_link()
        elif dip == 12:
            link = LoansLinks().get_link()
        elif dip == 13:
            link = MortgageLinks().get_link()
        elif dip == 14:
            link = RecoveryLinks().get_link()
        elif dip == 15:
            link = RehabLinks().get_link()
        elif dip == 16:
            link = SoftwareLinks().get_link()
        elif dip == 17:
            link = TradingLinks().get_link()
        elif dip == 18:
            link = TransferLinks().get_link()
        elif dip == 19:
            link = TreatmentLinks().get_link()
        else:
            link = HighLinks().get_link()

        return link

# print(Rand().get_other_site_link())
