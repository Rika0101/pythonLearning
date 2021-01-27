print("------可变序列 list,dictionary,可对序列执行增删改操作，对象地址不发生改变--------")
lst=[1,2,56,8]
print(id(lst))
lst.append(4)
print(id(lst))
d={"chacott":5,"yumiko":8,"othets":9}
print(id(d))
d["sansha"]=10
print(id(d))
print("------不可变序列 string,item,不可对序列执行增删改操作，对象地址发生改变--------")
s="hello"
print(id(s))
s=s+"world"
print(id(s))
