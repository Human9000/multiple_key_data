from struct_v3 import table2

# table2.load('table2.npz')
with open('396.csv', 'r', encoding='utf8') as f:
    lines = f.readlines()
    data = [line.replace('\n', '').split(',') for line in lines]

body = data[1:]

年龄 = [0, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 18, 50, 65, 80]
膳食 = ['膳食纤维/g', '植物淄醇/g', '植物淄醇脂/g', '番茄红素/mg', '叶黄素/mg',
      '原花青素/mg', '大豆异黄酮/mg', '花色苷/mg', '氨基葡萄糖/mg', '硫酸或盐酸基葡萄糖/mg', '姜黄素/mg']
指标 = ['SPL', 'UL']

for i in range(len(膳食)):
    for j in range(len(指标)):
        value = body[i][j+1]
        if value == '':
            continue

        if value.find('/AI') != -1:
            value = value.replace('/AI', '')
            指标j = 'AI'
        else:
            指标j = 指标[j]

        v1 = float(value)
        for 年龄 in [0, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 18, 50, 65, 80]:
            for 性别 in ['男','女']:
                for 孕期 in ["不是", "早期", "中期", "晚期", '乳母']:
                    table2.set(v1, 年龄, 性别, 指标j, 膳食[j], 孕期, log=True)


table2.save('table2.npz')
