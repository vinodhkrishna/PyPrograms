_author = "Vinodh Krishna Erramachetty Munaswamy"

print("You need to provide your age")
# age = int(input("Enter your age here"))
age = 16

if age <=16:
    print("You are too young to vote")
else:
    print("You can vote")


if age <=16:
    print("You are too young to vote")
elif age >16 and age <=74:
    print("Right time to vote")
else:
    print("No need to vote")



if 16 <= age <=65:
    print("You can vote")
else:
    print("Don't vote")

#no boolean datatypes. just TRUE or FALSE constants

if (age>16) or (age <=64):
    print("You can vote")
else:
    print("You cannot vote")


print("""0 {}, 1 none {}, 2 0.0 {}, 3 list {}, 4 tuple {}""".format(bool(0), bool(None), bool(0.0), bool([]), bool({})))

X= input("Enter the value")

if X:
    print("You entered value of " + X)
    print("You entered {}". format(X))
else:
    print("nothing entered")

if not X:
    print("You entered value of " + X)
    print("You entered {}". format(X))
else:
    print("nothing entered")


parrot = "Norweigen Bird"
Y = input("Enter the required letter")

# if Y not in parrot:
if Y not in parrot:
    print("Letter " + Y + " is in parrot")
else:
    print("Letter {0} is not in parrot".format(Y))