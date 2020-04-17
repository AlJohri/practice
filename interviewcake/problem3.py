# https://www.interviewcake.com/question/highest-product-of-3

# Given an array_of_ints, find the highest_product you can get
# from three of the integers.
# The input array_of_ints will always have at least three integers.

# Gotchas
# Does your function work with negative numbers?
# If list_of_ints is [-10, -10, 1, 3, 2] we should return 300 (which we get by taking -10 * -10 * 3).

# We can do this in O(n) time and O(1) space.

test_cases = [
	[4, 3, 1, 5, 7, 2, 0],
	[4, 3, 1, -5, 7, 2, 0],
	[-1, -2, -3, -4, -5, -6],
	[-5, -4, 6, 2, 1, -1],
	[5, -4, 6, 2, 1, -1],
	[1, 2, 3, 4, 5, -7, -8, 9],
	[0, 0, 0, 0, 0, 90, 100],
	[-10,-10,1,3,2],
	[6, -3, -10, 0, 2], # 180
]

product = lambda arr: reduce(lambda x,y: x*y, arr, 1)

def highest_product_of_3_optimal(array_of_ints):

	if len(array_of_ints) < 3: raise Exception("Less than 3 items!")

	highest = max(array_of_ints[:3-1])
	lowest = min(array_of_ints[:3-1])

	highest_product_of_2 = product(array_of_ints[:3-1])
	lowest_product_of_2 = product(array_of_ints[:3-1])

	highest_product_of_3 = product(array_of_ints[:3])

	for current in array_of_ints[3-1:]:

		highest_product_of_3 = max(
			highest_product_of_3,
			current * highest_product_of_2,
			current * lowest_product_of_2
		)

		highest_product_of_2 = max(
			highest_product_of_2,
			current * highest,
			current * lowest
		)

		lowest_product_of_2 = min(
			lowest_product_of_2,
			current * highest,
			current * lowest
		)

		highest = max(highest, current)
		lowest = min(lowest, current)

	return highest_product_of_3

def highest_product_of_n_optimal(array_of_ints, n=3):

	if len(array_of_ints) < n: raise Exception("Less than %d items!" % n)

	highest_product = [product(array_of_ints[:i]) for i in range(2, n+1)]
	lowest_product = [product(array_of_ints[:i]) for i in range(2, n+1)]

	highest_product.insert(0, max(array_of_ints[:n-1]))
	lowest_product.insert(0, min(array_of_ints[:n-1]))

	for current in array_of_ints[n-1:]:

		for i in range(len(highest_product)-1, 0, -1):

			highest_product[i] = max(
				highest_product[i],
				current * highest_product[i-1],
				current * lowest_product[i-1],
			)

			lowest_product[i] = min(
				lowest_product[i],
				current * highest_product[i-1],
				current * lowest_product[i-1],
			)

		highest_product[0] = max(highest_product[0], current)
		lowest_product[0] = min(lowest_product[0], current)

	return highest_product[-1]

for test_case in test_cases:
	print test_case, \
		highest_product_of_3_optimal(test_case), \
		highest_product_of_n_optimal(test_case, 3)



