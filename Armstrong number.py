n=int(input("Enter Number:"))
sum=0
x=n
while x>0:
    a=x%10
    sum+=a**3
    x//=10
if n==sum:
    print(n,"Is an Armstrong number")
else:
    print(n,"Is not an Armstrong number")
    