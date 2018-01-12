#Autumn Franke
#Upload File
#1-12-2018

counter = 0

infile = open("HelloWorld.py","r")
for line in infile.readlines():
    print(counter, line)
    counter = counter + 1
