import random


class IOSNameMgr:
    def __init__(self):
        self.ipads = [
            # iPads (iPad Air 3rd gen and newer, iPad 5th gen and newer, all iPad Pro recent gens)
            "iPad 5th generation",
            "iPad 6th generation",
            "iPad 7th generation",
            "iPad 8th generation",
            "iPad 9th generation",
            "iPad 10th generation",
            "iPad Air (3rd generation)",
            "iPad Air (4th generation)",
            "iPad Air (5th generation)",
            "iPad mini (5th generation)",
            "iPad mini (6th generation)",
            "iPad Pro (9.7-inch)",
            "iPad Pro (10.5-inch)",
            "iPad Pro (11-inch) 1st generation",
            "iPad Pro (11-inch) 2nd generation",
            "iPad Pro (11-inch) 3rd generation",
            "iPad Pro (12.9-inch) 1st generation",
            "iPad Pro (12.9-inch) 2nd generation",
            "iPad Pro (12.9-inch) 3rd generation",
            "iPad Pro (12.9-inch) 4th generation",
            "iPad Pro (12.9-inch) 5th generation",
            "iPad Pro (12.9-inch) 6th generation",
            "iPod Touch 7th generation"]
        self.iphones = [  # iPhones (iPhone 8 and newer)
            "iPhone 8",
            "iPhone 8 Plus",
            "iPhone X",
            "iPhone XR",
            "iPhone XS",
            "iPhone XS Max",
            "iPhone 11",
            "iPhone 11 Pro",
            "iPhone 11 Pro Max",
            "iPhone SE (2nd generation)",
            "iPhone 12 mini",
            "iPhone 12",
            "iPhone 12 Pro",
            "iPhone 12 Pro Max",
            "iPhone 13 mini",
            "iPhone 13",
            "iPhone 13 Pro",
            "iPhone 13 Pro Max",
            "iPhone SE (3rd generation)",
            "iPhone 14",
            "iPhone 14 Plus",
            "iPhone 14 Pro",
            "iPhone 14 Pro Max",
            "iPhone 15",
            "iPhone 15 Plus",
            "iPhone 15 Pro",
            "iPhone 15 Pro Max"]
        self.device_models = {
            # iPhones
            "iPhone 8": ["iPhone10,1", "iPhone10,4"],
            "iPhone 8 Plus": ["iPhone10,2", "iPhone10,5"],
            "iPhone X": ["iPhone10,3", "iPhone10,6"],
            "iPhone XR": ["iPhone11,8"],
            "iPhone XS": ["iPhone11,2"],
            "iPhone XS Max": ["iPhone11,4", "iPhone11,6"],
            "iPhone 11": ["iPhone12,1"],
            "iPhone 11 Pro": ["iPhone12,3"],
            "iPhone 11 Pro Max": ["iPhone12,5"],
            "iPhone SE (2nd generation)": ["iPhone12,8"],
            "iPhone 12 mini": ["iPhone13,1"],
            "iPhone 12": ["iPhone13,2"],
            "iPhone 12 Pro": ["iPhone13,3"],
            "iPhone 12 Pro Max": ["iPhone13,4"],
            "iPhone 13 mini": ["iPhone14,4"],
            "iPhone 13": ["iPhone14,5"],
            "iPhone 13 Pro": ["iPhone14,2"],
            "iPhone 13 Pro Max": ["iPhone14,3"],
            "iPhone SE (3rd generation)": ["iPhone14,6"],
            "iPhone 14": ["iPhone14,7"],
            "iPhone 14 Plus": ["iPhone14,8"],
            "iPhone 14 Pro": ["iPhone15,2"],
            "iPhone 14 Pro Max": ["iPhone15,3"],
            "iPhone 15": ["iPhone15,4"],
            "iPhone 15 Plus": ["iPhone15,5"],
            "iPhone 15 Pro": ["iPhone16,1"],
            "iPhone 15 Pro Max": ["iPhone16,2"],

            # iPads
            "iPad 5th generation": ["iPad6,11", "iPad6,12"],
            "iPad 6th generation": ["iPad7,5", "iPad7,6"],
            "iPad 7th generation": ["iPad7,11", "iPad7,12"],
            "iPad 8th generation": ["iPad11,6", "iPad11,7"],
            "iPad 9th generation": ["iPad12,1", "iPad12,2"],
            "iPad 10th generation": ["iPad13,18", "iPad13,19"],

            "iPad Air (3rd generation)": ["iPad11,3", "iPad11,4"],
            "iPad Air (4th generation)": ["iPad13,1", "iPad13,2"],
            "iPad Air (5th generation)": ["iPad13,16", "iPad13,17"],

            "iPad mini (5th generation)": ["iPad11,1", "iPad11,2"],
            "iPad mini (6th generation)": ["iPad14,1", "iPad14,2"],

            "iPad Pro (9.7-inch)": ["iPad6,3", "iPad6,4"],
            "iPad Pro (10.5-inch)": ["iPad7,3", "iPad7,4"],

            "iPad Pro (11-inch) 1st generation": ["iPad8,1", "iPad8,2", "iPad8,3", "iPad8,4"],
            "iPad Pro (11-inch) 2nd generation": ["iPad8,9", "iPad8,10"],
            "iPad Pro (11-inch) 3rd generation": ["iPad13,4", "iPad13,5", "iPad13,6", "iPad13,7"],

            "iPad Pro (12.9-inch) 1st generation": ["iPad6,7", "iPad6,8"],
            "iPad Pro (12.9-inch) 2nd generation": ["iPad7,1", "iPad7,2"],
            "iPad Pro (12.9-inch) 3rd generation": ["iPad8,5", "iPad8,6", "iPad8,7", "iPad8,8"],
            "iPad Pro (12.9-inch) 4th generation": ["iPad8,11", "iPad8,12"],
            "iPad Pro (12.9-inch) 5th generation": ["iPad13,8", "iPad13,9", "iPad13,10", "iPad13,11"],
            "iPad Pro (12.9-inch) 6th generation": ["iPad14,5", "iPad14,6"],

            # iPod Touch
            "iPod Touch 7th generation": ["iPod9,1"]
        }

    def get_ipad_name(self):
        return random.choice(self.ipads)

    def get_iphone_name(self):
        return random.choice(self.iphones)
    def get_device_model(self, device_name):
        pass
