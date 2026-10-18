# Reading from files
from  pathlib import Path
path = Path('C:/Users/kersc/OneDrive/Documents/Git/Hello-World/python_work/py_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)
print("break in the program here.")
lines = contents.splitlines()
for line in lines:
    print(line)
