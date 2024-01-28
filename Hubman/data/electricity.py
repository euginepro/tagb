import random


class ElectricityLinks:
    def __init__(self):
        self.links = ["https://www.reliant.com", "https://www.directenergy.com",
                      "https://www.constellation.com", "https://www.ambitenergy.com", "https://www.nrg.com",
                      "https://www.griddy.com", "https://www.gexaenergy.com",
                      "https://www.greenmountainenergy.com", "https://www.cirroenergy.com",
                      "https://www.firstchoicepower.com", "https://www.bounceenergy.com",
                      "https://www.4changeenergy.com",
                      "https://www.sparkenergy.com", "https://www.xoomenergy.com"]

    def get_link(self):
        return random.choice(self.links)
