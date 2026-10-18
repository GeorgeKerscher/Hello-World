# Writing to files

from pathlib import Path

path = Path('C:/Users/kersc/OneDrive/Documents/Git/Hello-World/python_work/programming.txt')
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path.write_text(contents)

