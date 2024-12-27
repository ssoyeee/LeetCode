class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num2letters = [
            [],
            [],
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']
       ]
        def helper(prefix, digits):
            if not digits:
                yield prefix
                return
            num = int(digits[0])
            letters = num2letters[num]
            for letter in letters:
                yield from helper(prefix + letter, digits[1:])
        return list(helper("", digits))