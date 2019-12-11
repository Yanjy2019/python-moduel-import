import time
print(time.localtime())   #输出当前的时间，精确度非常高，获取的是本地时间
print(time.time())    #获取当前的时间戳，代表着当今的时间和1970年1月1日0是0分0秒的时间差（以秒为单位），1970年是时间开始的基元，即相对0时间

import random
print(random.random())
print(random.randint(1,9))   #产生一个1-9的随机整数

import turtle #画笔函数的图形绘制，可以绘制任意形状的图形和画布
import time
#时间处理函数介绍4个
first_time=time.time()
a=0
for i in range(10000000):
    a+=1
print(a)
last_time=time.time()
print(last_time-first_time)    #使用时间戳可以获取不同程序运行时间来进行检测与测试程序的高效性，经常使用
print(time.gmtime())           #获取的是世界统一的时间，即当前对于全球各个地方的标准时间
print(time.localtime())        #某年莫月末日某时某秒某周几某天数(从每年的元旦算起来的天数)
print(time.ctime())            #以标准的格式输出时间，看起来比较方便的方式

#时间格式化处理函数3个
t=time.localtime()
print(t)
print(time.mktime(t))       #将str_time对象转换为时间戳，即与原始时间1970年0时做时间差得出的以秒为单位的时间
print(time.strftime("%Y-%m-%d-%H:%M:%S",t))   #格式化时间输出的形式，便于不同的情况来进行方便查看时间
time="2019-12-11-08:48:10"
#print(time.strptime(time,"%Y-%m-%d-%H:%M-%S"))  #strptime主要用来转换字符串你为标准的strc_time形式的时间输出形式，互为相反

#程序计时函数2个
import time
star_time=time.time()
time.sleep(1)             #推迟调用线程的运行，可以通过参数secs秒数来进行指定，表示进程挂起（睡眠）的时间
last_time=time.time()
print(last_time-star_time)
print(time.perf_counter())#返回一个函性能计数器的值（在的分秒以内）即具有很高精度分辨率的时钟，已测量短时间，它包括了在睡眠期间的时间。
a1=time.time()
b1=time.perf_counter()
a2=time.time()
b2=time.perf_counter()
print(a2-a1)   #进度相对较低
print(b2-b1)   #精度分辨率非常高，即使一行代码也可以检测出程序运行的时间
#模拟进度条的函数编写
scale=50
print("--------------程序开始")
start_time=time.perf_counter()
for i in range(scale+1):
    a="*"*i
    b="."*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start_time
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")   #\r表示将光标返回到不本行的开头，直接进行覆盖即可显示结果
    #{:^3.2f}的具体使用规则说明：
   #:前面有两个参数选择，0表示右对齐，1表示左对齐（默认情况下就是左对齐的方式）
    #^3表示的是输出的字符串的宽度约束为3个单位长度
    #.2f表示输出的形式保留两位小数的浮点数数据类型
    time.sleep(0.05)
print("----------------程序结束")

#random随机数产生库
import random
print(random.random())  #产生一个0-1的素随机小数
random.seed()       #初始化随机数种子，输入seed的参数，可以使得随机数确定下来，这样便可以固定一个随机参数值，默认为当前的系统时间
print(random.random())
print(random.randint(1,100))  #随机生成一个1-100的随机整数
print(random.randrange(1,100,10))
print(random.uniform(1,5))   #生成一个1到5的随机小数
a=["yjy2019",123,"剪刀"]
print(random.choice(a))

#Python石头剪刀布的小程序设计
ls=["剪刀","石头","布"]                    #剪刀石头布的小程序设计Python语言，只需要使用random模块里面的randdom.choice()来进行序列里面的随机选择
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

import turtle
turtle.setup(500,500,200,200)
turtle.right(45)

#setheading函数主要是绝对的角度方向
turtle.setheading(120)  #相对于磨人的方向逆时针旋转一定的角度，它是绝对的角度
turtle.fd(200)

#goto函数是指移动到绝对的位置坐标（x,y）处
turtle.goto(100,100)
turtle.goto(-100,-100)

#tutle.circle(R,angle)函数主要是进行圆的绘制和运动,R代表半径，angle是角度
turtle.circle(10,180)  #基于当前的方向进行画圆

#turtle.speed 运动画笔速度的设置函数
turtle.speed(10)    #设置画笔运动的速度，可以使得每一段画笔运动时的速度根据自己的需求进行设置和变化
turtle.fd(100)

import turtle

#penup画笔提起函数
turtle.penup()
turtle.fd(100)

#pendown画笔放下来的函数，与penup对应使用
turtle.down()
turtle.circle(100,360)

#pensize()函数主要用来设置画笔的粗细
turtle.pensize(10)
turtle.fd(100)
turtle.pensize(1)
turtle.fd(100)

#color函数用来设置画笔的颜色
turtle.color("red")
turtle.fd(100)

#begin_fill函数用；来填充一定的颜色,它必须和end_fill混合使用才会有效
turtle.begin_fill()
turtle.color("red")
turtle.circle(100)
print(turtle.filling())   #在填充的过程中是填充的状态，所以输出应该为true
turtle.end_fill()
print(turtle.filling())   #画结束之后输出为false
#filling函数的功能是返回填充的状态，true或者false

#clear()函数主要用来清空当前画布的图,但是并不改变画笔当前的位置，只保留下画笔当前的位置
#turtle.clear()

#reset函数主要用来直接恢复画布的状态为最原始的默认状态，即进行状态的重置
#turtle.reset()

#screensize()  重新设置画布的长度和宽度
turtle.screensize(2000,2000)

#hideturtle画图之后总是存在小箭头，可以隐藏小箭头,showturtle可以展示出小箭头
turtle.fd(100)
turtle.hideturtle()
import time
time.sleep(5)
turtle.showturtle()

#isvisible函数主要用来检测画布上是否有turtle,false和true
print(turtle.isvisible())

#s石头剪刀布的计算机小程序
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

#画出一个n多多边形
import turtle
n=eval(input("请输入多边形的边数："))     #画一个正多边形的函数
for i in range(1,n+1):
    turtle.fd(100)
    turtle.right(360/n)
turtle.done()

turtle.done()