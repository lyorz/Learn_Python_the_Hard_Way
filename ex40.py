"""类就像模块"""
class myStuff(object):
    def __init__(self):
        """创建空对象时用于初始化新创建的空对象"""
        self.tangerine="And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

"""对象就像导入"""
thing=myStuff()
thing.apple()
print(thing.tangerine)

"""举例"""
class Song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday=Song(
    ["Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"])
    
bulls_on_parade=Song(["They rally around tha family",
                    "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()