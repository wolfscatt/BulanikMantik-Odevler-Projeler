import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.1)
z = []

def f(x):
    return 1/(1+(10*(pow(x-5,2))))

for i in x:
    z.append(f(i))

plt.plot(x,z)

answer = 'y'
while answer == 'y' or answer == 'Y':
    userx = float(input("Enter a value for x (0-10): "))
    mx = f(userx)
    print(f"Value of f({userx}) is {mx}")
    plt.plot(userx,mx,'ro')
    plt.vlines(userx, ymin=0, ymax=mx, color='gray', linestyle='dashed')
    plt.hlines(mx, xmin=0, xmax=userx, color='gray', linestyle='dashed')
    answer = input("Do you want to continue? ((y/Y) - Yes , (n/N) - No): ")
    if(answer == 'n' or answer == 'N'):
        break

plt.show()
