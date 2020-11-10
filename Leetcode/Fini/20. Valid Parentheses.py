class Solution:
    def isValid(self, s):
        opened = ['(','{','[']
        closed = [')','}',']']
        while s[0] in opened:
            opposite = closed[opened.index(s[0])]
            if s.find(opposite) != -1:
                index = s.find(opposite)
                if s[index - 1]
                s = s[1:index] + s[index+1:]
                if not s:
                    return True
            else:
                return False
        return False

s = '[(])'
print(Solution().isValid(s))