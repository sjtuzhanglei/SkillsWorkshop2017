from __future__ import print_function

# using generators here as we don't know how long we'll need to run the loop
# this creates a "stream" of fibonacci numbers that we can test for evenness

def fib(limit=4000000):
    F = []
    i = 0
    while True:
        if i > 1:
            F.append(F[i - 1] + F[i - 2])
        elif i == 0:
            F.append(1)
        elif i == 1:
            F.append(2)
        i += 1
        if F[-1] < limit:
            yield F[-1]
        else:
            return

print(sum(x for x in fib() if x % 2 == 0))
