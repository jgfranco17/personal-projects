# This code is my personal attempt at a knapsack algorithm
# using Object-Oriented Programming structure in Python; it's
# designed to be open-ended and accept different parameters

class Knapsack:
    def __init__(self):
        pass
        
    def get_items(self):
        max_weight = int(input('Enter max weight: '))
        items = int(input('Enter number of items: '))
        values = []
        weights = []
        for i in range(items):
            weights.append(int(input(f'Item {i+1} weight = ')))
            values.append(int(input(f'Item {i+1} value = ')))
        self.max_weight = max_weight
        self.weights = weights
        self.values = values
        self.items = items
        
        mw = self.max_weight
        w = self.weights
        v = self.values
        n = self.items
        solution = [[0 for x in range(mw + 1)] for x in range(n + 1)] 

        for i in range(n + 1): 
            for j in range(mw + 1): 
                if i == 0 or j == 0: 
                    solution[i][j] = 0
                elif w[i-1] <= j: 
                    solution[i][j] = max(v[i-1]+solution[i-1][j-w[i-1]], solution[i-1][j]) 
                else: 
                    solution[i][j] = solution[i-1][j]
                    
        return solution[n][mw]
        
    def optimize(self): 
        mw = self.max_weight
        w = self.weights
        v = self.values
        n = self.items
        solution = [[0 for x in range(mw + 1)] for x in range(n + 1)] 

        for i in range(n + 1): 
            for j in range(mw + 1): 
                if i == 0 or j == 0: 
                    solution[i][j] = 0
                elif w[i-1] <= j: 
                    solution[i][j] = max(v[i-1]+solution[i-1][j-w[i-1]], solution[i-1][j]) 
                else: 
                    solution[i][j] = solution[i-1][j] 
  
        return solution[n][mw]
    
    def pack_info(self): 
        print('\nKNAPSACK INFORMATION:')
        print(f'Maximum capacity: {self.max_weight}\nItem count: {self.items}')
        for i in range(self.items):
            print(f'Item {i+1}: Weight = {self.weights[i]}, Value = {self.values[i]}')
    
    def item_info(self): 
        i = int(input('Enter item number: '))
        try:
            print(f'\nITEM INFORMATION {i}: Weight = {self.weights[i-1]}, Value = {self.values[i-1]}')
        except Exception:
            print(f'There are only {self.items} items in the set, invalid index.')        
    
    def result(self):
        final = self.optimize()
        print(f"The optimum value is: {str(final)}")

# This is just to run a demo 
knapsack = Knapsack()
knapsack.get_items()
knapsack.pack_info()
knapsack.result()
