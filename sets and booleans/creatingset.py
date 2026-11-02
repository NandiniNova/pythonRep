x = set()
x.add(1)
print(x)
x.add(2)
print(x)
x.add(1) # 1 will print because sets contain only unique items
print(x)

list1 = [1,2,1,2,2,1,3,5,7,3,4,4,3,2,1]
print(set(list1))
