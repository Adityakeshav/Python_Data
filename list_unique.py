def check_unique(lst):
    # Convert list to set to remove duplicates and compare lengths
    set_lst = set(lst)
    return len(set_lst) == len(lst)
    
