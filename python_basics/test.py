#my random work
#lists
thislist = ["apple", "banana", "cherry", "orange", 23, "melon", "mango"]
print(len(thislist))

print(thislist[2:5]) #prints out the items from index 2 to 5

thislist[1:3] = ["watermelon"]
print(thislist) #changes second and third value by replacing it with one value

thislist.append("orange")
print(thislist) #adds an item in the list

thislist.pop(1)
print(thislist) #removes indexed item

#tuples

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
print(len(months))

month = ("January",)
print(type(month))

date = ('January',23, True, 'March', False, 9)
#print(type(date))

#print(date[2])

#print(months[-4])

#print(months[1:9]) #pull second item onlist to the ninth item on the list

#print(date[2:4])#slice index 2 to index 4

#print(months[-4:-1]) #negative index

y = list(date)
print(type(y))
y[5] = 'False'
print(y)

#counmonths.count(January) #using count
#using index

#dictionaries
#doesnt allow duplicates
today = {
"date" : 9,
"month" : "June",
"year" : 2022
}

#print(today["month"])

#print(today)

print(len(today))

print(type(today))

x = today["month"]
print (today)


today["weather"] = "cool"
print(today)

today.pop("date")
print(today)#removing items