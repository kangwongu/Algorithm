coin_list = [500, 100, 50, 10]


def min_coin_count(value, coin_list):
    total_coin_list = 0
    details = list()
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value // coin
        total_coin_list += coin_num
        value -= coin * coin_num
        details.append([coin, coin_num])
        
    return total_coin_list, details
