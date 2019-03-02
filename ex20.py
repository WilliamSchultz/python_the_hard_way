from sys import argv

script, input_file = argv

def print_all(f): #f is file variable
    print f.read()

def rewind(f):
    f.seek(0) #0 is bytes, not lines. This goes to the start of the file.

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First, let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file) #rewinding file pointer

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
