from sys import argv

#escript,filename=argv

txt=open("ex15_sample.txt")

print("Here's your file ","ex15_sample.txt")
print(txt.read())

print("Type the filename again:")
filename_again=input(">")

txt_again=open(filename_again)

print(txt_again.read())

txt.close()
txt_again.close()