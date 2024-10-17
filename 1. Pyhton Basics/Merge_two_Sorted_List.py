def merge_two_sorted_lists(list1, list2):
    # Your code goes here
    merged_lst=[]
    for num in list1:
        merged_lst.append(num)
        
    for num in list2:
        merged_lst.append(num)
    return sorted(merged_lst)
