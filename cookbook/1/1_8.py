# 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 取出字典中最大/小的键及值
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))

# zip()创建一个只能访问一次的迭代器,第二次使用会error
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) # OK
# print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

# 排序字典
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
# 对直接字典进行min/max操作,仅仅作用于键
print(min(prices))
