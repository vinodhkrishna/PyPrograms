_author = "Vinodh Krishna Erramachetty Munaswamy"

for i in range(1,11):
    print("Value of i is {0:2}".format(i))

number = "8,999,888,777,666"
for i in range(0,len(number)):
    print(number[i])

for i in range(0,len(number)):
    if number[i] in "0123456789":
        print(number[i])

for i in range(0,len(number)):
    if number[i] in "0123456789":
        print(number[i],end="")
print("")
cleanednumber=""
for i in range(0,len(number)):
    if number[i] in "0123456789":
        cleanednumber = cleanednumber + number[i]
newnumber = int(cleanednumber)
print("Actual integer is {}".format(newnumber))

number1 = "9,111,222,333,444,555,666"
for char1 in number1:
    if char1 in "0123456789":
        print(char1,end="")
print("")

number2 = "1,22,33,44,55,66,77"
constring = ""
for char2 in number2:
    if char2 in "0123456789":
        constring = constring + char2
conintstring = int(constring)
print(conintstring)

for i in range(1,10):
    for j in range(1,5):
        print("Inner Loop")
    print("Outer loop*******")

for i in range(0,101):
    if (i%7 == 0):
        print(i)
# print(i//7)