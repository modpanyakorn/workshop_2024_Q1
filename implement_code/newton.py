class NewtonMethod:
    def __init__(self, f, df):
        self.f = f
        self.df = df
        
    def display(self, x):   
        print(f"final x = {self.f(x)}")
        print(f"final f({x}) = {self.df(x)}")
        
    def solve(self, x, tol = 1e-6, max_iter = 100):
        for i in range(max_iter):
            if self.df(x) == 0:
                print('df(x) is zero')
                break
            
            x = x - self.f(x) / self.df(x) 
            self.display(x) # call function in class use 'self.function'
            
            if abs(self.f(x)) < tol:
                break
            
        return x
    