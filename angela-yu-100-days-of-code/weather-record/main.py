# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
# Can be done as above but the output data will require a lot of cleaning.

# We can use the inbuilt csv package
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)

#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperature = int(row[1])
#             temperatures.append(temperature)

#     print(temperatures)


# Using pandas
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
