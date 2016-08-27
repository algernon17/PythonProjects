from random import choice

def print_message(username, age_val, adj, noun):
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
adjectives = ["wet", "big", "damp", "green", "small", "hideous"]
nouns = ["turnip", "dog", "bus", "elephant", "idiot", "molecule"]
print_message(name, int(age), choice(adjectives), choice(nouns))
