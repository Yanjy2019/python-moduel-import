import random
ls=["剪刀","石头","布"]
a=random.choice(ls)
b=input("请输入你的手势:")
print("计算机选择了:",a)
if a=="剪刀" and b=="石头":
    print("恭喜你赢了!")
if a=="剪刀" and b=="布":
    print("很抱歉你输了")
if a=="剪刀" and b=="剪刀":
    print("平局")
if a=="石头" and b=="剪刀":
    print("很抱歉你输了")
if a=="石头" and b=="布":
    print("恭喜你赢了!")
if a=="石头" and b=="石头":
    print("平局")
if a=="布" and b=="剪刀":
    print("恭喜你赢了!")
if a=="布" and b=="石头":
    print("很抱歉你输了")
if a=="布" and b=="布":
    print("平局")

random.shuffle(ls)   #random.shufffle()函数的功能是对原来的序列进行打乱和随机排序
print(ls)
print(random.sample(ls,2))     #从序列里随机选择n个元素，b并且以列表的形式返回随机选择的元素即可

