# """While Loop-------------------------------------"""

# # 1. Initial value
# # 2. Condition
# # 3. Block of code
# # 4.Increment/Decrement

# count=1
# while (count<=50):
#     if (count%2==0):
#         print(count,"is even")
#     else:
#         pass
#     count+=1
# print("Good bye")
    
"""Nested While-----------------------------------"""

# #break statement----------------------
# count=1
# while True:
#     print("Break",count)
#     count+=1
#     if count==6:
#         break

# #continue statement-------------------
# count=0
# while count<6:
#     count+=1
#     if count==3:
#         continue
#     print("continue: ",count)


outer=1
while outer<=5:
    #outer+=1          #outer starts with 2
    inner=1
    while inner<=5:
        print(outer,"*",inner,"=",outer*inner)
        inner+=1
    print("inner loop terminated")
    outer+=1           #Outer starts with 1
print("outer loop terminated")


