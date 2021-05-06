
# Perulangan For
## FIzz Buzz

"""
Write a number from 1 to 100 on a new line.
	- For each multiple of 3, print "Fizz" instead of the number. 
	- For each multiple of 5, print "Buzz" instead of the number. 
	- For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
"""

for a in range(1, 101) :
	if(a % 3 == 0 and a % 5 == 0):
			print("FizzBuzz")
	elif (a % 3 == 0) :
		print ("Fizz")
	elif (a % 5 == 0):
		print ("Buzz")
	else :
		print (a)

print ("                 ")


## Basic FOR
animals = ["Cow", "Cat", "Dog", "Ant"]
for x in animals :
	print("I have a " + x)

print ("                 ")

## Break Statement
print ("Break Statement")
for numbers in range(1, 10) :
	if (numbers == 5) :
		break
	print(numbers)

print ("                 ")

## Continue Statement
print ("Continue Statement")
for number in range (1, 10):
	if (number % 2 == 0):
		continue

	print(number)