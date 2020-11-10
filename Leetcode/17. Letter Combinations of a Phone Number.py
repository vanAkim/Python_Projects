

class Solution:
    def letterCombinations(self, digits):
        letterOfDigits = []
        for chiffre in str(digits):
            letterOfDigits.append(self.arrayOfLetter(int(chiffre)))
        print(letterOfDigits)
        index_letters = 0
        lenOfSol = 1
        lenOfLetterArray = []
        for i in range(len(letterOfDigits)):
            lenOfSol *= len(letterOfDigits[i])
            lenOfLetterArray.append(len(letterOfDigits[i]))
        productArray = []
        sol = []
        print(lenOfSol,lenOfLetterArray)
        while len(sol) < lenOfSol:
            for index_arrays in



    def arrayOfLetter(self, n):
        if n < 7:
            return [chr(94+((n-1)*3)+i) for i in range(3)]
        elif n == 7:
            return [chr(94+((n-1)*3)+i) for i in range(4)]
        elif n == 8:
            return [chr(94+((n-2)*3)+4+i) for i in range(3)]
        elif n == 9:
            return [chr(94+((n-2)*3)+4+i) for i in range(4)]

print(Solution().letterCombinations(23))