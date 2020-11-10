

class Solution:
    def numSquares(self, n):
        biggest_squareNumber = []
        i = 1
        while i*i <= n:
            biggest_squareNumber.append(i*i)
            i += 1

        biggest_squareNumber.reverse()
        print(biggest_squareNumber)
        sol = []

        Wsol = []

        for index in range(len(biggest_squareNumber)):
            total = 0
            tmpsol = []

            watchdog = []

            while total != n:
                count = 0
                while total + biggest_squareNumber[index]*(count+1) <= n:
                    count += 1
                if count != 0:
                    total += biggest_squareNumber[index]*count
                    tmpsol.append(count)
                    watchdog.append(str(count) + ' * ' + str(biggest_squareNumber[index]))
                if n - total
                index += 1
            sol.append(sum(tmpsol))
            Wsol.append(watchdog)

        print(Wsol)
        return min(sol)

print(Solution().numSquares(43))