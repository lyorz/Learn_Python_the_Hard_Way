the_count=[1,2,3,4,5]
fruits=['apples','oranges','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
    print("This is count ",number)

for fruit in fruits:
    print("A fruit of type: ",fruit)

for i in change:
    print("I got ",i)

elements=[]

for i in range(0,6):
    print("Adding ",i," to the list.")
    elements.append(i)

for i in elements:
    print("Elements was: ",i)

