n=int(input("Enter number of terms:"))
s=0
for i in range(1,n+1):
    s+=i*i*i
print("Sum of squares is:",s)