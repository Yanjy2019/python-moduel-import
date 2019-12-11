import turtle
n=eval(input("请输入多边形的边数："))     #画一个正多边形的函数
for i in range(1,n+1):
    turtle.fd(100)
    turtle.right(360/n)
turtle.done()
