fruits=["apple","banana","orange","cherries"]
for fruit in fruits:
    print("Wouls you like {}".format(fruit))
for number in range(1,11):
    print("Number {}".format(number))

# While loop

temp=40
while temp>32:
    print("Number {}".format(temp))
    temp-=1
    if temp==33:
        break

for number in range(1,11):
    if number==7:
        print(" We are skipping Number {}".format(number))
        continue
    print("This is Number {}".format(number))

for number in range(1,11):
    if number==3:
        pass
    else:
        print("This Number is {}".format(number))