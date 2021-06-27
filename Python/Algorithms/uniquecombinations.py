# This code file takes a list of numbers and generates
# the unique combinations depending on your input

class UniqueCombinations():

    def __init__(self, n, r, array):
        self.N = n
        self.R = r
        self.Set = array
      
    def __combinations(self, at, r, used, set):
        set = self.Set

        if r == 0:
            subset = []
            for i in range(0, len(set)):
                if used[i]:
                    subset.append(set[i])
            print(subset)

        else:
            for i in range(at, len(set)):
                if i > at and set[i - 1] == set[i]:
                    continue

            used[i] = True
            self.__combinations(i + 1, r - 1, used, set)
            used[i] = False
  
    def combinations(self):
        if self.Set is None:
            return
        if self.R < 0:
            return

        self.Set.sort()

        used = [False]*len(self.Set)
        self.__combinations(0, self.R, used, self.Set)


if __name__ == '__main__':
    set = []
    N = int(input('Enter number of entries: '))
    for i in range(N):
        entry = int(input(f'Input A[{i}]: '))
        set.append(entry)
    R = int(input('Enter number of items per combination: '))
    
    combo = UniqueCombinations(set, N, R)    
    combo.combinations()