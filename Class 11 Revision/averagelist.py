list1=[]
n=int(input("Enter number of terms:"))
for i in range(0,n):
    ele=int(input())
    list1.append(ele)
print(list1)
print("Average is:",sum(list1)/len(list1))
