import os

# Directory
directory = "output"



# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

# Parent Directory path
parent_dir = "./"

# Path
path = os.path.join(parent_dir, directory)


os.mkdir(path)
print("Directory '% s' created" % directory)


def get_lines(input_dir):

    file = open(input_dir,'r')
    Lines = file.readlines()

    return [line.strip() for line in Lines]