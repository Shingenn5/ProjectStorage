age = int(input("Please enter your age: "))
print(age)
if age >= 21:
    print("What kind of beer would you like?")
    beer = input("We have Bud, Coors, and Miller. ")
    print("Here is your " + beer + ". Enjoy!")
else:
    print("You are underage, go home!")
