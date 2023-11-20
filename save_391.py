from struct_v3 import table2

table2.load('table2.npz')
with open('391.csv', 'r', encoding='utf8') as f:
    lines = f.readlines()
    data = [line.replace('\n', '').split(',') for line in lines]

body = data[1:-4]
yun = data[-4:]
年龄 = [0, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 18, 50, 65, 80]
性别 = ['男', '女', '男', '女', ['男', '女', ], ['男', '女', ], ['男', '女', ], ['男', '女', ]]
指标 = ['EAR', 'EAR', 'EAR', 'EAR', 'EAR', 'D-AMDR', "U-AMDR", "U-AMDR", ]
元素 = ['蛋白质', '蛋白质', '蛋白质', '蛋白质', '碳水', '碳水', '碳水', '添加糖']
孕期 = ['不是', '早期', '中期', '晚期', '乳母']

for i in range(len(年龄)):
    for j in range(len(指标)):
        # print(i, j + 1)
        value = body[i][j + 1]
        if value != '':
            if value.find('/AI') != -1:
                value = value.replace('/AI', '')
                指标j = 'AI'
            else:
                指标j = 指标[j]
            v1 = float(value)
            for 性别j in 性别[j]:
                table2.set(v1, 年龄[i], 性别j, 指标j, 元素[j], 孕期[0], log=True)
                for k in range(1, len(孕期)):
                    value = yun[k - 1][j + 1]
                    v = v1
                    if value != '':
                        if value.find('+') != -1:
                            v = float(value) + v1
                        else:
                            v = float(value)
                    table2.set(v1, 年龄[i], 性别j, 指标j, 元素[j], 孕期[k], log=True)

table2.save('table2.npz')
