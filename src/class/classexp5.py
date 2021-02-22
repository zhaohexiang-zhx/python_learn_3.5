


# 静态方法，类方法，property方法

class Person:

    total_person = 0
    def __init__(self, name, sex, province):
        print("Init the class")
        self.name = name
        self.sex = sex
        self.province = province
        Person.total_person += 1

    # 静态方法，调用时，可以不实例化对象，也可以实例化调用
    # 用法：需要分享类参数，不想实例化对象时
    # 无self参数
    @staticmethod
    def set_new1_province(new1_province):
        return "new1 province is " + new1_province

    # property属性，调用时不加括号
    @property
    # 需要传参数self
    def get_sex(self):
        return self.sex

    # 类方法，默认参数为cls
    @classmethod
    def set_new2_province(cls,new2_province):
        return "new2 province is " + new2_province


if __name__ == "__main__":
    # 不实例化对象，直接调用
    print(Person.set_new1_province("Beijing"))
    print(Person.set_new2_province("Tiananmen"))
    print("*" * 40)
    # 实例化对象per
    per = Person("huahua", "Female", "Shandong")
    print(per.set_new1_province("Shanghai"))
    print(per.set_new2_province("Dongfangmingzhu"))
    # property方法，不用带括号也能访问
    print(per.get_sex)


