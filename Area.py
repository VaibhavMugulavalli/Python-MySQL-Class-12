print("A:Area of Circle",'\n',"B:Area of Reactangle",'\n',"C:Area of Square",'\n',"D:Circumfrence of Circle")
cha=input("Enter option:")
if cha=='A' or cha=='a':
    a=int(input("Enter radius of circle:"))
    areac=3.15*(a*a)
print("Area is:",areac)
elif cha=='B' or cha=='b':
    b=int(input("Enter length"))
    c=int(input("Enter breadth:"))
    arear=a*b
print("Area is:",arear)
elif cha=='C' or cha=='c':
    d=int(input("Enter side of square:"))
print("Area is:",d*d)
elif cha=='D' or cha=='d':
    e=int(input("Enter radius of circle"))
print("Area is:",6.28*e)
else:
    print("Error")