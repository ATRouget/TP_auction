# pylint: disable=missing-docstring
from itertools import count

from utils import Cli


class EnglishAuction():

    def __init__(self, cli=None):
        self.cli = cli if cli else Cli()

    def play(self):
        # Input opening bid
        self.cli.display('Started auction of type: English')
        opening_bid = self.cli.prompt('Please enter the amount for the opening bid:')
        opening_bid = int(opening_bid)
        self.cli.display(f"Opening bid is: {opening_bid}")

        # Input bidders
        bidders = []
        for index in count(1):
            bidder = self.cli.prompt(
                f"Enter name for bidder {index} (enter nothing to move on):"
            )
            if not bidder:
                break
            bidders.append(bidder)
        self.cli.display(f"\nBidders are: {', '.join(bidders)}\n")

        # Collect bids
        standing_bid = opening_bid
        winner = None
        while len(bidders) > 1 :
            new = []
            for ibidder in range(len(bidders)):
                bid = self.cli.prompt(
                    f"Standing bid is {standing_bid}. {bidders[ibidder]} bids:")
                if bid :
                    bid = int(bid)
                    if bid > standing_bid:
                        standing_bid = bid
                        winner = bidders[ibidder]
                        new.append(winner)
            bidders = new

        # Display winner
        self.cli.display("\n~~~~~~~~\n")
        self.cli.display(f"Winner is {winner}. Winning bid is {standing_bid}.")



if __name__ == "__main__":
    auction = EnglishAuction()
    auction.play()
