def matrixMultiplication(matrixA, matrixB):
	if type(matrixA) == int and type(matrixB) == int:
		return matrixA * matrixB
	elif type(matrixA) == int and type(matrixB) == list:
		solution = []
		for row in matrixB:
			solutionRow = []
			for col in row:
				solutionRow.append(col * matrixA)
			solution.append(solutionRow)
		return solution
	elif type(matrixB) == int and type(matrixA) == list:
		solution = []
		for row in matrixA:
			solutionRow = []
			for col in row:
				solutionRow.append(col * matrixB)
			solution.append(solutionRow)
		return solution
	elif type(matrixA) == list and type(matrixB) == list:
		solution = []
		addthis = []
		mul_index = 0
		for row in matrixA:
			mul_index += 1
			matrixB_row = 0
			for col in row:
				addthis.append(col * matrixB[matrixB_row][mul_index])
				matrixB_row += 1
				



print(matrixMultiplication(1,2))
print(matrixMultiplication(2,[[1,2,3],[4,5,6],[7,8,9]]))
print(matrixMultiplication([[1,2,3],[4,5,6],[7,8,9]],2))
print(matrixMultiplication([[1,2,3],[4,5,6]],[[7,8],[9,10],[11,12]]))
