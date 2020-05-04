rows, cols = (5, 5)
arr=[]
for i in range(cols):
    col = []
    for j in range(rows):
        col.append(myTinyCell())
    arr.append(col)
print(arr)

arr[0][0] = 100

print(arr)
