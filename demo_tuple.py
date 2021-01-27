"""元组的创建方式"""
"""第一种创建方式，使用()"""
t=("python","rabblt",98)
t2="python","rabbit",98 #可以省略小括号()
print(t2)
print(type(t2))
print(t)
print(type(t))
"""第一种创建方式，使用内置函数tuple()"""
t1=tuple(("python","rabblt",98))
print(t1)
print(type(t1))
print("----只包含一个元素的元组，需要使用逗号和小括号----")
t3=("python")
print(t3)
print(type(t3))
t3=("python",)
print(t3)
print(type(t3))
"""空元组的创建"""
lst=[]
lst1=list()
d={}
d1=dict()
t=()
t1=tuple()
print("空列表",lst,lst1)
print("空字典",d,d1)
print("空元组",t,t1)
print("----为什么要将元组设计成不可变序列----")
t=(2,[2,33],5)
print((t),type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
#t[1]=100 #元组是不允许修改元素的
#可以向列表中添加元素，并且列表的内存地址不变
t[1].append(100)
print(t[1],type(t[1]),id(t[1]))
print("----元组的遍历----")
t=("rabbit",34,[3,5,6])
print(t[0])
print(t[1])
print(t[2])
#print(t[3]) IndexError: tuple index out of range
"""遍历元组"""
for item in t:
    print(item)
print("----集合的创建方式----")
"""集合是没有value的字典，使用大括号{}"""
s={1,2,2,3,4,4,5} #集合中的元素不允许重复
print(s)
"""第二种创建方式，使用set()"""
s1=set(range(6))
print(s1,type(s1))
s2=set([1,2,3,3,4,5,5,6])
print(s2,type(s2))
s3=set((1,2,4,4,5,65))
print(s3,type(s3)) #集合中的元素是无序的
s4=set("rabbit")
print(s4,type(s4))
s5=set({1,2,2,34,56,6})
print(s5,type(s5))
print("----定义一个空集合----")
s6={} #dict字典类型
print(s6,type(s6))
s7=set()
print(s7,type(s7))


