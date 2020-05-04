# part 1
def typed(**kwargs):# kwargs=
    def deco(obj):
        # 1
        # print(kwargs)
        # 2
        # print(obj)
        # dict
        for key,val in kwargs.items():
            # print("--->",key,val)
            setattr(obj, key, val)
        return obj
    return deco

# 给类 添加属性（限定空间）
# 减少代码的重复写
@typed(x=1,
       # y=2,
       name= "space")
class mycl:
    propose = "parmas_deco"
    y = "nonspace"
    @classmethod
    def print_parmas(cls):
        print("cls.propose:", cls.propose)
        print("cls.x:", cls.x)
        print("cls.y:", cls.y)
        print("cls.name:", cls.name)

mycl.print_parmas()
print("cls: ",mycl.__dict__)

# part 2