import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
plt.figure(figsize=(6,6))
#1英寸=2.54cm
a=np.loadtxt("D:\\python\\python练习\\2018 513作业\\card price.csv",delimiter=',',skiprows=1,usecols=(1,2,3,4))

ope=a[1:5,0]
open=list(reversed(ope))

print(open)
high=a[1:5,1]
x=np.linspace(1,5,1000)       #根据需要生成X轴坐标数组的点数
X=np.array([1,2,3,4])           #将一个列表转化为数组
Y=open
def f(p):                  # 定义一个函数
    k,b=p               #对谁做拟合
    return(Y-(k*X+b))                  # X Y 属于外部变量
r=leastsq(f,[1,0])                  # f 是拟合函数  [1,0，0] 是初始参数值
k,b =r[0]                   #r0 是拟合结果
print("k=",k,"b=",b)                 #输出拟合完的参数a,b,c
plt.scatter(X,Y,s=20,alpha=1.0,marker='o',label=u'数据点')      #绘制散点图
y=k*x+b                #散点图函数
#设置坐标轴标签字体大小
ax=plt.gca()
ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)

plt.plot(x, y, color='r',linewidth=1, linestyle=":",markersize=10, label=u'拟合曲线')         #开始画图
plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')
#坐标轴意义
plt.xlabel(u'X')
plt.ylabel(u'Y')
#坐标轴长度
plt.xlim(-4, x.max() * 1.1)
plt.ylim(-3, y.max() * 1.1)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#刻度字体大小
plt.legend(loc='upper left')
plt.show()

w=float(input("请输入月份:"))

z=k*w+b
print(float(z))