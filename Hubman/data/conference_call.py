import random


class ConferenceCallLinks:
    def __init__(self):
        self.links = ["https://www.zoom.us", "https://www.microsoft.com/en-us/microsoft-365/microsoft-teams",
                      "https://www.webex.com", "https://www.gotomeeting.com", "https://www.bluejeans.com",
                      "https://www.skype.com", "https://www.join.me", "https://www.freeconferencecall.com",
                      "https://www.uberconference.com", "https://www.ringcentral.com", "https://www.anymeeting.com",
                      "https://www.startmeeting.com", "https://www.on24.com",
                      "https://www.eztalks.com", "https://www.clickmeeting.com",
                      "https://www.callbridge.com", "https://www.fuze.com", "https://www.loopup.com"]

    def get_link(self):
        return random.choice(self.links)
