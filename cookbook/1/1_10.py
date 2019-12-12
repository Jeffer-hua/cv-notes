# 怎样在一个序列上面保持元素顺序的同时消除重复的值
# 单纯消除重复的值使用集合属性就好,保持顺序则使用yield去return
def dedupe_hashable(items):
    seen = set()
    for item in items:
        if item not in seen:
            # 使用yield代替return保持元素顺序
            yield item
            seen.add(item)
    print(seen)


# 针对不可hashable
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
    print(seen)


b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a, key=None)))
print(list(dedupe(b, key=lambda d: (d['x'], d['y']))))
