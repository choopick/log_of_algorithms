def solution(s):
    num_in_english = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    test_list = []
    answer_list = []
    for i in range(len(s)):
        if ord(s[i]) < 58 and ord(s[i]) >= 48:
            answer_list.append(s[i])
            
        else:
            test_list.append(s[i])
            asci = ord(s[i])
        if ''.join(test_list) in num_in_english.keys():
            answer_list.append(str(num_in_english[''.join(test_list)]))
            test_list = []
    answer = ''.join(answer_list)
    return int(answer)

print(solution("one4seveneight"))