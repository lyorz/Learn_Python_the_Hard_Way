print("Let's practice everything.")

print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print("----------------")
print(poem)
print("----------------")

five=10-2+3-6

print("This should be five: ",five)

def secret_formula(started):
    jelly_beans=started*50
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates

start_points=10000
beans,jars,crates=secret_formula(start_points)

print("With a starting point of ",start_points)
print("We'd have ",beans,' beans, ',jars ,' jars, and ',crates,' crates.')

start_points/=10

print("We can also do that this way:")
t=secret_formula(start_points)
print("We'd have {} beans, {} jars and {} crates.".format(t[0],t[1],t[2]))

