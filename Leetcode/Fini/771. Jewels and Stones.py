import re


J = "a"
S = "aA"
count = 0


for jewel in J:
    if re.findall(jewel, S):
        count += len(re.findall(jewel, S))


print(len([re.findall(jewel, S) for jewel in J]))
print(testfc())


def testfc(self):
    return 5
