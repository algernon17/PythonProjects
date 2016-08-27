from random import choice
name = raw_input("What is your name ? ")
age = raw_input("What is you age ? ")
i_age = int(age)
if(i_age < 16):
    age_str = " a young "
elif(i_age < 45):
    age_str = " a middle aged "
else:
    age_str = " an old "
adjectives = ["wet", "big", "small", "green", "silly"]
nouns = ["turnip", "dog", "bus", "insect", "hamster"]
print ("Hello " + name +", you are" + age_str + choice (adjectives) + " " + choice(nouns) + " !")
