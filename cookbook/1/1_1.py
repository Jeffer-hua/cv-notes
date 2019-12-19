# 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？

# 1.解压赋值，解压前后元素个数需一致
p = (4, 5)
x, y = p
# 2.元素不一致时，可以使用占位符替代
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data

