# solve problem by saving data in an extra space to reduce time
def Fib(n):
    global F
    if n == 0 or n == 1:
        return 1
    result = F[n]
    if result == 0:
        result = Fib(n-1) + Fib(n-2)
        F[n] = result
    return result

def test():
    global F
    n = 7
    F = [0] * (n+1)
    print(Fib(n))

if __name__=="__main__":
    test()