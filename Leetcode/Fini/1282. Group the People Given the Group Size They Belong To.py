class Solution:
    def groupThePeople(self, groupSizes):
        people = []
        for ID, group in enumerate(groupSizes):
            people.append([group, ID])

        people = sorted(people)
        index = 0
        sol = []
        while index <= len(people)-1:
            sol.append([people[i][1] for i in range(index,index + people[index][0])])
            index += people[index][0]
        return sol

groupSizes = [2,1,3,3,3,2]
print(Solution().groupThePeople(groupSizes))