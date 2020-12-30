# 无构造函数：在函数初始化时，未得到所有变量

class Person:

    #先set，后get
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


if __name__ == "__main__":
    per1 = Person()
    per1.set_name("xiaozhao")
    print(per1.get_name())

