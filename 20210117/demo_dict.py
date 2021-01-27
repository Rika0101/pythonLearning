print("----字典的创建方式----")
#1，使用{}创建字典
scores={"miss.lee":100,"mr.duan":60}
print(scores,type(scores))
#2,创建dict()
student=dict(name="miss.lee",age=22)
print(student)
#空字典
d={}
print(d)
print("---获取字典中的元素---")
#第一种方法，使用[]
scores={"miss.lee":100,"mr.duan":60}
print(scores["miss.lee"])
# print(scores["mr,wang"]) KeyError: 'mr,wang'
#第一种方法，使用get
print(scores.get("miss.lee"))
print(scores.get("mr.wang")) #None
print(scores.get("mt,wang"),70) #70是在查找"mt,wang"所对应的value不存在时，提供的一个默认值
print("----key的判断----")
scores={"miss.lee":100,"mr.duan":60}
print("miss.lee" in scores)
print("miss.lee" not in scores)
del scores["mr.duan"] #删除指定的key-value对
print(scores)
#scores.clear() 清空列表中的元素
scores["mt.wang"]=70 #新增元素
print(scores)
scores["mr.wang"]=69
print(scores) #修改元素
print("----获取字典视图----")
#获取所有的keys
scores={"miss.lee":100,"mr.duan":60,"mr.wang":70}
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys)) #将所有keys组成的视图转成列表
#获取所有的values
values=scores.values()
print(values)
print(type(values))
print(list(values))
#获取所有的key-value对
items=scores.items()
print(items)
print(type(items))
print(list(items)) #转换之后的列表元素是由元组组成
print("----字典元素的遍历----")
scores={"miss.lee":100,"mr.duan":60,"mr.wang":70}
for item in scores:
    print(item,scores[item],scores.get(item))
print("----字典的特点----")
#1，字典中所有元素都是一个key-value对，key不允许重复，value可以重复
d={"name":"rabbit","name":"bear"}
print(d) #key不允许重复
d={"name":"rabblt","nickname":"rabblt"}
print(d) #value可以重复
#2,字典中的元素是无序的 列表中可以指定在具体某个位置插入某一个元素，但是字典不可以；因为字典中的value的位置是根据key计算出来的，不是人为指定的
lst=[10,20,40,60]
lst.insert(1,100)
print(lst)
#3字典中的元素必须是不可变对象
#d={lst:100}  TypeError: unhashable type: 'list'
#4字典也可以根据需要进行动态地伸缩
#字典会浪费较大地内存（但是查询速度快），是一种使用空间换时间的数据结构
print("----字典生成式----")
items=["chacott","yumiko","others"]
prices=[7000,10000,5000,70,500] #y以元素少的为基准进行生成
d={ item.upper():price for item,price in zip(items,prices)}  #在item后面添加.upper()转换成大写
print(d)