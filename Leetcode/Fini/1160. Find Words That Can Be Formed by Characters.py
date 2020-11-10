class Solution:
    def countCharacters(self, words, chars):
        totalLength = 0
        for word in words:
            temp_chars = chars
            for letter in word:
                if temp_chars.find(letter) != -1:
                    temp_chars = temp_chars.replace(letter,'',1)
                    if len(temp_chars) == len(chars) - len(word):
                        totalLength += len(word)
                else:
                    break

        return totalLength

print(Solution().countCharacters(["hello","world","leetcode"],'welldonehoneyr'))