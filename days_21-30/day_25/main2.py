# create a new csv file called "squirrel_count.csv" with
# pandas that looks like this:
'''
,Fur Color,Count
0,grey,2473
1,red,392
2,black,103
'''
import pandas

data = pandas.read_csv("squirrel_data.csv")
gray = 0
red = 0
black = 0
for d in data["Primary Fur Color"]:
    if d == "Cinnamon":
        red += 1
    if d == "Black":
        black += 1
    if d == "Gray":
        gray += 1

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray, red, black]
}

'''
INSTRUCTOR'S SOLUTION:

data = pandas.read_csv("squirrel_data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
'''

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")
