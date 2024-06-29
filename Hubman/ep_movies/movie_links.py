import random


class MoviesLinkManager:
    def __init__(self):
        self.links = ["https://m.eurofutbol.xyz/p/top-earning-and-money-tips.html",
                      "https://m.eurofutbol.xyz/p/top-law-tips.html"]

    def get_link(self):
        return random.choice(self.links)
