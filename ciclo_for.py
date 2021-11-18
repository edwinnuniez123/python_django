

for x in range(1, 11):
	print (x)

for y in "banana":
	print (y)

import itertools 
num = [1, 2, 3]
color = ['red', 'while', 'black']
value = [255, 256]

for (a, b, c) in itertools.zip_longest(num, color, value):
    print (a, b, c)


arr = ["asd", "dasda","reerwer"]
for z in arr:
	print(z)