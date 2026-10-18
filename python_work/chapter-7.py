# Chapter 7 Input and While


message =input("type something: ")
print(message)


# converting string to an integer

age = input("what is your age? ")
age = int(age)
guess =10
if age ==guess:
    print(age)
# While and break and continue

# While and break and continue
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")