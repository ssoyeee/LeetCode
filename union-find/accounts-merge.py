from collections import defaultdict 
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email2name = {}

        for account in accounts:
            name = account[0]

            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)
                
                email2name[email] = name
        
        res = []
        visited = set()
        for email in graph:
            if email not in visited:
                stack = [email]
                visited.add(email)

                local_res = []
                
                while stack:
                    node = stack.pop()
                    local_res.append(node)

                    for edge in graph[node]:
                        if edge not in visited:
                            stack.append(edge)
                            visited.add(edge)
                res.append([email2name[email]]+sorted(local_res))
        return res
# Time: O(NK) * N log K -> O(N * K * N log K) where n is number of accounts and K is max number of emails per user
# Space: O(NK)