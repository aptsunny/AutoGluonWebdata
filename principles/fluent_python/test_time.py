import time
from decimal import *
from functools import wraps
import random

def timeit_warpper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        # start = time.perf_counter()
        func_return_val = func(*args, **kwargs)
        end = time.perf_counter()
        print('{0:<10}.{1:<8} : {2:<8}'.format(func.__module__, func.__name__, end - start))
        return func_return_val
    return wrapper


@timeit_warpper
def exp(x):
    getcontext().prec +=2
    i, lasts, s, fact, num = 0,0,1,1,1
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num / fact
    getcontext().prec -=2
    return +s

def exp_time():
    print('{0:<10}.{1:<8} : {2:<8}'.format('module', 'function', 'time'))
    exp(Decimal(20))
    exp(Decimal(40))
    exp(Decimal(50))
    return

def lru_cache():
    import functools
    #
    @functools.lru_cache(maxsize=12)
    def slow_func(x,y):
        time.sleep(2)
        print(y)
        return x
    slow_func(1,5)
    slow_func(1,6)
    slow_func(3,7)
    return

def fast_function():
    r = random.random
    for i in range(1000):
        print(r()) # 在这里调用'r()', 比全局的 random.random()快

if __name__ == '__main__':
    exp_time()
    lru_cache()
    fast_function()
