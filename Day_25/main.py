# # import csv
# # with open("weather_data.csv","r") as data:
# #     file=csv.reader(data)
# #     temp=[]
# #     for row in file:
# #         if row[1]!="temp":
# #             temp.append(int(row[1]))
# import pandas as pd
# data=pd.read_csv("weather_data.csv")
# print(data["temp"].max())

# print(data[data.temp==data.temp.max()])

# Monday=data[data.day=="Monday"]
# print(Monday.temp*9/5+32)

import pandas as pd
data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
summary=data.groupby("Primary Fur Color").count()
print(summary)