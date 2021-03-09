"""如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？
Python 的星号表达式可以用来解决这个问题
"""

# 星号用于中间部分
def drop_first_last(grade):
    first, *middle, last = grade
    return sum(middle)/len(middle),middle
# 星号用于结尾部分
record=("dave","dave@exple.com","123-333-1111","222-111-2121")



# 星号用于前面部分，可变长元组的序列
a=drop_first_last([18, 22, 33, 44, 55, 66, 77, 88, 99, 100])
print(a)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

*tag,tag2=records
print(tag,tag2)

# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
username,*field,homedir,sh=line.split(":")
print(username,field,homedir,sh)



# 解压一些元素后丢弃它们，你不能简单就使用 *_
records = ('ACME', 50, 123.45, (12, 18, 2012))
name,*_,(*_,year)=records
print(name,year)
