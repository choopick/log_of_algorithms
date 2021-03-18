
def solution(name):
    answer = 0
    mid_point = (ord('A') + ord('Z')) / 2
    for i in range(len(name)):
        right = 1


        if name[i] != 'A' and ord(name[i]) < mid_point:
            answer += (ord(name[i]) - ord('A'))
        elif name[i] != 'A' and ord(name[i]) > mid_point:
            answer += (ord('Z') - ord(name[i]) + 1)
        
        if i == len(name)-1:
            break

        elif name[i] != 'A':
            for j in range(i + 1, len(name)):
                if name[j] == 'A':
                    right += 1
                else:
                    break
            if right < len(name)/2 and right != 1:
                answer += right
            elif right >= len(name)/2 and right != 1:
                answer += (len(name) - right - 1) 
            if right == 1:
                answer += right
                continue
        
    return answer

print(solution("BBBAAAB")) #8
print(solution("ABABAAAAABA")) #10
print(solution("CANAAAAANAN")) #48
print(solution("ABAAAAABAB")) #8
print(solution("ABABAAAAAB")) #8
print(solution("BABAAAAB")) #7
print(solution("AAA")) #0
print(solution("ABAAAAAAABA")) #6
print(solution("AAB")) #2
print(solution("AABAAAAAAABBB")) #11
print(solution("ZZZ")) #5
print(solution("BBBBAAAAAB")) #10
print(solution("BBBBAAAABA")) #12
'''

def solution(name):
    answer = 0
    begin = ['A' for i in range(len(name))]
    mid_asc = (ord('A') + ord('Z')) / 2
    idx = 0
    while ''.join(begin) != name:
        if begin[idx] != name[idx] and ord(name[i]) < mid_asc:
            answer += (ord(name[i]) - ord('A'))
            begin[idx] = name[idx]
        elif begin[idx] != name[idx] and ord(name[i]) > mid_asc:
            answer += (ord('Z') - ord(name[i]) + 1)
            begin[idx] = name[idx]
        
        next_idx = 
    return answer

solution('JAZ')
'''