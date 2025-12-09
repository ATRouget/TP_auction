# pylint: disable=missing-docstring

from itertools import count

# CLI = Command Line Interface
from utils import Cli

class Auction():

    def __init__(self, cli=None):
        self.cli = cli if cli else Cli()

    def inputbidders(self) :
        bidders = []
        for index in count(1):
            bidder = self.cli.prompt(
                f"Enter name for bidder {index} (enter nothing to move on):"
            )
            if not bidder:
                break
            bidders.append(bidder)
        self.cli.display(f"\nBidders are: {', '.join(bidders)}\n")
        return bidders
    
    def inputopeningbid(self, auctiontype):
        self.cli.display(f'Started auction of type: {auctiontype}')
        opening_bid = self.cli.prompt('Please enter the amount for the opening bid:')
        opening_bid = int(opening_bid)
        self.cli.display(f"Opening bid is: {opening_bid}")
        return opening_bid
    
    def displaywinner(self, winner, sbid):
        self.cli.display("\n~~~~~~~~\n")
        self.cli.display(f"Winner is {winner}. Winning bid is {sbid}.")


