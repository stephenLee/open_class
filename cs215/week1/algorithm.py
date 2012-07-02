"""def algorithm_development(problem_spec):
       correct = False
       while not correct or not fast_enough(running_time)
           algorithm = devise_algorithm(problem_spec)
           correct = analyse_efficiency(algorithm)
           running_time = analyse_efficency(algorithm)
       return algorithm
"""

def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

def russian(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1:
            z = z + y
        y = y << 1
        x = x >> 1
    return z

def rec_russian(a, b):
    if a == 0:
        return 0
    if a % 2 == 0:
        return 2 * rec_russian(a/2, b)
    return b + 2 * rec_russian((a-1)/2, b)


def main():
    from timeit import Timer
    t1 = Timer("naive(100,100)", "from __main__ import naive")
    print "naive test: naive(100,100) is %s and cost time is %s" % (naive(100,100), t1.timeit())
    t2 = Timer("russian(100,100)", "from __main__ import russian")
    print "russian test: russian(100,100) is %s and cost time it %s" % (russian(100,100), t2.timeit())
    t3 = Timer("rec_russian(100,100)", "from __main__ import rec_russian")
    print "rec_russian test: rec_russian(100,100) is %s and cost time is %s" % (rec_russian(100,100), t3.timeit())

if __name__ == '__main__':
    main()
