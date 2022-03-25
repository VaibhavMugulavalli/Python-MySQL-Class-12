marks=[]
n=int(input("Enter number of subjects:"))
for i in range(0,n):
    ele=int(input())
    marks.append(ele)
print(marks)
marksum=sum(marks)
avg=sum(marks)/5
print("Sum of marks is:",marksum)
print("Average marks are:",avg)
if avg >=91:
    print("Grade:A1")
elif avg>=81 and avg<=90:
    print("Grade:A2")
elif avg>=71 and avg<=80:
    print("Grade:B1")
elif avg>=61 and avg<=70:
    print("Grade:B2")
elif avg>=51 and avg<=60:
    print("Grade:C1")
elif avg>=41 and avg<=50:
    print("Grade:C2")
elif avg>=33 and avg<=40:
    print("Grade:D")
else:
    print("Grade:E")
    