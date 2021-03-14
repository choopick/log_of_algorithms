def merge(list1, list2):
    mergedList = list()
    i = 0
    j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            mergedList.append(list1[i])
            i += 1
        else:
            mergedList.append(list2[j])
            j += 1
            
    mergedList = mergedList + list1[i:] + list2[j:]
    return mergedList

# 합병 정렬
def merge_sort(my_list):
    # base case
    if len(my_list) < 2:
        return my_list
    
    # divide my_list as left_half and right_half
    left_half = my_list[:len(my_list) // 2]
    right_half = my_list[len(my_list) // 2:]
    
    # merge_sort 함수를 재귀적으로 호출하여 부분 문제 해결(conquer)하고,
    # merge 함수로 정렬된 두 리스트를 합쳐(combine)준다.
    return merge(merge_sort(left_half), merge_sort(right_half))
    

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
