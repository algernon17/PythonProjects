from random import choice
name = raw_input("What is your name ? ")
age = raw_input("What is your age ? ")
i_age = int(age)
if(i_age < 16):
    age_str = "a young "
elif (i_age < 45):
    age_str = "a middle aged "
else:
    age_str = "an old "
adjectives = ["wet", "big", "damp", "green", "small", "hideous"]
nouns = ["turnip", "dog", "bus", "elephant", "idiot", "molecule"]
message = "Hello " + name + ", you are " + age_str
print(message + choice(adjectives) + " " + choice(nouns) + " !")
