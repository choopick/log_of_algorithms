from collections import deque
def BFS():
    queue = deque()
    
    if False not in visited:
        return
    else:
        visited[start] = True
        for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            stack.append(i)
            
    while queue:
        q = queue.popleft()
        answer.append()


def solution(tickets):
    answer = ["ICN"]
    visited = [False for i in tickets]
    
    DFS()
    return answer