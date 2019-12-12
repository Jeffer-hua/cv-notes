# 怎样实现一个键对应多个值的字典（也叫 multidict）

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d2 = defaultdict(set)
d2['a'].add(1)
d2['a'].add(2)
d2['b'].add(4)
print(d)
print(d2)

# defaultdict会自动为将要访问的键(就算目前字典中并不存在这样的键)创建映射实体
# 如果不需要这样子的特性，可以在一个普通的字典上使用setdefault()方法来代替
d3 = {}
d3.setdefault(('a'), []).append(1)
d3.setdefault(('a'), []).append(2)
d3.setdefault(('b'), []).append(4)
print(d3)

# 使用 defaultdict创建一个多值映射字典
pairs = [(1, ['1']), (2, ['2', '4'])]
d4 = defaultdict(list)
for key, value in pairs:
    d4[key].append(value)
print(d4)
