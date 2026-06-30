placeholder = "[name]"

with open("./Input/Names/invited_names.txt") as file:
    name_for_files = file.readlines()
    print(name_for_files)

with open("./Input/Letters/starting_letter.txt") as file:
    content = file.read()
    for name in name_for_files:
        stripped_name = name.strip()
        new_letter = content.replace(placeholder, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode= "w") as letter:
            letter.write(new_letter)
      



