import pandas
import json
import os

dirlist=os.listdir()


#print(dirlist)


print("============= New Execution Json ===============")

dfjson = pandas.read_json("https://pythonhow.com/supermarkets.json" )

print(dfjson)

print("============= New Execution Excel ===============")

df7jason1 = dfjson.set_index("Address")

print(df7jason1)
