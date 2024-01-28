import random


class DegreeLinks:
    def __init__(self):
        self.links = ["https://www.collegeboard.org", "https://www.petersons.com", "https://www.princetonreview.com",
                      "https://www.usnews.com/education", "https://www.niche.com/colleges", "https://www.cappex.com",
                      "https://www.chegg.com", "https://www.degreequery.com", "https://www.educationcorner.com",
                      "https://www.educationplanner.org", "https://www.collegedata.com", "https://www.gradreports.com",
                      "https://www.universities.com", "https://www.campusreel.org",
                      "https://www.collegeconfidential.com", "https://www.matchcollege.com",
                      "https://www.collegexpress.com", "https://www.collegesimply.com",
                      "https://www.schoolinks.com"]

    def get_link(self):
        return random.choice(self.links)
