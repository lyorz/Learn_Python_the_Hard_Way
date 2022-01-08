from sys import argv
from os.path import exists

from_file='ex17in.txt'
to_file='ex17out.txt'


print("Copying from {} to {}.".format(from_file,to_file))

in_file=open(from_file)
in_data=in_file.read()

print("The input file is ",len(in_data),' bytes long.')

print("Dose the output file exsist? ",exists(to_file))
print("Ready, hit RETURN to continue, CRTL-C to abort.")
input()

out_file=open(to_file,'w')
out_file.write(in_data)

print("Alright,all done.")

#out_file.close()
in_file.close()