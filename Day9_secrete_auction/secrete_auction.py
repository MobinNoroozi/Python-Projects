from art import logo
print(logo)

def clear_screen():
    print("\n" * 500) # Clears the screen so they cannot see each others bid

# Empty, but this doctonary hold our bidders and bids
bid = {}

name = input("what is your name: ")
price = float(input("what is your bid?  $"))


bid[name] = price # Adds the bidder and their proce to the dicionary


should_continue = True
while (should_continue):
    clear_screen()

    
    more_bidder = input("Are there other bidder? type 'yes' or 'no':  ").lower()

    if (more_bidder == "no"):
        print("\n" * 500) # Clears the screen so they cannot see each others bid
        max_bid = 0 #Max bidd
        final_key = "" # Name of the bidder with highest bid
        for key in bid:
            if (bid[key] >= max_bid):
                max_bid = bid[key]
                final_key = key
        print(bid)
        print(f"Highest bid belongs to '{final_key}' with bid of ${bid[final_key]}")
        should_continue = False

    elif (more_bidder == "yes"):
        clear_screen()
        name = input("what is your name: ")
        price = float(input("what is your bid?  $"))
        bid[name] = price

    else:
        continue
