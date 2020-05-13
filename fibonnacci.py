import time

def fib1(n):
    if n == 0 or n ==1:
        return n
    return fib1(n-1) + fib1(n-2)

def fib2(n):
    if n not in memory:
        memory[n] = fib2(n -1) + fib2( n -2)
    return memory[n]

arg = 900

memory = {}
memory[0] = 0
memory [1] = 1

start = time.time()
result = fib2(arg)
print(f"fib2({arg}) = {result}, took {time.time()- start}sec()")


#start = time.time()
#result = fib1(arg)
#print(f"fib1({arg}) = {result}, took {time.time()- start}sec()")


