def mergeAndSortLists(list1,list2):
    new_list = list1 + list2
    new_list = list(set(new_list))
    return sorted(new_list)


A = [1,2,3,415,2,43,2,2,20 ,21, 23]
B = [1,2,3,412,3,5,2,10,9, 23]

print(mergeAndSortLists(A,B))