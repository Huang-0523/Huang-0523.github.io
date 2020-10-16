import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['axes.unicode_minus']=False
C=1;a=-0.5;b=0.5;c=0
t=np.arange(-5,5,0.01)
x1=C*np.exp(a*t)
x2=C*np.exp(b*t)
x3=C*np.exp(c*t)
plt.subplot(2,2,1)
plt.plot(t,x1,t,x2,t,x3)
plt.axis([-5,5,0,10])
plt.title("指数信号:x(t)=e^0.5t")
plt.xlabel('t')
plt.ylabel('x1(t)')

plt.subplot(2,2,2)
A=2;w=0.5*np.pi;fi=np.pi/6
t1=np.arange(-4,4,0.001)
x4=A*np.cos(w*t1+fi)
plt.plot(t1,x4)
plt.axis([-4,4,-3,3])
plt.title('正弦信号:x(t)=2cos(0.5πt+π/6)')
plt.xlabel('t1')
plt.ylabel('x2(t)')

plt.subplot(2,2,3)
t2=np.arange(-4,4,0.001)
w1=2*np.pi
x5=C*np.exp(a*t2)*np.cos(w1*t1+fi)
plt.plot(t2,x5)
plt.axis([-4,4,-5,5])
plt.title('幅度衰减的正弦信号:x(t)=(e^-0.5t)*cos(2πt+π/6)')
plt.xlabel('t2')
plt.ylabel('x3(t)')

plt.subplot(2,2,4)
t2=np.arange(-4,4,0.001)
w1=2*np.pi
x6=C*np.exp(b*t2)*np.cos(w1*t1+fi)
plt.plot(t2,x6)
plt.axis([-4,4,-5,5])
plt.title('幅度增长的正弦信号:x(t)=(e^0.5t)*cos(2πt+π/6)')
plt.xlabel('t2')
plt.ylabel('x4(t)')

plt.show()