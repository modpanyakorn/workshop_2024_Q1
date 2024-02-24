from newton import NewtonMethod

def test_nt_mt_quadratic():
    f = lambda x: x**2 - 4
    df = lambda x: 2*x
    nm = NewtonMethod(f, df)
    assert round(nm.solve(10, 1e-10, 100), 10) == 2
    assert round(nm.solve(-10, 1e-10, 100), 10) == -2