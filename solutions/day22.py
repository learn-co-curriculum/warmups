def solution_create_pmf(lst):
    n = len(lst)
    d = {}
    for event in lst:
        d[event] = d.get(event, 0) + 1
    
    for k, v in d.items():
        d[k] = v/n
    return d
