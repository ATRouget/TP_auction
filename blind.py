# pylint: disable=missing-docstring

from itertools import count

# CLI = Command Line Interface
from utils import Cli

from auction import Auction


class BlindAuction(Auction):

    def __init__(self, cli=None):
        self.cli = cli if cli else Cli()

    def play(self):
        opening_bid = Auction.inputopeningbid(self, 'Blind')

        bidders = Auction.inputbidders(self)

        # Collect bids
        standing_bid = opening_bid
        winner = None
        for bidder in bidders:
            bid = self.cli.prompt(
                f"Opening bid is {opening_bid}. {bidder} bids:"
            )
            bid = int(bid)
            if bid > standing_bid:
                standing_bid = bid
                winner = bidder

        # Display winner
        self.cli.display("\n~~~~~~~~\n")
        self.cli.display(f"Winner is {winner}. Winning bid is {standing_bid}.")


if __name__ == "__main__":
    auction = BlindAuction()
    auction.play()
