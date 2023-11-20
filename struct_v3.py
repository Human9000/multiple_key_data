import numpy as np


# 定义一个函数，用于获取变量名称
def get_variable_name(var):
    # 获取全局变量字典
    globals_dict = globals()
    # 遍历字典，查找变量名称
    for name, value in globals_dict.items():
        if value is var:
            return name


def index_age(value, data):
    assert 0 <= value < 150, "age must be in [0, 150]"
    index = 0
    while data[index] <= value and index < len(data) - 1:
        index += 1
    return index - 1


def index(value, data):
    assert value in data, f"value must be in data, value={value}, data={data}"
    return data.index(value)


class Col:
    def __init__(self, data, index_fuc=index):
        self.data = data
        self.index_fuc = index_fuc

    def index(self, value):
        return self.index_fuc(value, self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        return self.data[i]

    def __str__(self):
        return str(self.data)


class Data:
    def __init__(self, *cols):
        self.cols = cols
        self.shape = [len(i.data) for i in cols]  # 多维数组的形状
        self.pages = [1]  # 多维数组的页面大小
        for s in self.shape[1:][::-1]:
            self.pages.insert(0, self.pages[0] * s)
        self.data = np.zeros(self.pages[0] * self.shape[0]).astype(np.float32)  # 存储的时候拉直，存成1维数组

    def __str__(self):
        var_name = get_variable_name(self)
        return f"{var_name}.shape = {self.shape} \n\t" + "\n\t".join([str(i) for i in self.cols])

    def get(self, *keys, log=False):
        # 将 keys 映射成 indexes
        indexes = [col.index(key) for col, key in zip(self.cols, keys)]

        value = self.__get__(*indexes)
        if log:
            var_name = get_variable_name(self)
            print(f"{value:5.2f} <= {var_name}." + "Get(" + ", ".join([str(i) for i in keys]) + ')')
        return value

    def set(self, value, *keys, log=False):
        # 将 keys 映射成 indexes
        indexes = [col.index(key) for col, key in zip(self.cols, keys)]

        self.__set__(value, *indexes)

        if log:
            var_name = get_variable_name(self)
            print(f"{value:5.2f} => {var_name}." + "Set(" + ", ".join([str(i) for i in keys]) + ')')

    def __get__(self, *indexes):  # 按照多维数组进行读取
        assert len(indexes) == len(self.shape), "indexs的长度与keys的长度不一致"
        assert all(0 <= i < s for i, s in zip(indexes, self.shape)), "indexs的值不在范围内"
        # ==== 计算索引坐标
        index = 0
        for i, v in enumerate(indexes):
            index += self.pages[i] * v
        # ==== 取得数据
        return self.data[index]

    def __set__(self, value, *indexes):  # 按照多维数组进行读取
        assert len(indexes) == len(self.shape), "indexs的长度与keys的长度不一致"
        assert all(0 <= i < s for i, s in zip(indexes, self.shape)), "indexs的值不在范围内"
        # ==== 计算索引坐标
        index = 0
        for i, v in enumerate(indexes):
            index += self.pages[i] * v
        self.data[index] = value

    def save(self, path):
        np.savez(path, data=self.data)

    def load(self, path):
        self.data = np.load(path)['data']

# 可以选择的列有以下几个
孕期 = ["不是", "早期", "中期", "晚期", '乳母']
年龄 = [0, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 18, 50, 65, 80]
性别 = ["男", "女"]
指标 = ["EAR", "RNI", "AI", "UL", "D-AMDR", "U-AMDR", "RI-NCD", "SPL"]
活动水平 = ["轻", "中", "重"]
能量 = ['MJ', "kcal"]
元素 = ['蛋白质', '碳水', '添加糖', '总脂肪', '饱和脂肪酸', 'n-6多不饱和脂肪酸', 'n-3多不饱和脂肪酸', 'EPA+DHA', 'DHA', '维生素A/μg', '维生素D/μg',
      '维生素E/mg', '维生素K/μg', '维生素B1/mg', '维生素B2/mg', '维生素B6/mg', '维生素B12/μg', '泛酸/mg', '叶酸/μg', '烟酸/mg',
      '胆碱/mg', '生物素/μg', '维生素C/mg', '钙/mg', '磷/mg', '钾/mg', '钠/mg', '镁/mg', '铁/mg', '碘/μg', '锌/mg', '硒/ug',
      '铜/mg', '氟/mg', '铬/mg', '锰/mg', '钼/μg', '烟酰胺/mg']
膳食 = ['膳食纤维/g', '植物淄醇/g', '植物淄醇脂/g', '番茄红素/mg', '叶黄素/mg',
      '原花青素/mg', '大豆异黄酮/mg', '花色苷/mg', '氨基葡萄糖/mg', '硫酸或盐酸基葡萄糖/mg', '姜黄素/mg']
元素 += 膳食
# 版本v3，孕期的统统采用
# 390
table1 = Data(Col(年龄, index_age), Col(指标), Col(活动水平), Col(性别), Col(能量), Col(孕期))

# 391 - 395
table2 = Data(Col(年龄, index_age), Col(性别), Col(指标), Col(元素), Col(孕期))

# 396


if __name__ == '__main__':
    table1.save('./table1.npz')
    table2.save('./table2.npz')

    table1.load('./table1.npz')
    table2.load('./table2.npz')

    print(table1)
    print(table2)
