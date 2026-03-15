# simple array sum
arr =[]
n=int(input("Enter the number of Elements"))
count=0
for i in range(n):
  a=int(input("Enter the number "))
  arr.append(a)
for i in range(n):
    count+=arr[i]
print(count)

#min and max array 
arr =[]
n=int(input("Enter the number of Elements"))
for i in range(n):
  a=int(input("Enter the number "))
  arr.append(a)
arr=sorted(arr)
print(arr[0],arr[n-1])

#remove duplicated from unsorted array
def removeduplicates(arr):
    b=[]
    for i in arr:
        if i not in b:
            b.append(i)
    return b
if __name__ == '__main__':
    arr = [int(x) for x in input("Enter elements in series").split()]
    print(removeduplicates(arr))

#pattern
def pattern(n):
    b=[]
    for i in arr:
        if i not in b:
            b.append(i)
    return b
if __name__ == '__main__':
    n = [int(x) for x in input("Enter number").split()]
    print(pattern(n))

#pattern
n=int(input())
a=1
for i in range(n):
    a+=2
a-=2
for i in range(1,n+1):
    if i==3:
        a-=2
        continue
    print(i , i+a)
    a-=2

#alternate negative positive
n = int(input("Enter the number of Elements: "))
a = []
for i in range(n):
    v = int(input("Enter the number: "))
    a.append(v)
neg = []
pos = []
for x in a:
    if x < 0:
        neg.append(x)
    else:
        pos.append(x)
b = []
i = 0
j = 0
while i < len(neg) and j < len(pos):
    b.append(neg[i])
    b.append(pos[j])
    i += 1
    j += 1
while i < len(neg):
    b.append(neg[i])
    i += 1
while j < len(pos):
    b.append(pos[j])
    j += 1
print(b)
    



    
