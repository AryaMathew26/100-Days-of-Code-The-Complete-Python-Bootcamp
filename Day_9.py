from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print('Welcome to the secret auction program.')

def find_highest_bid(bidding_record):
  highest_bid=0
  for bidder in bidding_record:
    if bidding_record[bidder]>highest_bid:
      highest_bid=bidding_record[bidder]
      highest_bidder=bidder
  print(f"The highest bidder is {highest_bidder} who bid {highest_bid}")

other_bidders=True
blind_bid={}
while other_bidders:
  name=input("What is your name?")
  bid=int(input("What's your bid?"))
  blind_bid[name]=bid
  others=input("Are there any other bidders? Type 'yes' or 'no'.")
  if others=='no':
    other_bidders=False
    find_highest_bid(blind_bid)
  elif others=='yes':
    clear()
