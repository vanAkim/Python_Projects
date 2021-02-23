import math

def dot5(x):
        """ number -> number

        Return a rounded number bounded to 3 limits.
        Lower limit is set to 0 when input decimal part is between [0, 1/3[,
        middle limit is set to .5 when input decimal part is between [1/3, 2/3[,
        and upper limit is set to 1 when input decimal part is between [2/3, 1[.

        >>>dot5(66.3)
        66
        >>>dot5(66.5)
        66.5
        >>>dot5(66.9)
        67"""


        if x < math.floor(x) + 1/3:
                return math.floor(x)

        elif x < math.floor(x) + 2/3:
                return math.floor(x) + 0.5

        else:
                return math.ceil(x)


def dot3of5(x,limit):
        """ number -> number

        Return a rounded number bounded to 0.6 of limit.

        >>>dot3of5(76,25)
        75
        >>>dot3of5(89,25)
        75
        >>>dot3of5(90,25)
        100
        >>>dot3of5(94,25)
        100
        """


        if x < (x//limit) * limit + 3*limit/5:
                return (x//limit) * limit

        else:
                return (x//limit) * limit + limit