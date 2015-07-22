# Find Maximum Profit in Daily Apple Stocks
# # https://www.interviewcake.com/question/stock-price

# I have an array stock_prices_yesterday where:

# The indices are the time in minutes past trade opening time, which was 9:30am local time.
# The values are the price in dollars of Apple stock at that time.
# For example, the stock cost $500 at 10:30am, so stock_prices_yesterday[60] = 500.

# Write an efficient algorithm for computing the best profit I could have made from 1 purchase
# and 1 sale of 1 Apple stock yesterday.

# No "shorting"-you must buy before you sell. You may not buy and sell in the same time step
# (at least 1 minute must pass).

def brute_force_find_max_price_difference(stock_prices_yesterday):

    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    max_price_difference = {
        "time_earlier": 0,
        "time_later": 1,
        "price_difference": stock_prices_yesterday[1] - stock_prices_yesterday[0]
    }

    for earlier_time, price_earlier in enumerate(stock_prices_yesterday):
        for later_time_delta, price_later in enumerate(stock_prices_yesterday[earlier_time:]):
            if later_time_delta == 0: continue

            later_time = earlier_time + later_time_delta
            potential_profit = price_later - price_earlier

            if potential_profit > max_price_difference['price_difference']:
                max_price_difference = {
                    "time_earlier": earlier_time,
                    "time_later": later_time,
                    "price_difference": potential_profit
                }

    return max_price_difference

def optimal_find_max_price_difference(stock_prices_yesterday):

    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    minimum_stock_price = stock_prices_yesterday[0]
    minimum_stock_time = 0

    max_price_difference = {
        "time_earlier": 0,
        "time_later": 1,
        "price_difference": stock_prices_yesterday[1] - stock_prices_yesterday[0]
    }

    for current_time, current_stock_price in enumerate(stock_prices_yesterday):
        if current_time == 0: continue # can't sell at time 0
        potential_profit = current_stock_price - minimum_stock_price

        if potential_profit > max_price_difference['price_difference']:
            max_price_difference = {
                "time_earlier": minimum_stock_time,
                "time_later": current_time,
                "price_difference": potential_profit
            }

        if current_stock_price < minimum_stock_price:
            minimum_stock_price = current_stock_price
            minimum_stock_time = current_time

        minimum_stock_price = min(minimum_stock_price, current_stock_price)

    return max_price_difference

stock_prices_yesterday = [100, 200, 300, 400, 500, 600, 700]
print brute_force_find_max_price_difference(stock_prices_yesterday)
print optimal_find_max_price_difference(stock_prices_yesterday)

stock_prices_yesterday = [200, 200, 200, 500, 700,  10, 600]
print brute_force_find_max_price_difference(stock_prices_yesterday)
print optimal_find_max_price_difference(stock_prices_yesterday)

stock_prices_yesterday = [700, 600, 500, 400, 300, 200, 100]
print brute_force_find_max_price_difference(stock_prices_yesterday)
print optimal_find_max_price_difference(stock_prices_yesterday)

