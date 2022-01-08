from sys import argv

script,user_name=argv
prompt='>'

print("Hi {}, I'm the {} script.".format(user_name,script))
print("I'd like to ask you a few questions.")
print("Do like me,{}?".format(user_name))
likes=input()

print("Where do you live, ",user_name,"?")
lives=input()

print("What kind of computer do you have?")
computer=input()

print("""
Aright,so you said {} about liking me.
You live in {}. Not sure where that is.
And you have a {} computer. Nice
""".format(likes,lives,computer))

"""
输入:python ex14.py l
输出:
Hi l, I'm the ex14.py script.
I'd like to ask you a few questions.
Do like me,l?
yes
Where do you live,  l ?
nj
What kind of computer do you have?
lenovo

Aright,so you said yes about liking me.
You live in nj. Not sure where that is.
And you have a lenovo computer. Nice
"""