import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def system(XY, t):
   dx = a1*XY[0] - b1*XY[0]*XY[1]/(1 + A*XY[0]) - c1*XY[0]**2
   dy = -a2*XY[1] + b2*XY[0]*XY[1]/(1 + A*XY[0])
   return dx, dy

def draw(a1,a2,b1,b2,A,c1,XY,t,name):
    s = odeint(system, XY, t)
    plt.plot(t, s[:, 0], 'o-', label='Жертва')
    plt.plot(t, s[:, 1], 'o-', label='Хищник')
    plt.xlabel('t')
    plt.ylabel('x(t),y(t)')
    plt.legend()
    plt.grid()
    plt.savefig(name+'.png', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    a1 = 6                 #коэф размножения жертвы
    a2 = 3                  #коэф вымирания хищника
    b1 = 3                  #коэф уменьшения численности жертвы за счёт поедания хищником
    b2 = 1.4                  #коэф увеличения численности хищника за счёт поедания жертвы
    A = 0.5               #коэф насыщения хищника
    c1 = 0.1             #коэф внутривидовой конкуренции жертвы
    XY = [100, 50]
    t = np.linspace(0, 3)

    draw(a1, a2, b1, b2, A, c1, XY, t, "Изначально")
    a1/=2
    draw(a1, a2, b1, b2, A, c1, XY, t, "Уменьшили a1")
    a1*=4
    draw(a1, a2, b1, b2, A, c1, XY, t, "Увеличим a1")
    a1/=2
    a2/=2
    draw(a1, a2, b1, b2, A, c1, XY, t, "Уменьшим a2")
    a2*=4
    draw(a1, a2, b1, b2, A, c1, XY, t, "Увеличим a2")
    a2/=2
    b1/=2
    draw(a1, a2, b1, b2, A, c1, XY, t, "Уменьшим b1")
    b1 *= 4
    draw(a1, a2, b1, b2, A, c1, XY, t, "Увеличим b1")
    b1/=2
    b2/=2
    draw(a1, a2, b1, b2, A, c1, XY, t, "Уменьшим b2")
    b2*=4
    draw(a1, a2, b1, b2, A, c1, XY, t, "Увеличим b2")
    b2/=2
    A/=2
    draw(a1, a2, b1, b2, A, c1, XY, t, "Уменьшим A")
    A*=4
    draw(a1, a2, b1, b2, A, c1, XY, t, "Увеличим A")
    A/=2
    c1/=2
    draw(a1, a2, b1, b2, A, c1, XY, t, "Уменьшим C1")
    c1 *= 4
    draw(a1, a2, b1, b2, A, c1, XY, t, "Увеличим C1")
