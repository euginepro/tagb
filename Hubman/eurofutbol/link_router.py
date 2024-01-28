import random


class Router:
    def __init__(self):
        self.searches = ["https://www.google.com/search?q=Attorneys",
                         "https://www.google.com/search?q=Claims",
                         "https://www.google.com/search?q=Classes+Online",
                         "https://www.google.com/search?q=Conference+call",
                         "https://www.google.com/search?q=Credit+Companies",
                         "https://www.google.com/search?q=Degree+Online",
                         "https://www.google.com/search?q=Donate",
                         "https://www.google.com/search?q=Electricity",
                         "https://www.google.com/search?q=Hosting",
                         "https://www.google.com/search?q=Insurance+Quotes",
                         "https://www.google.com/search?q=Lawyers+Websites",
                         "https://www.google.com/search?q=Loans",
                         "https://www.google.com/search?q=Mortgage",
                         "https://www.google.com/search?q=Recovery",
                         "https://www.google.com/search?q=Rehab",
                         "https://www.google.com/search?q=Software+Companies",
                         "https://www.google.com/search?q=Trading",
                         "https://www.google.com/search?q=Transfer+Websites"
                         "https://www.google.com/search?q=Treatment+Websites"]

    def get_search_link(self):
        return random.choice(self.searches)
