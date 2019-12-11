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

turtle.done()