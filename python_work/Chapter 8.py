# Chapter 8
# Greetings
def greet_people(names):
    """Say hi to all people in list"""
    for person in names:
        message = (f"Hello, {person.title()}!")
        print(message)

angels = ["carol", "gail", "murph", "mary", "jeannie"]
riffraff = ["bob", "george", "jud", "tim"]

# greet_people(angels)
greet_people(angels[:])
greet_people(riffraff)