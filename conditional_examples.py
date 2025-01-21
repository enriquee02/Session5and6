from random import choice


# virtual bartendeer
drinks = ("vodka ", "tequila", "rum", "whiskey", "sake", "rakja", "gin")
print("welcome to La Chimenea online")
name = input("I will be your bartender today, what is yor name?")
try:
    age = input(f"How old are you, {name}?")
    age = int(age)
    if age >=21:
        legal = True
    elif age < 16:
        legal = False
    else:
        country = input(f"where are you from, {name}?")
        legal = False
    elif age >= 18 and country != "USA":
        legal = True
    elif age >= 16 and country == "Luxembourg":
        legal = True
    else:
        print("you are not allowed to drink")
    if age > 120 or age < 5
        print("please do not lie to me")
    elif legal:
        print("You are allowed to drink")
        print(f"Here is a {choice(drinks)} for you")
    else:
        print(f"unfortunatley {name}, I am not allowed to get you a drink")

except ValueError:
    print("please give a valid age")



