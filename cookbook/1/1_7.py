# 你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

# 控制JSON编码后字段的顺序
import json

print(json.dumps(d))

# OredereDict内部维护着一个根据健插入顺序的双向链表
# 一个OrderedDict的大小是普通字典的两倍
