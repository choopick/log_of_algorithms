def max_profit(stock_list):
    # 주식을 산 날로부터 가장 비싸게 팔았을 때의 수익을 담을 리스트
    max_p_list = list()
    max_p = 0
    for i in range(len(stock_list) - 1):
        max_p_list.append(max(stock_list[i+1:]) - stock_list[i])

    return max(max_p_list)


# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))