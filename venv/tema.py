import numpy as np

n = int(input("Enter the number of rows and columns: "))

print("Enter the entries in a single line (separated by space): ")
# User input of entries in a single line separated by space
entries = list(map(str, input().split()))
# For printing the matrix
matrix1 = np.array(entries).reshape(n, n)
print(matrix1)

dimension = matrix1.shape
print("Dimension is " + str(dimension))
# User input of entries in a single line separated by space
print("Enter the second matrix element in a single line (separated by space):  ")
entries = list(map(str, input().split()))
# For printing the matrix
matrix2 = np.array(entries).reshape(n, n)
print(matrix2)
#Creating empty list where the results of the concatenated matrices will be stored
result = []
#Transforming the matrices in lists to be easier to work with
m1 = matrix1.flatten()
m2 = matrix2.flatten()
#The length of the lists
ran = n*n
#Travesting the lists and concatenating the elements of the matrices and adding them to the result list
for i in range(ran):
    result.append(m1[i]+m2[i])

#Reshaping the list into a matrix
result = np.array(result).reshape(n,n)
print("The result is: ")
print(result)

#Accessing a string from the matrix through its position
i = int(input("Enter the row of the string you want to acces: "))
j = int(input("Enter the column of the string you want to acces: "))
print("The string at position [" + str(i) + "]" + "[" + str (j) + "] is " + matrix1[i][j])
word = str(input("Enter the string you want to search: "))
#Intializing the firs and the last rows and columns where we find the string
lrow = lcolumn = frow = fcolumn  = 0
a = 0
#a = number of total appearances of the string in the matrix
#Creating two lists to store the rows and the columns where the string is found
row = []
column = []

#Traversing the first matrix searching for the string
for i in range(n):
    for j in range(n):
        #storing the position where we find the string as the last until we found a new one and replace it
        if matrix1[i][j] == word:
            a=a+1
            lrow = i
            lcolumn = j
            row.append(i)
            column.append(j)
        #storing the position where the string first appears
        if matrix1[i][j] == word and a == 1:
            frow = i
            fcolumn = j
#If the number of appearances is 0 then the string is not in the matrix
if a == 0:
    print("The string was not found.")
else:
    print("First occurrence at position " + "[" + str(frow) + "]" + "[" + str (fcolumn) + "]")
    print("Last occurrence at position " + "[" + str(lrow) + "]" + "[" + str (lcolumn) + "]")
    print("The string is found on following positions: ")
    for i in range(len(row)):
        print("[" + str(row[i]) + "]" + "[" + str (column[i]) + "]")
#Creating a list where the values that we will multiply the matrix will be stored
val = []
#Traversing the matrix item by item
for i in range(len(m2)):
    m = m2[i]
    res = 0
    for j in range(len(m)):
        #if the difference of the letter and 'a' is greater than 10, letters from j to the end
        if ord(m[j])-ord('a')>9:
            res = res*100+ord(m[j])-ord('a')
        else:
            res = res*10 + ord(m[j])-ord('a')
    #adding the numbers to the list
    val.append(res)
#Empty list for the resulted matrix through multiply
res1 = []
#Storing the element resultet through multiplying the elements of the first matrix
for i in range(len(m1)):
    res1.append(m1[i] * val[i])

#Reshaping the list into a matrix
res1 = np.array(res1).reshape(n,n)
print(res1)
#Intializing the number of elements that are greater in the first than its equivalent in the second matrix
m1c = m2c = 0
for i in range(len(m1)):
    #Comparing the item from the first matrix with the element on the same position from the second
    if m1[i] > m2[i]:
            m1c = m1c+1
    else:
        if m2[i] > m1[i]:
            m2c = m2c+1
if m1c > m2c:
    print("The first matrix is greater than the second.")
else:
    if  m2c == m1c:
        print("The matrices are equal.")
    else:
        print("The second matrix is greater than the first.")