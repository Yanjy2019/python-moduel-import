#模拟进度条的函数编写
scale=50
print("--------------程序开始")
import time
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
    time.sleep(0.2)
print("\n----------------程序结束")
