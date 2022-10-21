# import random
# magic = random.randint(1,101)
# scorp_mode = -1

# while 

s = set()
for word in input().split():
    if word in s:
        print("YES")
    else:
        print("NO")
        s.add(word)