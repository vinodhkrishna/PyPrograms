_author = "Vinodh krishna"


shopping_list = ["milk", "eggs", "rice", "pasta"]

for item in shopping_list:
    print(item)

for item in shopping_list:
    if item == "eggs":
        continue
    else:
        print(item)

for item in shopping_list:
    if item == "rice":
        break
    print(item)

print("Vinodh Krishna")
for item in shopping_list:
    if item == "eggs":
        break
else:
    print(item)