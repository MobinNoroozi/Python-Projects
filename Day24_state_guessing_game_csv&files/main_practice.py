"""import csv #Importing csv helper

with open("./weather_data.csv") as data_file:
    data = csv.reader(data_file) #This reads csv files
    
    temperatures = [] #Create a list and we add to it

    for row in data: #For every row in data
        if row[1] != "temp": #Get the temperature, but not the lable
            temperatures.append(int(row[1]))

print(temperatures)

USING PANDA IS EASIER 👇👇👇
"""

"""
import pandas

data = pandas.read_csv("./weather_data.csv")


dicts = data.to_dict()
print(dicts)

lists = data["temp"].to_list()
print(lists)"""



import pandas
data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

num_gray = len(data[data["Primary Fur Color"] == "Gray"])
num_black = len(data[data["Primary Fur Color"] == "Black"])
num_cin = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(num_black)
print(num_cin)
print(num_gray)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [num_gray, num_cin, num_black]

}

df = pandas.DataFrame(data_dict)
df.to_csv("squirl_count.csv")
