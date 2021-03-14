num_net = 1

def DFS(start, n, computers):
    global num_net
    if start == n:
        return 

    for idx in range(start, n):
        if computers[start][idx] == 0:
            num_net += 1
            DFS(idx, n, computers) 
        
        
            
def solution(n, computers):
    DFS(0, n, computers)

    return num_net

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))