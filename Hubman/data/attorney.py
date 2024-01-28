import random


class AttorneyLinks:
    def __init__(self):
        self.links = ["https://www.skadden.com", "https://www.bakerlaw.com", "https://www.jonesday.com",
                      "https://www.dlapiper.com", "https://www.hoganlovells.com", "https://www.whitecase.com",
                      "https://www.kirkland.com", "https://www.sidley.com",
                      "https://www.sullcrom.com", "https://www.paulweiss.com", "https://www.shearman.com",
                      "https://www.clearygottlieb.com", "https://www.weil.com", "https://www.freshfields.com",
                      "https://www.cov.com", "https://www.quinnemanuel.com", "https://www.goodwinlaw.com",
                      "https://www.cooley.com"]

    def get_link(self):
        return random.choice(self.links)
