n=int(input("Enter number of terms:"))
n1,n2=0,1
c=0
if n<=0:
    print("Enter positive number:")
elif n==1:
    print("Fibonaci sequence upto",n,":")
    print(n1)
else:
    print("Fibonaci sequence :")
    while c<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        c+=1