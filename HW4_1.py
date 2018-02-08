import math

def main(S, k):
    print(S)
    print(k)
    if k <= len(S):
        counter = 0
        mid = math.floor(len(S)/2)
        distance = math.floor(k/2)
        print(counter)
    elif k > len(S) :
        print("MUST BE LESS THAN SIZE S")
    elif k <= 0:
        print("USE POSTIVE INT ONLY")
    
