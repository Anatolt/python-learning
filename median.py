def median(array):
	array = sorted(array)
	count = len(array)
	if count % 2 == 0:
		return (array[count/2 - 1] + array[count/2]) / 2.0
	else:
		return array[count/2]
