import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(1,10,0.1)
# y = []

# for tutx in x:
#     y.append(1/(1 + pow(tutx - 30/5, 4 )))
# plt.plot(x,y)
# plt.show()

'''
X = np.arange(-501,501,100)
Y = []

def yakin_uyelik_fun(mesafe):
    if mesafe <= -500:
        return 0
    elif -500 < mesafe <= -200:
        return (500 - abs(mesafe)) / 300
    elif -200 < mesafe < 200:
        return 1
    elif 200 <= mesafe < 500:
        return (500 - mesafe) / 300
    elif 500 <= mesafe:
        return 0
    

for mesafe in X:
    Y.append(yakin_uyelik_fun(mesafe))

plt.plot(X,Y, label="YAKIN Üyelik Fonksiyonu")
plt.xlabel("Mesafe")
plt.ylabel("YAKIN Üyelik Derecesi")
plt.grid(True)

userx = float(input("Enter a value for x (-500-500): "))
mx = yakin_uyelik_fun(userx)
plt.plot(userx,mx, 'ro')
plt.hlines(mx, xmin = -500, xmax = userx, color = 'red', linestyle = 'dashed')
plt.vlines(userx, ymin = 0, ymax = mx, color = 'red', linestyle = 'dashed')
plt.show()
'''


x = np.arange(0,100,1)
y = []
a , b, c, d = 20, 40, 60, 80

def ucgen_uyelik_fun(u, a, b, c):
    if u < a:
        return 0
    elif a <= u <= b:
        return (u - a) / (b - a)
    elif b <= u <= c:
        return (c - u) / (c - b)
    else:
        return 0
    
def yamuk_uyelik_fun(u,a,b,c,d):
    if u < a:
        return 0
    elif a <= u < b:
        return (u - a) / (b - a)
    elif b <= u <= c:
        return 1
    elif c < u <= d:
        return (d - u) / (d - c)
    else:
        return 0
    

def s_uyelik_fun(u,a,b,c):
    if u < a:
        return 0
    elif a <= u <= b:
        return 2*(pow((u-a)/(c-a),2))
    elif b <= u <= c:
        return 1 - 2*(pow((u-c)/(c-a),2))
    else:
        return 1


def pi_uyelik_fun(u, b, c):
    if u <= c:
        return s_uyelik_fun(u, c-b, c-b/2, c)
    elif u >= c:
        return 1 - s_uyelik_fun(u, c, c+b/2, c+b)
    

y = [ucgen_uyelik_fun(tutx, a, b, c) for tutx in x]
plt.plot(x,y, label="Üçgen Üyelik Fonksiyonu")

y = [yamuk_uyelik_fun(tutx, a,b,c,d) for tutx in x]
plt.plot(x,y, label="Yamuk Üyelik Fonksiyonu")

y = [s_uyelik_fun(tutx, 20, 50, 90) for tutx in x]
plt.plot(x,y, label="S_uyelik Fonksiyonu")

y = [pi_uyelik_fun(tutx, 40, 50) for tutx in x]
plt.plot(x,y, label="PI_uyelik Fonksiyonu")
plt.xticks(np.arange(0,100,10))
plt.grid(True)
plt.show()