import random
import urllib.request
import sys

WORD_URL="http://learncodethehardway.org/words.txt"
WORDS=[]

"""PHRASES的key是一些创建类的语句，value为相应的注释"""
PHRASES={
    #创建一个名为%%%的类
    "class %%%(%%%):":
    #注释：创建一个名为%%%的
    "Make a class named %%% that is-a %%%.",
    #创建一个名为%%%的类并赋予初始化函数（传参***）
    "class %%%(object):\n\tdef __init__(self,***)":
    #注释：
    "class %%% has-a __init__ that takes self and *** parameters.",
    #创建一个名为%%%的类并定义成员函数名为***，传参@@@
    "class %%%(object):\n\tdef ***(self,@@@)":
    #注释
    "class %%% has-a function named *** that takes self and @@@ parameters.",
    #利用类%%%实例化对象***
    "***=%%%()":
    #注释
    "Set *** to an instance of class %%%.",
    #实例化后的***调用%%%中的成员函数***并传参@@@
    "***.***(@@@)":
    "From *** get the *** function, and call it with parameters self,@@@.",
    #实例化后的***，将‘***’赋予其属性***
    "***.***='***'":
    "From *** get the *** attribute and set it to '***'."
}

if len(sys.argv)==2 and sys.argv[1]=='english':
    PHRASE_FIRST=True
else:
    PHRASE_FIRST=False

#从网站加载单词列表
for word in urllib.request.urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

def convert(snippet,phrase):
    """将语句snippet中的符号替换成具体参数"""
    #sample(list,k)：返回一个长度为k的新列表，列表存放list产生的k个随机元素
    #class_names是一个从单词列表中随机抽取k个（k等于字符串snippet中%%%数量）元素的列表
    #还要首字母大写
    class_names=[w.capitalize() for w in
                random.sample(WORDS,snippet.count("%%%"))]
    #other_names是一个从单词列表中随机抽取k个（k等于字符串snippet中***数量）元素的列表
    other_names=random.sample(WORDS,snippet.count("***"))
    results=[]
    param_names=[]

    for i in range(0,snippet.count("@@@")):
        param_count=random.randint(1,3)

        #报错：list中元素是byte型不能直接转化为字符串
        #param_names.append(', '.join(random.sample(WORDS,param_count)))
        #修改如下：
        param_list=random.sample(WORDS,param_count)
        #将列表里的元素挨个转化为str型
        for i in range(len(param_list)):
            param_list[i]=str(param_list[i]) 
        #将列表转化为指定格式字符串
        param_names.append(', '.join(param_list))           
        #fine 修改完就正常了

    for sentence in snippet,phrase:
        result=sentence[:]

        for word in class_names:
            result=result.replace("%%%",str(word))
        for word in other_names:
            result=result.replace("***",str(word))
        for word in param_names:
            result=result.replace("@@@",str(word))
        results.append(result)
    return results

try:
    while True:
        snippets=list(PHRASES.keys())
        #将snippets列表中的元素顺序随机打乱
        random.shuffle(snippets)

        for snippet in snippets:
            #phrase记录注释
            phrase=PHRASES[snippet]
            #question定义语句 answer相应注释
            question,answer=convert(snippet,phrase)
            if PHRASE_FIRST:
                question,answer=answer,phrase
            print(question)
        
        input(">")
        print("ANSWER: ",answer,"\n\n")
except EOFError:
    print("\nBye")