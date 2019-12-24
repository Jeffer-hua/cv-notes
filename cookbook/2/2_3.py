# 你想使用 Unix Shell 中常用的通配符(比如 *.py , Dat[0-9]*.csv 等)去匹配文本字符串

# fnmatch 模块提供了两个函数—— fnmatch() 和 fnmatchcase() ，可以用来实现这样的匹配

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

# fnmatch() 函数使用底层操作系统的大小写敏感规则(不同的系统是不一样的)来匹配模式
# On OS X(Mac)
print(fnmatch('foo.txt', '*.TXT'))
# False
# On Windows
print(fnmatch('foo.txt', '*.TXT'))
# True

# 对大小写要求严格的建议使用fnmatchcase()
print(fnmatchcase('foo.txt', '*.TXT'))
