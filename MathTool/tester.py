def solution(answers):
    max_corr = []
    ans_cnt = []
    
    # 맞춘 정답의 개수를 세기 위한 파라미터 생성
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    # 1, 2, 3번 수포자의 규칙이 들어있는 배열 생성
    ruleNo1 = [1, 2, 3, 4, 5]
    ruleNo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ruleNo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 수포자 답변의 배열을 정답 배열보다 길게 반복시킴
    No1 = ruleNo1 * (len(answers)//len(ruleNo1) + 1)
    No2 = ruleNo2 * (len(answers)//len(ruleNo2) + 1)
    No3 = ruleNo3 * (len(answers)//len(ruleNo3) + 1)
    
    # 비교 카운트 시작
    for i in range(len(answers)):
        if No1[i] == answers[i]:
            cnt1 += 1
        if No2[i] == answers[i]:
            cnt2 += 1
        if No3[i] == answers[i]:
            cnt3 += 1
    
    # 맞춘 개수 저장
    ans_cnt =[cnt1, cnt2, cnt3]
    max_cnt = max(ans_cnt)
    # 최다 정답자 리스트
    max_corr = []
    
    # 최다 정답자가 한명일 경우
    if ans_cnt.count(max_cnt) == 1:
        max_corr.append(ans_cnt.index(max_cnt) + 1)
        return max_corr
    
    # 최다 정답자가 둘 이상일 경우
    elif ans_cnt.count(max_cnt) > 1:
        for i in range(len(ans_cnt)):
            if ans_cnt[i] == max_cnt:
                max_corr.append(i + 1)
        return sorted(max_corr)

print(solution([1,2,3,4,5]))