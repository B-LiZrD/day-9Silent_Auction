# silent_auction.py
import art
logo = art.logo


auction_dict = {}

loop = True
while loop:
  print(logo)
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  auction_dict[name] = bid
  bidders = input("Are there any other bidders? 'Yes' or 'No' ").lower()
  if bidders == "no":
    loop = False


def winner(dictionary):
  highest_number = -1
  winner = ""
  for key in dictionary:
    bid_amount = dictionary[key]
    if bid_amount > highest_number:
      highest_number = bid_amount
      winner = key
  print(f"The winner is {winner} with the bid of ${highest_number}")


winner(auction_dict)