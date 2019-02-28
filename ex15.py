from sys import argv #sys is a package getting argv feature from this package

script, filename = argv #filename is passed in terminal

txt = open(filename) #opens filename

print "Here's your file %r:" % filename #prints the sentence with filename
print txt.read() #prints the file

print "Type the filename again:"
file_again = raw_input("> ") #getting user input

txt_again = open(file_again) #open file again

print txt_again.read()
