n=int(input())
odd=0
even=0

for i in range(0,7):
    m=int(input("Enter Input : "))
    if(m%2==0):
        even=even+m*m
    else:
        odd=odd+m*m

print(even,odd)   
