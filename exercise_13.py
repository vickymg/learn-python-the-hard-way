# Parameters, Unpacking, Variables

# import module

# argv is the "argument variable" - the variable holds the arguments you pass
# to your script
from sys import argv

# line 3 unpacks argv, so the arguments get assigned to four variables you can
# work with
script, first, second, third = argv

print "The script is called:", script
print "Your first variabe is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# to run: $ python exercise_13.py first 2nd 3rd
