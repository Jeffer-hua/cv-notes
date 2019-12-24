# 你想匹配或者搜索特定模式的文本

# 假设你想匹配数字格式的日期字符串比如 11/27/2012
import re

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
# re.match
if re.match(r'\d+/+\d+/+\d+', text2):
    print('yes')
else:
    print('no')

# 使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象
# re.compile
datepat = re.compile(r'\d+/+\d+/+\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

# match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位置
# 使用 findall() 方法去代替
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

# 通常会利用括号去捕获分组,将每个组的内容提取出来
datapet_1 = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datapet_1.match('11/27/2012')
print(m)
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.groups())

# findall() 方法会搜索文本并以列表形式返回所有的匹配
# 如果你想以迭代方式返回匹配，可以使用 finditer() 方法来代替
for m in datapet_1.finditer(text):
    print(m.groups())
