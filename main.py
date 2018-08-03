import pandas

df1 = pandas.DataFrame([[2,4,6],[10,20,30]])

print("DF1 Result is")
print(df1)

print("============= New Execution ===============")


df2 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"])

print("DF2 Result is")
print(df2)

print("============= New Execution ===============")

df3 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"],index=["First","Second"])

print("DF3 Result is")
print(df3)

print("============= New Execution ===============")

df4 = pandas.DataFrame([{"Name":"John"},{"Name":"Jack"}])

print("DF4 Result is")
print(df4)

print("============= New Execution ===============")

df5 = pandas.DataFrame([{"Name":"John", "Surname":"Man"},{"Name":"Jack","Surname":"Man"}])

print("DF5 Result is")
print(df5)

print("============= New Execution ===============")


# Calculate mean of DF1

meandf1 = df1.mean()

print("Mean of DF1 is: ", meandf1)

print("============= New Execution ===============")


df2age = df2.Age

print(df2age)



