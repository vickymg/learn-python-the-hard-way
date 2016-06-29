# Reading and Writing Files

# close - closes the files ( like file -> save in an editor )
# read - reads the content of a file - you can assign the result to a variable
# readline - reads just one line of a text file
# truncate - empties the file
# write(stuff) - writes stuff to the file

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# 'w' here means open the file in 'write' mode, just open() will open in
# 'r' (read) mode
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "The same thing again, but my code is neater!"

target.write("%r\n%r\n%r\n" % (line1, line2, line3))

print "Now, let's read the file..."
target = open(filename)
print target.read()

print "And finally, we close it."
target.close()
