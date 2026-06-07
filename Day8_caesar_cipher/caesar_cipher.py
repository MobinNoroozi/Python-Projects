""" In this program we encode and decode texts by shiffting each letter forward or backward for an inputted shift number"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# crypt function. It takes a text and shift number
def encrypt(original_text, shift_amount):
    cipher_text = ""  #Empty, but will be used to append the shifted text to it
    for letter in original_text:
        if letter in alphabet:
            shift_position = alphabet.index(letter) + shift_amount # Gets the shift number of the letter, then it adds the shift amount to it
            shift_position %= len(alphabet) # Keeps us in bound so we will not get an error
            cipher_text += alphabet[shift_position] # Appends the new letter, letter by letter. 
        else:
            cipher_text += letter # This allows the message to have numbers, symbols, and space in them
    print(f" Here is the encoded result: {cipher_text}")


def decrypt(original_text, shift_amount):
    decoded_text = ""  #Empty, but will be used to append the shifted text to it
    for letter in original_text:
        if letter in alphabet:
            shift_position = alphabet.index(letter) - shift_amount # Gets the shift number of the letter, then it minuses the shift amount to it
            shift_position %= len(alphabet)  # Keeps us in bound so we will not get an error
            decoded_text += alphabet[shift_position] # Appends the new letter, letter by letter. 
        else:
            decoded_text += letter # This allows the message to have numbers, symbols, and space in them
    print(f" Here is the decoded result: {decoded_text}")


# Boolean for the program logic
should_continue = True



while(should_continue):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'quit':\n").lower()

    #quit
    if (direction == "quit"):
        print("Goodbye!")
        should_continue = False
        break
    

    if(direction not in ["encode", "decode"]):
        print("Wrong input. Try again")
        continue
    
        
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    

    if(direction == "encode"):
        encrypt(text, shift)

        go_again = input("Type 'yes' if you want to go again. Type anything else to quit.\n").lower()
        if (go_again == "yes"):
            continue
        else:
            print("Goodbye!")
            should_continue = False
        
        
        
    elif (direction == "decode"):
        decrypt(text, shift)
        go_again = input("Type 'yes' if you want to go again. Type anything else to quit.\n").lower()
        if (go_again == "yes"):
            continue
        else:
            print("Goodbye!")
            should_continue = False

 



