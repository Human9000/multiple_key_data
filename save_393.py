from struct_v3 import table2

table2.load('table2.npz')
with open('393.csv', 'r', encoding='utf8') as f:
    lines = f.readlines()
    data = [line.replace('\n', '').split(',') for line in lines]

body = data[1:-4]
yun = data[-4:]
年龄 = [[0], [0.5], [1, 2, 3], [4, 5, 6], [7, 8, 9, 10], [11], [14], [18], [50], [65], [80]]
指标 = ['RNI', 'RNI', 'RNI', 'AI', 'AI', 'RNI', 'RNI', 'RNI', 'RNI', 'RNI', 'RNI', 'AI', 'RNI', 'RNI',
      'RNI', "AI", "AI", "AI", "RNI"]
元素 = ['维生素A/μg', '维生素A/μg', '维生素D/μg', '维生素E/mg', '维生素K/μg', '维生素B1/mg',
      '维生素B1/mg', '维生素B2/mg', '维生素B2/mg', '维生素B6/mg', '维生素B12/μg', '泛酸/mg',
      '叶酸/μg', '烟酸/mg', '烟酸/mg', '胆碱/mg', '胆碱/mg', '生物素/μg', '维生素C/mg', ]
性别 = [['男'], ['女'], ['男', '女'], ['男', '女'], ['男', '女'], ['男'], ['女'], ['男'], ['女'], ['男', '女'], ['男', '女'], ['男', '女'],
      ['男', '女'], ['男'], ['女'], ['男'], ['女'], ['男', '女'], ['男', '女'], ]

孕期 = ['不是', '早期', '中期', '晚期', '乳母']


for i in range(len(年龄)):
    for j in range(len(指标)):
        value = body[i][j + 1]
        if value == '':
            continue

        if value.find('/AI') != -1:
            value = value.replace('/AI', '')
            指标j = 'AI'
        else:
            指标j = 指标[j]

        v1 = float(value)

        for 年龄i in 年龄[i]:
            for 性别j in 性别[j]:
                table2.set(v1, 年龄i, 性别j, 指标j, 元素[j], 孕期[0], log=True)
                if 性别j == '男':
                    continue
                for k in range(1, len(孕期)):
                    value = yun[k - 1][j + 1]
                    v = v1
                    if value != '':
                        if value.find('+') != -1:
                            v = float(value) + v1
                        else:
                            v = float(value)
                    table2.set(v1, 年龄i, 性别j, 指标j, 元素[j], 孕期[k], log=True)

table2.save('table2.npz')
