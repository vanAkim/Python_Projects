class Solution:
    def addSol(self, input, king):
        input.append(king)
        input.sort()
        index = input.index(king)
        sol = []
        if index > 0:
            sol.append(input[index - 1])
        if len(input) - 1 > index:
            sol.append(input[index + 1])
        return sol

    def queensAttacktheKing(self, queens, king):

        row, col, diagleft, diagright = self.checkColRowDiag(queens, king)

        sol = self.addSol(row, king)
        sol += self.addSol(col, king)
        sol += self.addSol(diagleft, king)
        sol += self.addSol(diagright, king)

        return sorted(sol)

    def checkColRowDiag(self, queens, king):
        mini = min(king)
        row = []
        col = []
        diagleft = []
        diagright = []
        for queen in queens:
            if queen[0] == king[0]:
                row.append(queen)
            elif queen[1] == king[1]:
                col.append(queen)
            elif [queen[0]-min(queen), queen[1]-min(queen)] == [king[0]-mini, king[1]-mini]:
                diagleft.append(queen)
            elif [[7, sum(queen)][sum(queen) < 8], sum(queen)-[7, sum(queen)][sum(queen) < 8]] == [[7, sum(king)][sum(king) < 8], sum(king) - [7, sum(king)][sum(king) < 8]]:
                diagright.append(queen)
        return row, col, diagleft, diagright


print(Solution().queensAttacktheKing([[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4], [2, 2], [1, 1], [
      6, 4], [5, 4], [0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3], [0, 5], [4, 2], [1, 0], [2, 7], [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]], [3, 4]))
