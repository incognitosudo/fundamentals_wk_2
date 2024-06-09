#using python interactive shell input number of nth position and outputs the FB sequence 
def rFib(n):    #want it to return at <n> position in Fibonacci sequence
    if n == 0:   #base cases
        return 0
    elif n ==1 or n ==2:
        return 1
    return rFib(n-1) + rFib(n-2)
