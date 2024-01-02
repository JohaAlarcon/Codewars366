def longest (a1, a2):
    
    unique_letters = set (a1+a2)
    result = '' .join(sorted(unique_letters))
    
    return result