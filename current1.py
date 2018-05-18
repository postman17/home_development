def modify_list(l):
    sp=[]
    for x in l:
        if x%2==0:
            sp.append(int(x/2))
    l.clear()
    for y in sp:
        l.append(y)        
    return l

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))
modify_list(lst)
print(lst)

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
