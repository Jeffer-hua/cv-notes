# 你需要将一个字符串分割为多个字段，但是分隔符(还有周围的空格)并不是固定的
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
# string 对象的 split() 方法只适应于非常简单的字符串分割情形
# re.split(),允许你为分隔符指定多个正则模式
res1 = re.split(r'[;,\s]\s*', line)
# 使用括号捕获分组会使被匹配的文本都返回
res2 = re.split(r'(;|,|\s)\s*', line)
print(res1)
print(res2)
