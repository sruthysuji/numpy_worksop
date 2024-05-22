# create a list as below
output=[[1,2,3],[4,5,6],[7,5,3,2,3,[2,[3]]]]
a=[1,2,3]
b=[4,5,6]
c=[7,5,3,2,3]
d=[2]
e=[3]
output = []
output.append(a)
output.append(b)
nestedlist = []
nestedlist.append(e)
nestedlist2 = []
nestedlist2.append(d)
nestedlist2.append(nestedlist)
final = c.copy()
final.extend(nestedlist)
output.append(final_list)
print(output)

# use these lists to create another list which will look like the list output in line 2

# use append method to do this.

