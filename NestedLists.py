#https://www.hackerrank.com/challenges/nested-list/problem

d={} 
for _ in range(int(input())): 
    try:
        Name=input() 
        Grade=float(input()) 
        d[Name]=Grade 
    except Name < 2 or N > 5:
        print("N<2 or N>5 not allowed")
        sys.exit()
        
v= d.values()
second = sorted(list(set(v)))[1]

second_lowest = []
for key,val in d.items():
    if val == second:
        second_lowest.append(key)
for name in sorted(second_lowest):
    print(name)
