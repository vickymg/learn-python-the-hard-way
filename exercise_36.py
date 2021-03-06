# Designing and Debugging

# Rules for If-statements

# 1. Every if-statement must have an else
# 2. If this else should never be run becuase it doesn't make sense, you should
#    use a 'die' function in the else that prints out an error message and dies
# 3. Never nest if-statements more than two deep, and always try to make them
#    one deep
# 4. Treat if-statements like paragraphs, where each, if, elif, else grouping
#    is like a set of sentences. Put blank lines before and after.
# 5. Boolean tests should be simple. If they are complex, move their calculations
#    to variables earlier in your function, and use a good name for the variable

# Rules for Loops

# 1. Use a while loop only to loop forever (and that means probably never) -
#    Python specific
# 2. Use a for loop for all other kinds of looping, especially if there is a
#    fixed or limited number of things to loop over

# Tips for Debugging

# 1. Do not use a debugger
# 2. Use print to print out the values of variables at points in the program to
#    see where rhey go wrong
# 3. Make sure parts of your program work section by section
