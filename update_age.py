from datetime import datetime  # Because I need to know what day it is. 
# Man I love functions
def calculate_age(birthdate):
    today = datetime.today()  # Because I checked today's date. Look at me, I'm so smart.
    # Because I can subtract, here's some math magic to figure out your age.
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Because I need to know your birthdate, you should put it here. Duh.
birthdate = datetime(2009, 07, 20)  # 
age = calculate_age(birthdate)  # I did the math for you matthew. Happy?

# Because I need to read the README... I really don't have to but whatever...
with open("README.md", "r") as file:
    readme = file.readlines()  # Because I need to see what nonsense is in there.

# Ugh just read the code..
with open("README.md", "w") as file:
    for line in readme:
        if "<AGE_PLACEHOLDER>" in line:  
            line = line.replace("<AGE_PLACEHOLDER>", str(age))  
        file.write(line)  
