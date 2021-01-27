lst = ["hello", "world", 98, "hello", 235]
# 获取索引为2的元素
print(lst[2])
print(lst[-4])
#print(lst[7]) list index out of range
#正向索引范围为 0到n-1;  负向索引范围为 -1到-n
lst=[10,20,30,40,50,60,70,80]
#start=1,stop=6,step=1
#print(lst[1:6:1])
print("original list:",id(lst))
lst2=lst[1:6:1]
print("切的片段:",id(lst2))
print(lst[1:6])#默认步长为1
print(lst[1:6:])#默认步长为1
#start=1, stop=6,step=2
print(lst[1:6:2])
# stop=6,step=2, start采用默认
print(lst[:6:2])
# start=1,step=2, stop采用默认
print(lst[1::2])
print("---------------step为负的情况-------------------")
print("original list:",lst)
print(lst[::-1])
print(lst[7::-1])
print(lst[:0:-1])
print(lst[6:0:-2])


lst=[10,20,"python","hello"]
print(10 in lst)
print(10 not in lst)
print(100 not in lst)
print(100 in lst)
print("------------------")
for item in lst:  #列表元素的遍历 for in
    print(item)
    print("------列表元素的增加操作--------")
#向列表的末尾添加一个元素 lst.append  添加前后仍然是同一个列表
lst=[10,20,30]
print("before",lst,id(lst))
lst.append(100)
print("after",lst,id(lst))
lst2=["hello","world"]
lst.append(lst2) #将lst2作为一个元素添加到列表的末尾
print(lst)
#在列表的末尾一次性添加多个元素 lst.extend
lst.extend(lst2)
print(lst)
#在任意一个位置上添加一个元素 lst.insert
lst.insert(1,90)
print(lst)
#在任意位置上添加多个元素  切片
lst2=[True,False,"hello"]
lst[1:]=lst2
print(lst)
print("------列表元素的删除操作--------")
lst=[10,20,30,40,50,60,30]
lst.remove(30) #从列表中移除一个元素，如果有重复元素只移除第一个元素 lst.remove
print(lst)
#lst.remove(100)
#print(lst) ValueError: list.remove(x): x not in list
lst.pop(1) #根据index移除元素
print(lst)
#lst.pop(5)
#print(lst) IndexError: pop index out of range
lst.pop() #如果不指定参数（index），将删除列表中最后一个元素
print(lst)
print("-------切片操作，至少删除一个元素，将产生一个新的列表对象----------")
new_list=lst[1:3]
print("original list",lst)
print("切片后的列表",new_list)
#不产生新的列表对象，而是删除原列表中的内容
lst[1:3]=[]
print(lst)
lst.clear() #清除列表中的所有元素 lst.clear
print(lst)
#del 语句 将列表整个删除
del lst
print("------列表元素的修改操作--------")
lst=[10,20,30,40]
lst[2]=100 #为指定索引的元素赋上一个新值
print(lst)
lst[1:3]=[200,300,400]  #为指定的切片赋上一个新值
print(lst)
print("------列表元素的排序操作--------")
lst=[10,30,15,79,1]
print("original list",lst,id(lst))
lst.sort() # sort 进行升序排序
print("排序后的列表",lst,id(lst))
lst.sort(reverse=True) #进行降序排序
print(lst)
lst.sort(reverse=False)# 效果同sort 进行升序排序
print(lst)
lst=[10,30,15,79,1]
new_list=sorted(lst) #使用内置函数sorted进行排序，将产生一个新的列表对象
print(new_list,id(new_list))
desc_list=sorted(lst,reverse=True)
print(desc_list,id(desc_list))
print("--------列表生成式------")
lst=[i*i for i in range(1,10)]
print(lst)
#example 生成一个列表表达式，列表中元素的值为2,4,6,8,10
lst=[i*2 for i in range(1,6)]
print(lst)