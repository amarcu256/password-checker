
name1= input("Please enter a name: ")
age1 = (input("Please enter " + name1 + "'s age"))

while age1.isdigit() == False:
    age1 = (input("Please enter " + name1 + "'s age - Must be a number. "))

name2= input("Please enter a second name: ")
age2 = input("Please enter " + name2 + "'s age: ")

while age2.isdigit() == False:
    age2 = (input("Please enter " + name1 + "'s age - Must be a number. "))

if (age1>age2):
    difference = int(age1)-int(age2)
    print(name1 + " is " + str(difference) + "years older than " +name2)
else:
    difference = int(age2)-int(age1)
    print(name2 + " is " + str(difference) + " years older than " + name1)