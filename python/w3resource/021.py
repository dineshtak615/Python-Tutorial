def histogram(list):
	for n in list:
		output = ''
		while True:
			output = '*' * n
			print(output)
			break
print(histogram([3,2,3]))