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

turtle.done()