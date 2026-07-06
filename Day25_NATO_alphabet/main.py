import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

my_dic = {} #Creating an empty dictionary for now

"""The data.iterrows() gives us index and the row of data. But I do not need the index
   So I assign the key and value of each
"""
for (_, row) in data.iterrows():
    my_dic[row.letter.lower()] = row.code #Make it a lower case so I can compare even if the user messes up 


word = input("Enter the word: ").lower() #Get the input and lower it so I can compare correctly

my_list = []

for letter in word:
    if letter in my_dic:
        my_list.append(my_dic[letter])

print(my_list)