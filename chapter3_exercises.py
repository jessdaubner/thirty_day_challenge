# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

# Jessie Daubner

# 3.1
# The error message that results from running the following program is "NameError: name 'repeat_lyrics' is not defined".
# A function definition must be executed befor it can be called.

repeat_lyrics

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

def repeat_lyrics():
	print_lyrics()
	print_lyrics()


# 3.2
# When the following program runs, an indentation error occurs: "IndentationError: unexpected indent" because the print statements are still
# indended as if they comprise a the body of a function. If the beginning print statements were indented correctly, an indentation error would 
# still occur because the definition of print_lyrics does not have any body statements that follow it. 

	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

repeat_lyrics

def print_lyrics():

# 3.3
# Create a function that takes a string named 's' as a parameter and prints the string so that its last leter is in column 70 of the display.

def right_justify(s):
	sp = ' '
	print(sp * (70 - len(s)) + s)

right_justify('Jessie')

# 3.4

#1)
def do_twice(f):
	f()
	f()

def print_spam(): 
	print 'spam'

do_twice(print_spam) 

#2)

def do_twice(f, v):
	f(v)
	f(v)

def print_name(j): 
	print j

do_twice(print_name, "Jessie") 

#3)
def print_twice(s): 
	print s
	print s

#4) 
def do_twice(f, v):
	f(v)
	f(v)

def print_twice(s):
	print s
	print s

do_twice(print_twice, "spam")

#5) func do_four takes a func object and a value and calls the func 4 times, passing value as a parameter
def do_four(f, v, t):
	for i in range(t):
		f(v)

def print_name(j): 
	print j

do_four(print_name, "Jessie", 4)

