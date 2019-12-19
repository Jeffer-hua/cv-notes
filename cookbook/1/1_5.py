# 怎样实现一个按优先级排序的队列？ 并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素

# heapq.heappush 根据index自动进行排序
import heapq


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # heapq.heappush 在队列上插入第一个元素
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
        print(self._queue)

    def pop(self):
        # heapq.heappop 在队列上删除第一个元素
        # heappop() 函数总是返回”最小的”的元素
        return heapq.heappop(self._queue)[-1]


class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item{!r}'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
