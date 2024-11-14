# """ print-> a[1,2,3,4,5] ==============================="""

# a=[1,2,3,4,5]
# #WHILE ------------------------
# # i=0
# # while i<len(a):
# #     print(a[i])
# #     i+=1
# #FOR --------------------------
# for i in a:
#     print(i)

# """ Sum of List -> [22, 44, 33, 51, 64]================="""

# a= [22, 44, 33, 51, 64 ]
# sum=0
# for i in a:
#     sum+=i
# print(sum)

# """find the largest number ============="""
# a=[22, 44, 33, 51, 64]

# largest=-99
# for i in a:
#     if i>largest:
#         largest=i
#     else:
#         largest=largest
# print(largest)

"""For loop ==================================================
1. Break keyword
2. Continue keyword
3. range() keyword
4. Nested for loop
"""

# flowers=["Lily","Mily","Rose","Cherry","Orchid"]
# for x in flowers:
#     if x=="Rose":
#         break
#     print(x) 

# flowers=["Lily","Mily","Rose","Cherry","Orchid"]
# for x in flowers:
#     if x=="Rose":
#         continue
#     print(x) 

#range() function----------------------------
#range(start, stop, step)
# flowers=["Lily","Mily","Rose","Cherry","Orchid"]
# for x in range(3,10,2):
#     print(x)

# for x in range(30,10,-2):
#     print(x)

colors=["White","Blue","Gray","Black"]
cars=["BMW","Audi","Toyota","Koinigsegg","Ferrari"]
for x in colors:
    for y in cars:
        print(x,y)





