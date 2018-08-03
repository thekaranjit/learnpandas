import pandas
import json
import os

dirlist=os.listdir()


#print(dirlist)

print("============= New Execution ===============")

df = pandas.read_csv("C:\\Users\Karanjit Singh\\Desktop\\Programing Course\\Python\\Pyhon Mega Course\\course\\pandas\learnpandas\\data.csv")

#print(df)

print("============= New Execution ===============")


dfcsv = pandas.read_csv("data.csv")

#print(dfcsv)

print("============= New Execution CSV ===============")

dfcsvwheader = pandas.read_csv("data.csv", header=None)

print(dfcsvwheader)

print("============= New Execution CSV ===============")

dfcsvwid = pandas.read_csv("data.csv")

dfcsvwid.set_index('ID')

print(dfcsvwid)


print("============= New Execution Json ===============")

dfjson = pandas.read_json("data.json" )

dfjson.set_index("ID")
print(dfjson)



print("============= New Execution Excel ===============")

dfxls = pandas.read_excel("data.xlsx", sheet_name=0 )

dfxls2 = dfxls.set_index("ID")
print(dfxls2)

print("============= New Execution TXT by comma ===============")

dfbycomma = pandas.read_csv("datacomma.txt")

dfbycomma2 = dfbycomma.set_index("ID")
print(dfbycomma2)

print("============= New Execution TXT by SemiColom ===============")

dfbysemi = pandas.read_csv("datasemi.txt", sep = ";")

dfbysemi2 = dfbysemi.set_index("ID")
print(dfbysemi2)



print("============= New Execution grab from Web ===============")

dfweb = pandas.read_csv("https://pythonhow.com/supermarkets.csv")

dfweb2 = dfweb.set_index("ID")
print(dfweb2)
