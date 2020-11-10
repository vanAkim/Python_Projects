import re

wordList = ["flower","flow","flight"]





if not wordList:
    print("not")
elif min([len(word) for word in wordList]) == 0:
    print("y a un nul")

firstLetterArray = [word[0] for word in wordList]

if re.findall(wordList[0][0],' '.join(firstLetterArray)) == firstLetterArray:
    indexLetter = 1
    lenWordList = [len(word) for word in wordList]
    indexShortWord = lenWordList.index(min(lenWordList))

    pattern = wordList[indexShortWord][0:indexLetter]
    print( re.findall(pattern, ' '.join([word[0:indexLetter] for word in wordList])))
    while indexLetter <= lenWordList[indexShortWord] and re.findall(pattern, ' '.join([word[0:indexLetter] for word in wordList])) == [pattern for _ in wordList]:
        indexLetter += 1
        pattern = wordList[indexShortWord][0:indexLetter]
    print(wordList[indexShortWord][0:indexLetter-1])
else:
    print("else")