""" Snowball effect 
    Instagram: @probably_significant"""
import numpy as np

def play(m = 5, n = 5):
    if(m==0):
        return "Loss"
    elif(n==0):
        return "Win"
    p = m/(m+n)
    if(np.random.rand()<p):
        return play(m, n-1)
    return play(m-1,n)

win_counts = 0

m = 5
n = 4

for i in range(10000):
    if(play(m,n) == "Win"):
        win_counts += 1

print(win_counts/10000)