name = input("What is your name?")
print("Hello", name)
age = input("How old are you?")
try:
    # another way to format the print is via f-strings (to be taught)
    print(f"{name}, you were born in {2024 - int(age)}")
    #division = int(age) / 0
except ValueError:
    print("Age must be a valid number")
    print(f"the value that you typed was {age}")
    age = input("try again, how old are you?")
    print(f"{name}, you were born in {2024 - int(age)}")

except ZeroDivisionError:
    print("You can't divide by 0")
except:
    print("I have no idea what else could go wrong")
else:
    print("Thanks for being a good sport")
finally:
    print("Thanks for playing")

