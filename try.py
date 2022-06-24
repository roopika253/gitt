test=int(input())
#holaa
while(test!=0):
    
        
    n=int(input())
    w=list(map(int,input().split()))
    w=w.sort()
    print(w)
    p=0

    for i in range(n):
        p=p+w[i]
        w.pop(0)
        for j in range(len(w)):
            if w[j]>0:
                w[j]=w[j]-1
    print(p)
            
