from struct_v3 import table1

table1.load("table1.npz")
with open('390.csv', 'r', encoding='utf8') as f:
    lines = f.readlines()
    data = [line.replace('\n', '').split(',') for line in lines]

body = data[1:-4]
yun = data[-4:]
年龄 = [0, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 18, 50, 65, 80]
能量 = ['MJ'] * 6 + ['kcal'] * 6
活动 = ['轻', '轻', '中', '中', '重', '重', ] * 2
性别 = ['男', '女', ] * 6
孕期 = ['不是', '早期', '中期', '晚期', '乳母']
print(能量)
print(活动)
print(性别)

for i in range(len(年龄)):
    for j in range(len(能量)):
        # print(i, j+1)
        value = body[i][j + 1]
        if value != '':
            v1 = float(value)
            table1.set(v1, 年龄[i], 'EAR', 活动[j], 性别[j], 能量[j], 孕期[0], log=True)
            for k in range(1, len(孕期)):
                value = yun[k-1][j+1]
                v = v1
                if value != '':
                    if value.find('+') != -1:
                        v = float(value) + v1
                table1.set(v, 年龄[i], 'EAR', 活动[j], 性别[j], 能量[j], 孕期[k], log=True)

table1.save('table1.npz')