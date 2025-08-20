#create the empty list
my_list=[]
#append the given numbers
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insert 15 at index 1
my_list.insert(1,15)
#extend with given list
my_list.extend([50,60,70])
#remove the last element
my_list.pop()
#sort in ascending order
my_list.sort()
#find and print index of 30
index_of_30=my_list.index(30)
print("Index of 30 is:",index_of_30)