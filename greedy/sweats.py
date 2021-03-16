def solution(n, lost, reserve):
    new_lost = list(lost)
    # 여벌 체육복을 도난맞은 경우
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            new_lost.remove(i)

    # 체육 수업을 들을 수 있는 학생은 1, 없는 학생은 0
    possible = [0 if i in new_lost else 1 for i in range(1, n + 1)]
    
    for i in new_lost:
        if i + 1 in reserve:
            possible[i - 1] = 1
            reserve.remove(i + 1)
            
        elif i - 1 in reserve:
            possible[i - 1] = 1
            reserve.remove(i - 1)
    
    answer = sum(possible)
    return answer

print(solution(7,[1,2,3,4,5,6,7],[1,2,3]))