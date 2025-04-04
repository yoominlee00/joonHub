def solution(tickets):
    tickets.sort()
    result = ["ICN"]
    visited = [False]*len(tickets)
    def dfs(n):
        key = result[-1]
        if n == len(tickets):
            return result
        for i,val in enumerate(tickets):
            start = val[0] 
            end = val[1] 
            if not visited[i] and start == key:
                visited[i] = True
                result.append(end)
                ans = dfs(n+1)
                if ans :
                    return ans
                visited[i] = False
                result.pop()
    
    return dfs(0)