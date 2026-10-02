# This program is a practice to use variables  and lists up to chapter 3 in the Crash course 3rd edition

 # Angels and Riff Names
angels = ['mary', 'gail', 'murph', 'jeannie', 'carol']
riffraff=['tim', 'george', 'bob', 'jud']

print(angels[0])
couple = f"One couple is {riffraff[0].title()} and {angels[3].title()}."

print(couple)
print(len(riffraff))
for friend in riffraff:
    print(friend)
    print("george")

# working with range and exponents **

for value in range(1, 6):
    print (value)

numbers =list(range(1, 6))
print(numbers[2])
print(numbers)
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
