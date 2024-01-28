import random


class ClassLinks:
    def __init__(self):
        self.links = ["https://www.udemy.com", "https://www.coursera.org", "https://www.edx.org",
                      "https://www.skillshare.com", "https://www.khanacademy.org", "https://www.linkedin.com/learning",
                      "https://www.pluralsight.com", "https://www.codecademy.com", "https://www.futurelearn.com",
                      "https://www.treehouse.com", "https://www.udacity.com", "https://www.masterclass.com",
                      "https://www.datacamp.com", "https://www.lynda.com", "https://www.simplilearn.com",
                      "https://www.creativelive.com", "https://www.aleks.com", "https://www.memrise.com",
                      "https://www.skillcrush.com", "https://www.brilliant.org"]

    def get_link(self):
        return random.choice(self.links)
