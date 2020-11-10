class Solution:
    def buddyStrings(self, A, B):
        if A == "":
            return False
        elif len(A) != len(B):
            return False
        elif A == B[::-1]:
            return True

        first_stop = self.stop(A,B)
        second_stop = self.stop(A[first_stop+1:],B[first_stop+1:]) + first_stop + 1
        if second_stop > len(A)-1:
            return False
        else:
            print(A[:first_stop] + A[second_stop] + A[first_stop+1:second_stop] + A[first_stop] + A[second_stop+1:])
            return [False,True][A[:first_stop] + A[second_stop] + A[first_stop+1:second_stop] + A[first_stop] + A[second_stop+1:] == B]

    def stop(self,A,B):
        radical = ''
        stop = 0
        for letter in A:
            found_index = B.find(radical)
            stop = found_index + len(radical)
            if found_index == -1:
                break
            radical += letter
        return stop

print(Solution().buddyStrings("aaab","aaab"))