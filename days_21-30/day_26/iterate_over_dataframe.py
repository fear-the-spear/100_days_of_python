# How to iterate over a pandas DataFrame
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key)
    # student
    # score

for (key, value) in student_dict.items():
    print(value)
    # ['Angela', 'James', 'Lily']
    # [56, 76, 98]

# Looping through a data frame
student_data_frame = pandas.DataFrame(student_dict)

# notice the difference when printing the key vs. the value:
for (key, value) in student_data_frame.items():
    print(key)
    # student
    # score


for (key, value) in student_data_frame.items():
    print(value)
    # 0    Angela
    # 1    James
    # 2    Lily
    # Name: student, dtype: object
    # 0    56
    # 1    76
    # 2    98
    # Name: score, dtype: int64

# this isn't particularly useful - it's esentially looping through the names
# of our columns and then printing the data in each column

# this is why pandas has an inbuilt loop called `iterrows` that allows us to
# loop through each of the ROWS of a data frame rather than each of the COLUMNS

# Loop through ROWS of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index)
    # 0
    # 1
    # 2

for (index, row) in student_data_frame.iterrows():
    print(row)
    # student    Angela
    # score          56
    # Name 0, dtype: object
    # student    James
    # score         76
    # Name 1, dtype: object
    # student    Lily
    # score        98
    # Name 2, dtype: object

# each of these rows is a pandas series object, which means we can tap into the
# row and get ahold of the value under a particular column using dot notation
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    # Angela
    # James
    # Lily

for (index, row) in student_data_frame.iterrows():
    print(row.score)
    # 56
    # 76
    # 98

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
        # 56
