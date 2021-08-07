# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 01:34:31 2021

@author: snakk
"""

import math

def combination(n):
    if n==1:
        return 0
    C= math.factorial(n)/(2*math.factorial(n-2))
    return C

def nearlySimilar(sides_rows: int, sides: list):
    assert len(sides) == sides_rows and len(sides[0]) == 2, "Dims don't match"
    
    pairs= 0
    checks= 1
    check= [False for i in range(sides_rows)]
    
    for i in range(sides_rows):
        if check[i]== True:
            continue
        for j in range(i+1, sides_rows):
            if check[j]== True:
                continue
            if sides[i][0]/sides[j][0]== sides[i][1]/sides[j][1]:
                check[j]= True
                checks+=1
        pairs= combination(checks)
        checks= 1
    
    return int(pairs)


def nearlySimilarNaive(sides_rows: int, sides: list):
    assert len(sides) == sides_rows and len(sides[0]) == 2, "Dims don't match"
    
    pairs= 0
    
    for i in range(sides_rows):
        for j in range(i+1, sides_rows):
            if sides[i][0]/sides[j][0]== sides[i][1]/sides[j][1]:
                pairs+=1
            
    return pairs


def stresstest():
    import random
    okcounter=0
    while True:
        sides_rows= random.randint(1, 1000)
        sides= [[0]*2]*sides_rows
        for i in range(sides_rows):
            for j in range(2):
                sides[i][j]= random.randint(1,10**15)
        print(f'sides_rows= {sides_rows}, Result1= {nearlySimilar(sides_rows, sides)}')
        print(f'sides_rows= {sides_rows}, Result1= {nearlySimilarNaive(sides_rows, sides)}')

        if nearlySimilar(sides_rows, sides)== nearlySimilarNaive(sides_rows, sides):
            okcounter= okcounter+1
            print('ok\n')
            if okcounter>=100:
                break

        else: 
            print('Error')
            break
        
stresstest()

def timecounter(func1, func2, number):
    from timeit import timeit
    import random
    sides_rows= random.randint(1, 1000)
    sides= [[0]*2]*sides_rows
    for i in range(sides_rows):
        for j in range(2):
            sides[i][j]= random.randint(1,10**15)
            
    time1= timeit(lambda: nearlySimilar(sides_rows, sides), number= number)
    time2= timeit(lambda: nearlySimilarNaive(sides_rows, sides), number=number)

    time= {"Time1": round(time1,4),"Time2": round(time2,4)}
    
    min= "Time1"
    for key in time:
        if time[key]<time[min]:
            min= key
    
    for key in time:
        if time[key]==time[min]:
            print(f'The fastest is {key}!\n')
        
    return time

print(timecounter(nearlySimilar, nearlySimilarNaive, number= 10000))

# =============================================================================
#Some testcases................................................................
# print(nearlySimilar(sides_rows= 3, sides= [[4,8],[15,30],[25,50]]))
# print(nearlySimilarNaive(sides_rows= 3, sides= [[4,8],[15,30],[25,50]]))
# print(nearlySimilar(sides_rows= 5, sides= [[2,1],[10,7],[9,5],[6,9],[7,3]]))
# print(nearlySimilarNaive(sides_rows= 5, sides= [[2,1],[10,7],[9,5],[6,9],[7,3]]))
# =============================================================================
    