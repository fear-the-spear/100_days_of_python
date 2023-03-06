# working with csv in python
import csv  # read and write
import pandas  # more complex operations made easier

# put a single column of data (the temps) into a new list with 'csv'
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    tempuratures = []
    for row in data:
        if row[1] != 'temp':
            tempuratures.append(int(row[1]))
    print(tempuratures)

# do the same thing, but with pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])

# that was much easier, and we didn't even need to append
# any data to a new list

# more work with pandas
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# CHALLENGE: calculate the avg. temps in the list
avg = round(sum(temp_list) / len(temp_list), 1)
print(avg)

# or, you can do this:
avg = data["temp"].mean()
print(avg)

# CHALLENGE: get ahold of the max temp by using a pandas series method
print(data["temp"].max())

# pandas converts column headings into attributes!
print(data.temp)

# get data in rows
print(data[data.day == "Monday"])  # <- 0  Monday  12  Sunny

# CHALLENGE: pull out row of data where temp was at maximum
print(data[data.temp == data.temp.max()])  # <-- 6  Sunday  24  Sunny

# get single value from row that matches criteria
monday = data[data.day == "Monday"]
print(monday.condition)

# CHALLENGE: convert Monday's temp into fahrenheit
monday = data[data.day == "Monday"]
celcius_temp = monday.temp
fahrenheit_temp = ((celcius_temp * (9 / 5)) + 32)
print(fahrenheit_temp)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela", "Dakota"],
    "scores": [76, 56, 65, 99]
}

data = pandas.DataFrame(data_dict)
# create a csv file from that data
data.to_csv("new_data.csv")
