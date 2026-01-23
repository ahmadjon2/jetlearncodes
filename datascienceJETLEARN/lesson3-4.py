import pandas as pd

dictionary = {"name":["Ahmadjon","Shobhit"],"age":[14,18],"country":["Uzbekistan","India"]}
print(type(dictionary))
data1 = pd.DataFrame(dictionary)
print(type(data1))

data = pd.read_csv("titanic.csv")
print(data)
print(data.info())
print(data.shape)
print(data.describe())
print(data.tail(10))
print(data.dtypes)
print(data[["Age","Name"]])

# filtering rows

print(data[data["Age"] < 18]) 
print(data[data["Sex"] == "male" ]) 
print(data[(data["Sex"] == "male") | (data["Age"] < 18)])

#counting

print(data["Pclass"].value_counts())
print(data["Sex"].value_counts())
print(data["Survived"].value_counts())