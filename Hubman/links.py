import random


class LinkManager:
    def __init__(self):
        self.links = []

    def get_link(self):
        return random.choice(self.links)
