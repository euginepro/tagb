import random


class LawyerLinks:
    def __init__(self):
        self.links = ["https://www.skadden.com", "https://www.lw.com", "https://www.dlapiper.com",
                      "https://www.whitecase.com", "https://www.jonesday.com", "https://www.klgates.com",
                      "https://www.hoganlovells.com", "https://www.bakermckenzie.com", "https://www.sidley.com",
                      "https://www.shearman.com", "https://www.sullcrom.com", "https://www.freshfields.com",
                      "https://www.wilmerhale.com", "https://www.paulweiss.com", "https://www.gibsondunn.com",
                      "https://www.clearygottlieb.com",
                      "https://www.simpsonthacher.com", "https://www.linklaters.com", "https://www.cliffordchance.com"]

    def get_link(self):
        return random.choice(self.links)
