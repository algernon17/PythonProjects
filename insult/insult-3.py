from random import choice
adjectives = ["wet", "big", "damp", "green", "small", "hideous"]
nouns = ["turnip", "dog", "bus", "elephant", "idiot", "molecule"]

def print_insult(username, age_val):
    adj = choice(adjectives)
    noun = choice(nouns)
    if(age_val < 16):
        age_str = "a young "
    elif (age_val < 45):
        age_str = "a middle aged "
    else:
        age_str = "an old "
    message = "Hello " + name + ", you are " + age_str + adj + " " + noun + " !"
    print(message)

name = raw_input("What is your name ? ")
age = raw_input("What is your age ? ")
print_insult(name, int(age))
for item in adjectives:
    print(item)
for item in nouns:
    print(item)
for count in [15, 44, 45]:
    print_insult(name, count)
print(list(range(10)))
for count in range(14,18):
    print_insult(name, count)
userAnswer=""
while(userAnswer !="no"):
    print_insult(name, int(age))
    userAnswer=raw_input("can you take any more ? [no] ")
print("So you've had enough !!")
                         
