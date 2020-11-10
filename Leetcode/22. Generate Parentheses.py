

n = 5

a = "("
b = ")"

class moovingPattern:
    def __init__(self, a, b, dimensionOfAnswer):
        self.dimension = dimensionOfAnswer
        self.a = a
        self.b = b

    def moovingTable(self):
        initialSolution = self.a + self.b*(self.dimension-1)

        solution = []
        solution.append(initialSolution)
        i = 0

        while i != self.dimension-1:
            initialSolution = initialSolution[-1] + initialSolution[0:self.dimension-1]
            solution.append(initialSolution)
            i += 1
        return solution

class callingPattern:
    import re
    def __init__(self,a,b,dimension):
        self.dimension = dimension
        self.a = a
        self.b = b

    def add_bCol(self,initialPattern,indexToInsert):
        return initialPattern[:indexToInsert+1] + self.b + initialPattern[indexToInsert + 1:]

    def callingTable(self):
        #full a
        initialSolution = self.a * (self.dimension -2)
        post = moovingPattern(self.a, self.b, self.dimension).moovingTable()
        solution = []

        for string in post:
           solution.append(self.a + initialSolution + string + self.b)

        #Composed a/b
        n_b_avant = 0
        for col_a in range(self.dimension - 2): # déplace le b initial d'une colonne
            ##### Instance avec un seul b
            initial_calling = callingPattern(self.a, self.b, self.dimension).add_bCol(initialSolution, col_a - 1)
            n_b_avant += 1
            post = moovingPattern(self.a, self.b, self.dimension - 1).moovingTable()
            actual_prefix = initial_calling

            for string in post:
                solution.append(self.a + initial_calling + string + self.b)

            ##### Instance avec plusieurs b
            alt_col_b = col_a
            alt_n_b_avant = n_b_avant #avant suffixe
            alt_calling = actual_prefix

            while self.dimension - 2 - alt_n_b_avant > 0: # il y a des aa
                alt_calling = callingPattern(self.a, self.b, self.dimension).add_bCol(alt_calling, alt_col_b + 1)
                alt_n_b_avant += 1
                alt_col_b += 2
                post = moovingPattern(self.a, self.b, self.dimension - alt_n_b_avant).moovingTable()

                if self.dimension - 2 - alt_n_b_avant > 0: #il y a encore des aa
                    partial_calling = moovingPattern(self.b, self.a, self.dimension - alt_n_b_avant).moovingTable()
                else:
                    partial_calling = [alt_calling[alt_col_b:]]


                for index,string_calling in enumerate(partial_calling):
                    altDual_calling = alt_calling[:alt_col_b] + string_calling
                    print(alt_col_b,index,altDual_calling, post)

                    if len(partial_calling) > 1:
                        True

                    for string in post:
                        solution.append(self.a + altDual_calling + string + self.b)

        return solution





print(callingPattern("a","b",n).callingTable())