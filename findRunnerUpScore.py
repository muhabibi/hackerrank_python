from collections import Counter 
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    #sort array
    result = sorted(arr,reverse=True)
    
    #instantiation
    counterR = Counter(result)
    
    #return keys [1] from sorted dict (sorted by key desc)
    print(list(counterR.keys())[1])
