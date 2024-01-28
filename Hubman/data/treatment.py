import random


class TreatmentLinks:
    def __init__(self):
        self.links = ["https://www.mayoclinic.org", "https://www.webmd.com", "https://www.clevelandclinic.org",
                      "https://www.medlineplus.gov", "https://www.health.harvard.edu",
                      "https://www.johnshopkinsmedicine.org", "https://www.medicinenet.com", "https://www.medscape.com",
                      "https://www.nhs.uk", "https://www.patient.info", "https://www.everydayhealth.com",
                      "https://www.healthline.com", "https://www.emedicinehealth.com", "https://www.aafp.org",
                      "https://www.cancer.org", "https://www.who.int", "https://www.ncbi.nlm.nih.gov",
                      "https://www.mind.org.uk", "https://www.psychologytoday.com", "https://www.arthritis.org"]

    def get_link(self):
        return random.choice(self.links)
