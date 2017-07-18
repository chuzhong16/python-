list1=[1,2,3,4,5]
list2=[6,7,8,9,0]
list3=[7,8,9,2,1]
r=map(lambda x,y,z:x+y+z,list1,list2,list3)
print(list(r))