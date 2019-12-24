# 你想在字符串中搜索和匹配指定的文本模式

# 1.简单的替换 str.replace()
# 2.复杂的替换 re.sub

import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# 反斜杠加数字（\N），则对应着匹配的组（matched group）
# 比如\3，表示匹配前面pattern中的第3个group
convert_text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(convert_text)

# 如果除了替换后的结果外，你还想知道有多少替换发生了，可以使用 re.subn() 来代替
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext, n)