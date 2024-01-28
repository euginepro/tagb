import random


class ClaimLinks:
    def __init__(self):
        self.links = ["https://www.morganandmorgan.com", "https://www.forthepeople.com",
                      "https://www.friedmanrubin.com", "https://www.hg.org", "https://www.johnfoy.com",
                      "https://www.levinlaw.com", "https://www.lawyernc.com",
                      "https://www.sokolovelaw.com", "https://www.zehllaw.com", "https://www.burgsimpson.com",
                      "https://www.shookandstone.com", "https://www.berginjurylawyers.com", "https://www.kuzyklaw.com",
                      "https://www.kislingnestico.com", "https://www.dolmanlaw.com", "https://www.knrlegal.com",
                      "https://www.nbalawfirm.com", "https://www.willenslaw.com"]

    def get_link(self):
        return random.choice(self.links)
