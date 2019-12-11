import turtle
#设置画布的大小和位置
turtle.setup(500,500,200,200)    #setup()函数4个独立的参数来进行设置画布的大小和相对位置：长宽左边和顶部距离（距离屏幕的距离）

#forward函数：沿着当前的方向前进一定的距离，直线运动
turtle.forward(200)    #默认的方向为想右边的方向，其中200是前进的像素大小，开始点默认为画布的中心
turtle.fd(200)         #forward函数的缩写形式
#backward函数是后退函数
turtle.backward(200)  #向后走一定的距离，其中方向依旧为默认的向右方向
    #不断地展示出画布在屏幕上面
#right函数是指向右旋转一定的角度，默认为右边的方向，是指相对于当前的方向，相对方向
turtle.right(90)
turtle.backward(200)
turtle.done()
