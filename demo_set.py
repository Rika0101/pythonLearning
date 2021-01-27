#集合的相关操作
s={10,20,30,100}
"""集合元素的判断操作 in or not in"""
print(10 in s)
print(90 in s)
print(10 not in s)
print(90 not in s)
print("---集合元素的添加操作---")
s.add(60) #添加一个元素
print(s)
s.update([20,100,15]) #可至少添加一个元素  添加列表
print(s)
s.update({12,34,5}) #添加集合
print(s)
s.update((50,40,2)) #添加元组
print(s)
print("---集合元素的删除操作---")
s.remove(60)  #一次删除一个指定元素，如果指定元素不存在则抛出keyerror
print(s)
#s.remove(105) KeyError: 105
s.discard(100) #一次删除一个指定元素，如果指定元素不存在不抛出异常
print(s)
s.discard(105)
print(s)
s.pop() #一次只删除一个任意元素
print(s)
s.pop()
print(s)
#s.pop(40) TypeError: pop() takes no arguments (1 given) 元素不能进行指定
s.clear() #清空集合
print(s)
#集合间的关系
print("---两个集合是否相等，元素相同就相等---")
s={10,20,30,40}
s2={40,30,20,10}
print(s==s2) #True
print(s!=s2) #False
print("---一个集合是否是另一个集合的子集---")
s1={10,20,30,40,50,60}
s2={10,20,30}
s3={10,20,90}
print(s2.issubset(s1)) #True
print(s3.issubset(s1)) #False
print("---一个集合是否是另一个集合的超集---")
print(s1.issuperset(s2)) #True
print(s1.issuperset(s3)) #False
print("---两个集合是否含有交集---")
print(s2.isdisjoint(s1)) #False 两个集合含有交集
s4={100,200,300}
print(s2.isdisjoint(s4)) #True 两个集合不含有交集
#集合的数学操作
print("---交集操作---")
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s2.intersection(s1))
print(s2 & s1)   # intersection与＆等价  交集操作
print("---并集操作---")
print(s1.union(s2))
print(s1 | s2)  # union与|等价，并集操作
print("---差集操作---")
print(s2.difference(s1))
print(s2-s1)  #difference与—等价，差集操作
print(s2.symmetric_difference(s1))
print(s2 ^ s1) #symmetric_difference 与^等价，对称差集操作
print("---集合生成式---")
lst=[i*i for i in range(10)]
print(lst)
s={i*i for i in range(10)}
print(s)
