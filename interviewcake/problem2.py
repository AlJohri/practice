# https://www.interviewcake.com/question/product-of-other-numbers
#
# You have an array of integers, and for each index you want to find the
# product of every integer except the integer at that index.
#
# Write a function get_products_of_all_ints_except_at_index() that takes an
# array of integers and returns an array of the products.

# For example, given:

#   [1, 7, 3, 4]
# your function would return:

#   [84, 12, 28, 21]
# by calculating:

#   [7*3*4, 1*3*4, 1*7*4, 1*7*3]
# Do not use division in your solution.

def brute_force_get_products_of_all_ints_except_at_index(lst):
	return [reduce(lambda x,y: x*y, (x for j,x in enumerate(lst) if j != i), 1) for i in range(len(lst))]

def optimal_get_products_of_all_ints_except_at_index(lst):
	# traverse first time
	temp_product_list = list(lst)
	current_product = 1
	for i, x in reversed(list(enumerate(lst))):
		current_product = current_product * x
		temp_product_list[i] = current_product

	# traverse second time
	ret = list(lst)
	current_product = 1
	for i in range(len(lst)-1):
		ret[i] = temp_product_list[i+1] * current_product
		current_product = current_product * lst[i]
	ret[-1] = current_product

	return ret

print(brute_force_get_products_of_all_ints_except_at_index([1, 7, 3, 4]))
print(optimal_get_products_of_all_ints_except_at_index([1, 7, 3, 4]))

print(brute_force_get_products_of_all_ints_except_at_index([1, 7, 3, 0]))
print(optimal_get_products_of_all_ints_except_at_index([1, 7, 3, 0]))
