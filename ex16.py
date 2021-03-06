from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that hit CTRL-C (^C)."
print "If you do want that, hit RETURN"

raw_input("?")

print "Opening the file..."
target= open(filename, 'w') #w stands for writing permission for the opened file

print "Truncating the file. Goodbye!"
target.truncate() #empties the file. So does the 'w' in open. Truncate allows
#to say how much of the file is deleted

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"

target.write(line1) #writing to the file
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n") #condensed

print "And finally, we close it."
target.close()
