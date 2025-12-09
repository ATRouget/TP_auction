# pylint: disable=missing-docstring
from itertools import count
from auction import Auction
from utils import Cli


class EnglishAuction(Auction):

    def __init__(self, cli=None):
        self.cli = cli if cli else Cli()

    def play(self):
        
        opening_bid = Auction.inputopeningbid(self, 'English')

        bidders = Auction.inputbidders(self)

        # Collect bids
        standing_bid = opening_bid
        winner = None
        initbid = -1
        while initbid != standing_bid :
            initbid = standing_bid
            for bidder in bidders:
                bid = self.cli.prompt(
                    f"Standing bid is {standing_bid}. {bidder} bids:")
                if bid :
                    bid = int(bid)
                    if bid > standing_bid:
                        standing_bid = bid
                        winner = bidder

        Auction.displaywinner(self, winner, standing_bid)




if __name__ == "__main__":
    auction = EnglishAuction()
    auction.play()
