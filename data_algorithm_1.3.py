"""在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
"""


# ???


from _collections import deque



# 使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉。
q=deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.pop()

print(q)
# 更一般的， deque 类可以被用在任何你只需要一个简单队列数据结构的场合。 如果你不设置最大队列大小，那么就会得到一个无限大小队列，你可以在队列的两端执行添加和弹出元素的操作。
q=deque()
q.append(1)
q.append(2)
q.append(3)
q.appendleft(4)
q.append(5)
q.pop()

print(q)
