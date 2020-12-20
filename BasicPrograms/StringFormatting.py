_author = "Vinodh krishna E M"

print("Vinodh age is " + str(32))
print("Vinodh age is {0}".format(32))
print("""Welcome to "Hello" World {0} and python's {1} programs altogether {0}""".format("program", "24"))
#formatting operator is replaced by replacement operator
print("There are {0} days in {1}, {2}, {3}".format(31,"Jan","Mar","May"))
print("There are %d days in %s, %s, %s" %(31, "Jan","Mar","May"))
print(""" There are {0} students in
            Class {1}
            Class {2}""".format(0,1,2))
for i in range(1,12):
    print("{0:2} square is {1:3}".format(i,i**2))
for i in range(1,12):
    print("{0:2} square is {1:<3}".format(i, i**2))
data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[0:-1:5])
