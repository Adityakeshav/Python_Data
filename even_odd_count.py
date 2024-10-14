def count_even_odd(lst):
    # Your code goes here
    even=0
    odd=0
    for num in lst:
        if num%2==0:
            even=even+1
        else:
            odd+=1
    return (even,odd)
            
