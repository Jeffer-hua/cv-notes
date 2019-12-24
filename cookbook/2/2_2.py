# 你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL Scheme等等。

# str.startswith() / str.endswith()

filename = 'spam.txt'
print(filename.endswith('.txt'))

# 检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去
# any(),内置函数(里面所有为False则为False,否则为True)

test = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
print([name for name in test if name.endswith(('.c', '.h'))])
print(any(name.endswith('.py') for name in test))
