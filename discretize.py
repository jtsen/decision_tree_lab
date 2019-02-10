def sort_entropy(dataset):
	for row in range(len(dataset)):
		if row == 0:
			continue
		dataset[row][4] = round(int(dataset[row][4]))
		if((dataset[row][4] % 10) >= 5):
			dataset[row][4] = dataset[row][4]+(10 - dataset[row][4]%10)
		else:
			dataset[row][4] = dataset[row][4]- (dataset[row][4]%10)

		dataset[row][5] = round(int(dataset[row][4]))
		if((dataset[row][5] % 10) >= 5):
			dataset[row][5] = dataset[row][5]+(10 - dataset[row][5]%10)
		else:
			dataset[row][5] = dataset[row][5]- (dataset[row][5]%10)

		dataset[row][7] = round(float(dataset[row][7]))
		dataset[row][8] = round(float(dataset[row][8]))

		dataset[row][4] = str(dataset[row][4])
		dataset[row][5] = str(dataset[row][4])
		dataset[row][7] = str(dataset[row][7])
		dataset[row][8] = str(dataset[row][8])

		dataset[row][9] = float(dataset[row][9])
		if(dataset[row][9] > 3.5):
			dataset[row][9] = "good"
		else:
			dataset[row][9] = "bad"

	dataset.pop(0)

	return dataset

def sort_variance(dataset):
	for row in range(len(dataset)):
		if row == 0:
			continue
		dataset[row][4] = round(int(dataset[row][4]))
		if((dataset[row][4] % 10) >= 5):
			dataset[row][4] = dataset[row][4]+(10 - dataset[row][4]%10)
		else:
			dataset[row][4] = dataset[row][4]- (dataset[row][4]%10)

		dataset[row][5] = round(int(dataset[row][4]))
		if((dataset[row][5] % 10) >= 5):
			dataset[row][5] = dataset[row][5]+(10 - dataset[row][5]%10)
		else:
			dataset[row][5] = dataset[row][5]- (dataset[row][5]%10)

		dataset[row][7] = round(float(dataset[row][7]))
		dataset[row][8] = round(float(dataset[row][8]))

		dataset[row][4] = str(dataset[row][4])
		dataset[row][5] = str(dataset[row][4])
		dataset[row][7] = str(dataset[row][7])
		dataset[row][8] = str(dataset[row][8])

		dataset[row][9] = float(dataset[row][9])

	dataset.pop(0)


	return dataset