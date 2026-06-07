from art import logo, vs
from game_data import data
import random
print(logo)
score = 0

while(True):
    A = random.choice(data)
    print(f"Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}.")
    A_follower = A["follower_count"]


    print(vs)


    B = random.choice(data)
    print(f"Against B: {B["name"]}, a {B["description"]}, from {B["country"]}.")
    B_follower = B["follower_count"]


    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    if(guess == "a"):
        if(B_follower > A_follower):
            score += 1
            print(f" You are right. Current score: {score}")
        else:
            print(f"Sorry that was wrong! Final score: {score}")
            break
    elif(guess == "b"):
        if(A_follower > B_follower):
            score += 1
            print(f" You are right. Current score: {score}")
        else:
            print(f"Sorry that was wrong! Final score: {score}")
            break
           


    