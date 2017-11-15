def isort(A):
	for i in range(len(A)):
		j = i
		while j > 0 and A[j-1] > A[j]:
			A[j], A[j-1] = A[j-1], A[j]
			j -= 1
	return A

A = [53,12,34,21,58,15]
print(A)
print(isort(A))
