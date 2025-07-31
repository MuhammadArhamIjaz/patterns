print("Half pyramid pattern of stars")
n=int(input("Enter the number of rows you want to print"))
      #outer loop for rows
for i in range(n):
#inner loop for colums
 for j in range(i+1):
   print("* ",end="")
 print()