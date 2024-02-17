import random


class TradingLinks:
    def __init__(self):
        self.links = ["https://www.tdameritrade.com", "https://www.etrade.com", "https://www.schwab.com",
                      "https://www.interactivebrokers.com", "https://www.robinhood.com",
                      "https://www.tastyworks.com", "https://www.thinkorswim.com",
                      "https://www.ally.com/invest", "https://www.ig.com", "https://www.fxcm.com",
                      "https://www.oanda.com", "https://www.questrade.com", "https://www.plus500.com",
                      "https://www.cmegroup.com", "https://www.forex.com", "https://www.nadex.com",
                      "https://www.avatrade.com", "https://www.xtb.com"]

    def get_link(self):
        return random.choice(self.links)
