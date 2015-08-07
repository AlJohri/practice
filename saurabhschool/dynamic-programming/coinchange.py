# Programming Interview: Dynamic Programming: Coin Change Problem
# https://www.youtube.com/watch?v=GafjS0FfAC0&index=1&list=PL962BEE1A26238CA3

total = 30
denominations = (1, 15, 25)

from functools import lru_cache

@lru_cache(maxsize=None)
def coin_change(total, denominations):
	return min(coin_change(total-denomination, denominations)
		for denomination in sorted(denominations)) + 1 if total > 0 else 0

print(coin_change(total, denominations))
print(coin_change.cache_info())
