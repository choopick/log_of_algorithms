import time


def sublist_max(profits):
    max_profit = profits[0] # 최대 수익
    
    for i in range(len(profits)):
        # 인덱스 i부터 j까지 수익의 합을 보관하는 변수
        total = 0
        
        for j in range(i, len(profits)):
            # i부터 j까지 수익의 합을 계산
            total += profits[j]
            
            # i부터 j까지 수익의 합이 최대 수익이라면, max_profit 업데이트
            max_profit = max(max_profit, total)

    return max_profit


def sublist_max2(profits):
    max_profit = -999
    li = []
    for i in range(len(profits)):
        for j in range(i,len(profits)):
            temp = sum(profits[i:j+1])
            if temp > max_profit:
                max_profit = temp
                li = profits[i:j+1]
    # print(li)
    return max_profit


# 테스트

start = time.time()

print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))

end = time.time()
print("time1",end - start)


start2 = time.time()

print(sublist_max2([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max2([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max2([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))

end2 = time.time()
print("time2",end2 - start2)