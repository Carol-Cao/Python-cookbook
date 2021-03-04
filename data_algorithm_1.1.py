"""现在有一个包含N个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N个变量？
任何的序列（或者是可迭代对象）可以通过一个简单的赋值操作来分解为单独的变量。 唯一的要求就是变量的总数和结构必须与序列相吻合。"""

p=(4,5)
x,y=p
print(x,y)
print("")

data=["acme",59,90.1,(2012,12,21)]
name,shares,prices,date=data
print(name,shares,prices,date)
print("")

name,shares,prices,(year,mon,day)=data
print(name,shares,prices,year,mon,day)

#元素不匹配会报错，p=(4,5)   x,y,z=p

# 字符串，文件对象也可以进行迭代
s="hello"
a,b,c,d,e=s
print(a,b,c,d,e)

# 使用占位符丢弃变量
data=["acme",50,90.1,(2012,12,21)]
_,shares,prices,_=data
print(shares,prices)

