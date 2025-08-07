# Day 7: Time Complexity Explorer – Python Simulation of Big O

import time

# O(1) - Constant Time
def constant_time():
    start = time.time()
    result = 42 + 58  # simple constant-time operation
    end = time.time()
    print(f"O(1) Time: {end - start:.8f} seconds")

# O(n) - Linear Time
def linear_time(n):
    start = time.time()
    for i in range(n):
        pass
    end = time.time()
    print(f"O(n) Time for n={n}: {end - start:.8f} seconds")

# O(n^2) - Quadratic Time
def quadratic_time(n):
    start = time.time()
    for i in range(n):
        for j in range(n):
            pass
    end = time.time()
    print(f"O(n^2) Time for n={n}: {end - start:.8f} seconds")

# O(log n) - Logarithmic Time
def logarithmic_time(n):
    start = time.time()
    while n > 1:
        n = n // 2
    end = time.time()
    print(f"O(log n) Time: {end - start:.8f} seconds")


#ng
