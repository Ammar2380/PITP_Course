# a = [1,2,3,4,5,6,7]
# b = map(lambda x:x%2==0,a)
# print(list(b)) 
a = [1,2,3,4,5,6,7]
b = filter(lambda x:x%2==0,a)
print(list(b)) # only those who are even like name filter

# map : works like for loop visit each
# filter : filter data according to condition