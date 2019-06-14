a=[1,2,3,4]
b=a
print(a is b)
c=[9,8,7,1]
print(c is a)
v=b[2]*10
print(v)
print(a[1:3])
print(a[3:3])
a[4:5]=['x','y','z']
print(a)
fruits=['apple','banana','chikoo','mango','orange']
fruits.append('guava')
fruits.extend(['litchi','dragonfruit'])
fruits.insert(2,'pineapple')
fruits.remove('apple')
print(fruits)
print(fruits.pop(3))
fruits.sort()
print(fruits)
