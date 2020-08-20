from collections import defaultdict

def even_odd_solution(lst):
    d = defaultdict(list)
    for n in lst:
        if n%2==0:
            d['evens'].append(n)
        else:
            d['odds'].append(n)
    return dict(d)