import random
import time
arr = [1,2,3,4,5,6,7,8,9,10]
# o = arr
# random.shuffle(o)

def is_sorted(ar):
    shorted = True
    for i in range(len(ar)-1):
        if ar[i]>ar[i+1]:
            shorted = False
    return shorted

def monkeySort(arr):
    while not is_sorted(arr):
        # time.sleep(0.5)
        random.shuffle(arr)
        print(arr)
    print(arr)

monkeySort([6,5,4,7,9,1,3,2,8])