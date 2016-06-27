# Asking questions

name = raw_input("What is your name? ")
print "Hello, %s." % name

print "How old are you?"
age = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weigh?"
weight = raw_input()

print "So, you're %r years old, %r tall and %r heavy." % (age, height, weight)


# raw_input([prompt])
# If the prompt argument is present, it is written to standard output without a
# trailing newline. The function then reads a line from input, converts it to a
# string (stripping a trailing newline), and returns that.
# >>>
# >>> s = raw_input('--> ')
# --> Monty Python's Flying Circus
# >>> s
# "Monty Python's Flying Circus"


# The difference with input() is that it tries to interpret the input given by
# the user; it is usually best to avoid input() and to stick with raw_input()
# and custom parsing/conversion code.
