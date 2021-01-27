#字符串的常见操作
print("---字符串的查询操作----")
s="hello,hello"
print(s.index("lo"))
print(s.rindex("lo"))
print(s.find("lo"))
print(s.rfind("lo"))
#print(s.index("k")) ValueError: substring not found
print(s.find("k")) #-1
print("---字符串的大小写转换----")
s="hello,python"
a=s.upper() #转成大写之后，会产生一个新的字符串对象
print(a,id(a))
print(s,id(s))
print(a==s)
b=s.lower() #转成之后，仍然会产生一个新的字符串对象
print(b,id(b))
print(s,id(s))
print(b==s)
print(b is s)

s2="Hello,Python"
print(s2.swapcase())
a=s2.swapcase()
print(a)
print(s2.title())
print(s2.capitalize())
print("---字符串内容对齐操作----")
s="hello,python"
"""居中对齐"""
print(s.center(20,"*"))
"""左对齐"""
print(s.ljust(20,"*"))
print(s.ljust(20))
print(s.ljust(10))
"""右对齐"""
print(s.rjust(20,"*"))
print(s.rjust(20))
print(s.rjust(10))
"""右对齐使用0进行填充"""
print(s.zfill(20))
print(s.zfill(10))
print("-8910".zfill(8))
print("---字符串内容劈分操作----")
s="hello world ptyhon"
lst=s.split()
print(lst)
s1="hello|world|python"
print(s1.split())
print(s1.split(sep=("|")))
print(s1.split(sep="|",maxsplit=1))
print("---字符串从右侧开始劈分，rsplit()----")
print(s.rsplit())
print(s1.rsplit(sep="|"))
print(s1.rsplit(sep="|",maxsplit=1))