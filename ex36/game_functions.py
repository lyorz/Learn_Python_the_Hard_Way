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
    start_function()

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