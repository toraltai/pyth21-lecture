arr = [22,14,515,12,41,414,[24,13,[90,65],177]]
def unpack(lst, level=1):
    print(*lst, 'level =', level)
    for i in lst:
        if type(i) == list:
            unpack(i,level+1)
unpack(arr)