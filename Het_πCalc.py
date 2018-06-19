from time import time
import math
lnum = 0
pic = 0
start = time()
##while True:
##    global a,lnum
##    while lnum < 1001:
##        pi = a*(math.sqrt((1/2)-math.cos(360/a)))
##        a += 1
##        lnum += 1
##    print("Here is pi:",pi)
##    print("Number of repetitions:",a)
##    print("Time Elasped from the beginning",time()-start)
################################################################################
"""
This is the function versrion, the one that uses functions.
"""
benchmarks = set()
benchmarks = [1,10,100,1000,10000,100000,1000000,10000000]
def picalc(n):
    global pic
    pic = n*(math.sqrt((1/2)-math.cos(360/n)))
    print("Time from start:", time()-start)
    return int(pic)

for i in range(len(benchmarks)):#This part just runs the benchmarks
    print(picalc(benchmarks[i]))
