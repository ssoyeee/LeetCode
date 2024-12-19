'''
2086. Minimum Number of Food Buckets to Feed the Hamsters | Medium

You are given a 0-indexed string hamsters where hamsters[i] is either:
'H': hamster at index i, or '.' : index i is empty
You will add some number of food buckets at the empty indices in order to feed the hamsters. 
A hamster can be fed if there is at least one food bucket to its left or to its right. 
A hamster at index i can be fed if you place a food bucket at index i - 1 and/or at index i + 1.
Return the minimum number of food buckets you should place at empty indices to feed all the hamsters 
    or -1 if it is impossible to feed all of them.
'''
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        n = len(hamsters)
        i, result = 0, 0
        while i < n:
            if hamsters[i] == 'H':
                if i+1 < n and hamsters[i+1] == '.':
                    i += 2
                    result += 1
                elif i- 1 >= 0 and hamsters[i-1] == '.':
                    result += 1
                else:
                    return -1
            i += 1
        return result