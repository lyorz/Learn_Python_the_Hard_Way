"""
原本试图分模块进行
将所有除main以外的函数写入了game_function.py文件
但导入以后不能使用，报错attributeerror，暂时不知道为什么
所以将所有函数写入了同一个文件
"""

def start_function():
    """初始场景描述"""
    print("""
    When you woke up, you found that you were in the woods.
    \nThere is light in front of you, and behind you is black fog.
    \nWhat do you want to do now?
    """)

def go_straight():
    """0.前进"""
    print("""
    You choose to go straight.
    \nBut you find there are four road.
    \nWhat do you want to do now?
    """)

def walk_back():
    """0.后退"""
    print("""
    You feel walking foreward is dangerous, so you choose to go back.
    \nIt seems to be something in the fog that makes you feel sleepy.
    \nYou go insensible soon.
    """)
    main()

def werewolf():
    """1.狼人"""
    print("""
    You choose the first road, and you see there is a werewolf staring at you with red eyes.
    \nIt looks at you and ask you a question.
    """)

def vampire():
    """2.吸血鬼"""
    print("""
    You choose the second road, and you see there is a vampire drinking blood of a dead person.
    \nIt looks at you and ask you a question.
    """)

def ghost():
    """3.幽灵"""
    print("""
    You choose the third road, and you see a ghost. It is saying something you can't hear clearly.
    \nYou go closely, and hearing it is saying,"I'm hungry...hungry..."
    \nIt looks at you and ask you a question.
    """)

def ghoul():
    """4.食尸鬼"""
    print("""
    You choose the fourth road, and you see a ghoul eating someone's body.
    \nIt looks at you and ask you a question.
    """)

questions=[
    "What is the shape of today's moon?",
    "What taste is your blood?",
    "Do you know who killed me?",
    "AbaAba?"
]

def ask_question(i):
    print(questions[i])
    return input()

def answer_weewolf(answer):
    if answer=="circle":
        print("The weewolf becames angry, and scratch your face.")
    elif answer=="i don't know":
        print("The weewolf runs away.")
    else:
        print("The weewolf don't understand, and scratch your face.")

def answer_vampire(answer):
    if answer=="sweet":
        print("The vampire seems to be interested, and bites your throat.")
    elif answer=="i don't know":
        print("The vampire runs away.")
    else:
        print("The vampire don't understand, and bites your throat. ")

def answer_ghost(answer):
    if answer=="i don't know":
        print("The ghost becomes angry and take your head off.")
    else:
        print("The ghost flys away.")

def answer_ghoul(answer):
    if answer=="abaaba":
        print("The ghoul becomes very happy, and ran away.")
    else:
        print("The ghoul eat you brain!")



def main():
    print("""
    When you woke up, you found that you were in the woods.
    \nThere is light in front of you, and behind you is black fog.
    \nWhat do you want to do now?
    """)
    choice1=input(">")
    if choice1 =="go straight":
        go_straight()
        choice2=input(">")
        if choice2=="1":
            werewolf()
            answer=ask_question(eval(choice2)-1)
            answer_weewolf(answer)
        elif choice2=="2":
            vampire()
            answer=ask_question(eval(choice2)-1)
            answer_vampire(answer)
        elif choice2=="3":
            ghost()
            answer=ask_question(eval(choice2)-1)
            answer_ghost(answer)
        elif choice2=="4":
            ghoul()
            answer=ask_question(eval(choice2)-1)
            answer_ghoul(answer)
        else:
            print("Please enter the numbers: 1,2,3,4.")
            go_straight()
    elif choice1=="go back":
        walk_back()
    else:
        print("What are you talking aoubt? I don't understand.")

main()