import time
import random

#This function iterates and pops the lists until they are in order. 
#It then returns the sorted array as variable d. The if statements 
#are used for comparing the lists. I got help from chegg for some of the if statements
#because I'm not as fluent in python as c++/c and needed a little more structure.
def merge3(a, b, c, d):
	#While loop that iterates until lists are empty. 
	while len(a) > 0 or len(b) > 0 or len(c) > 0:
        #If statements pop from none empty lists
		if len(a) == 0 and len(b) == 0:
			d.append(c[0])
			c.remove(c[0])
		elif len(a) == 0 and len(c) == 0:
			d.append(b[0])
			b.remove(b[0])

		elif len(b) == 0 and len(c) == 0:
			d.append(a[0])
			a.remove(a[0])
		else:
			if len(a) == 0:
				if b[0] > c[0]:
					d.append(c[0])
					c.remove(c[0])
				else:
					d.append(b[0])
					b.remove(b[0])
			elif len(b) == 0:
				if c[0] > a[0]:
					d.append(a[0])
					a.remove(a[0])
				else:
					d.append(c[0])
					c.remove(c[0])
			elif len(c) == 0:
				if a[0] > b[0]:
					d.append(b[0])
					b.remove(b[0])
				else:
					d.append(a[0])
					a.remove(a[0])
			else:
				x = [a[0], b[0], c[0]]
				y = min(x)
				if y == a[0]:
					d.append(a[0])
					a.remove(a[0])
				elif y == b[0]:
					d.append(b[0])
					b.remove(b[0])
				else:
					d.append(c[0])
					c.remove(c[0])
	return d

#This function splits the list into 3rds as variables a, b, and c. 
#Then uses recursion to do the same for each 3rd until the length is equal to 1.
#Then merges the lists. I used Piazza mainly to come up this this function for more
#general information
def mergesort3(arr):
	if len(arr) > 1:
		left = len(arr) // 3
		right = left + (len(arr) - left) // 2

		a = arr[:left]
		b = arr[left:right]
		c = arr[right:]

		a = mergesort3(a)
		b = mergesort3(b)
		c = mergesort3(c)

		d = []
		arr = merge3(a, b, c, d)
	return arr

n = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
index = 0
while (index < len(n)):
    a = time.time()
    mergesort3([random.random() for _ in range(n[index])])
    z = time.time()
    runtime = (z - a)
    print("n value: " + str(n[index]), "time: " + str(runtime))
    index += 1