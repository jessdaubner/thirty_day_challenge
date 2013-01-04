# Exercises for chapter 2: Problems 2.1, 2.2, 2.3, and 2.4 in Think Python

# Jessie Daubner

# 2.1 

zipcode = 02492
zipcode = 02132


# Python interprets an integer with a leading zero as a base-8 system value converted to decimal representation, which it does
# by taking the sum of the products of the octal digits and the powers of 8 which they represent. 
# For instance, 01 displays as 1 = (1 * 8**1) + (1 * 8**0), 010 as 8  = (0 * 8**2) + (1 * 8**1) + (0 * 8**0) and so on. 

#2.2

5
x = 5
x + 1

# produces the output 5 and 6, each on separate lines.

print 5
x = 5
print x + 1

# also produces the output 5 and 6, each on separate lines. 


#2.3
width = 17
height = 12.0
delimiter = '.'

# 1) width/2 		In Python 2, the value is 8 and they type is int. In Python 3, the value is 8.5 and the value is float.
# 2) width/2.0  	The value is 8.0 and the type is float.
# 3) height/3   	The value is 4.0 and the type is float.
# 4) 1 + 2 * 5      The value is 11 and the type is int.
# 5) delimiter * 5  The value is '.....' and the type is str. 

#2.4
# 1) 523.599
(4.0/3.0)*(math.pi)*(5**3) = 523.599

# 2) $945.45
((24.95)*(0.6))*60 + (3 + 59 * 0.75) = 945.45

# 3) 7:30am
((60 * 6 + 52) + (8.25 * 2) + (7.20 * 3))/60.0 = 7.50 hrs #total elapsed in the day