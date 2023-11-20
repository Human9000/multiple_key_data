# multiple_key_data
快速的多key查询存储工具，参考摄入量


使用样例
```python
# 390 创建表格
table1 = Data(Col(年龄, index_age), Col(指标), Col(活动水平), Col(性别), Col(能量), Col(孕期))

# 391 - 396 创建表格
table2 = Data(Col(年龄, index_age), Col(性别), Col(指标), Col(元素), Col(孕期))

# demo 查询表格
table1.Get(...)

# demo 修改表格
table1.Set(...)
```
