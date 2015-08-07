# Programming Interview: 0/1 Knapsack Problem (Dynamic Programming)
# https://www.youtube.com/watch?v=UhFvK3uERGg&index=7&list=PL962BEE1A26238CA3

items = ((1,1), (10,1), (5,2), (3,7), (1,10))
max_weight = 13

from functools import lru_cache

@lru_cache(maxsize=None)
def knapsack_val(items, max_weight):
	potential_knapsacks = [value + knapsack_val(items[i+1:], max_weight-weight)
		for i, (value, weight) in enumerate(items) if weight <= max_weight]
	return max(potential_knapsacks, default=0) if len(items) > 0 and max_weight > 0 else 0

print(knapsack_val(items, max_weight))
print(knapsack_val.cache_info())

print("--------------------------------------------------------------")

sum_by_value = lambda items: sum(value for value, weight in items)

@lru_cache(maxsize=None)
def knapsack(items, max_weight):
	potential_knapsacks = [((value, weight),) + knapsack(items[i+1:], max_weight-weight)
		for i, (value, weight) in enumerate(items) if weight <= max_weight]
	return max(potential_knapsacks, key=sum_by_value, default=()) if len(items) > 0 and max_weight > 0 else ()

print(knapsack(items, max_weight))
print(knapsack.cache_info())