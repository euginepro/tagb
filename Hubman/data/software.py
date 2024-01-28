import random


class SoftwareLinks:
    def __init__(self):
        self.links = ["https://www.microsoft.com", "https://www.apple.com", "https://www.adobe.com",
                      "https://www.oracle.com", "https://www.ibm.com", "https://www.sap.com",
                      "https://www.salesforce.com", "https://www.intuit.com", "https://www.autodesk.com",
                      "https://www.symantec.com", "https://www.avast.com", "https://www.coreldraw.com",
                      "https://www.vmware.com", "https://www.redhat.com", "https://www.dropbox.com",
                      "https://www.box.com", "https://www.slack.com", "https://www.atlassian.com",
                      "https://www.bitdefender.com", "https://www.teamviewer.com"]

    def get_link(self):
        return random.choice(self.links)
