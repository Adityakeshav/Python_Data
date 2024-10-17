def max_consecutive_difference(lst):
    # Initialize an empty list to store differences
    diff_lst = []
    if len(lst)<2:
        return 0
    for i in range(len(lst) - 1):
        diff = abs(lst[i] - lst[i + 1])
        diff_lst.append(diff)
    
    sorted_diff_lst = sorted(diff_lst)
    
    return sorted_diff_lst[-1] 