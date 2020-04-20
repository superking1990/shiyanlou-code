for num in range(1,100):
	if num % 10 == 7 or num % 7 == 0 or num // 10 == 7:
		continue
	print(num)
