from newton import NewtonMethod

def f(x):
    return x ** 3 - 4
    # return 1

def df(x):
    return 3 * x ** 2

x = 10
f_x = f(x)
df_x = df(x)

nt_mt1 = NewtonMethod(f, df)
nt_mt1.solve(x, 1e-10, 100)
