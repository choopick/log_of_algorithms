
def solution(number, k):
    answer = ''
    temp = list()
    number_list = [int(i) for i in number]
    allow = len(number) - k
    cnt = int(allow)
    sorted_num_list = list(set(sorted(number_list)))
    sorted_num_list.reverse()
    print(sorted_num_list)
    i = 0
    while len(temp) < allow:
        for idx, con in reversed(list(enumerate(number_list))):
            if len(temp) > 1 and idx < temp[-1][0] and number_list[idx] < temp[-1][1]:
                cnt -= 1
                number_list[idx] = -1
            if idx == 0:
                i += 1
            if int(con) == sorted_num_list[i] and len(number_list) - idx - 1 >= cnt - 1:
                temp.append([idx, con])
                number_list[idx] = -1
                cnt -= 1
                i = 0
                break
        
    temp = sorted(temp, key = lambda x : x[0])
    
    answer = ''.join([str(i[1]) for i in temp])

    return answer

print(solution("4177252841", 4))