import heapq

# 取出最大或者最小的n个数字, heapq.nlargest, heapq.nsmallest
l=[1,2,3,2,2,3,4,5,6,7,8,9,657,567,6,567,1,2,1,1,1,1,1]

print(heapq.nlargest(5,l))
print(heapq.nsmallest(4,l))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print(heapq.nsmallest(3,portfolio,lambda x: x["price"]))
print(heapq.nlargest(3,portfolio,lambda x: x["price"]))

# heapq.heappush添加元素到堆中
list=[1,2,3,666,444,555,666,777]
heapq.heappush(list,999)
print(list)
# heapq.heapify转换为堆
list=[10,999,3,2,1]
print(list)
heapq.heapify(list)
print(list)
# heapq.heappop 删除元素第一个元素并返回最小值

list=[0,2,2,3,4,56,66,78,77,88,88,99]
print(list)
print(heapq.heappop(list))
print(list)
# heapq.heapreplace(heap.item)删除返回最小值，添加新的元素
aaa=[0,20,30,40]
print(heapq.heapreplace(aaa,55))
print(aaa)


