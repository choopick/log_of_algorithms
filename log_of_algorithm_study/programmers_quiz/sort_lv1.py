def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]
        idx = commands[i][2] - 1
        temp_list = array[start:end]
        temp_list.sort()
        answer.append(temp_list[idx])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))