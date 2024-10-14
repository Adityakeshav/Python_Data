def remove_duplicates(lst):
    # Your code goes here
    unique_list=[]
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
        
