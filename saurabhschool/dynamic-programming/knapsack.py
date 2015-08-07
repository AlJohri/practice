# Programming Interview: 0/1 Knapsack Problem (Dynamic Programming)
# https://www.youtube.com/watch?v=UhFvK3uERGg&index=7&list=PL962BEE1A26238CA3

items = ((1,1), (10,1), (5,2), (3,7), (1,10))
max_weight = 13

from functools import lru_cache

@lru_cache(maxsize=None)
def knapsack(items, max_weight):
	return max(value + knapsack(items[i+1:], max_weight-weight) if weight <= max_weight else 0
			for i, (value, weight) in enumerate(items)) if len(items) > 0 and max_weight > 0 else 0

print(knapsack(items, max_weight))
print(knapsack.cache_info())