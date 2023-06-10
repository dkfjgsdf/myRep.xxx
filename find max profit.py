def find_max_price(prices):
    count = 0
    profit = 0
    
    for current_price in prices:

        count += 1

        if current_price == min(prices):

            for max_price_in_profit_range in prices[count-1:]:

                if max_price_in_profit_range == max(prices[count-1:]):

                    profit = max_price_in_profit_range - current_price
    
    return print('profit = ', profit)



# find_max_price([7,1,5,3,6,4]) # 5
# find_max_price([7,6,4,3,1]) # 0
# find_max_price([2,2,1,3,9,5]) # 8
find_max_price([2,4,1]) # 2
