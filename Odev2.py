import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-500, 501, 100)
z = []

# YAKIN üyelik fonksiyonu
def yakin_uyelik_fonksiyonu(mesafe):
    if -500 < mesafe <= -200:
        return (500 - abs(mesafe)) / 300
    elif -200 < mesafe < 200:
        return 1
    elif 200 <= mesafe < 500:
        return (500 - mesafe) / 300
    else:
        return 0

for mesafe in x:
    z.append(yakin_uyelik_fonksiyonu(mesafe))       # x teki her bir değerin y sini yani üyelik derecesini z dizisine ekliyoruz.

plt.plot(x, z, label="YAKIN Üyelik Fonksiyonu")
plt.xlabel("Mesafe")
plt.ylabel("YAKIN Üyelik Derecesi")
plt.title("YAKIN Dilsel Teriminin Üyelik Fonksiyonu")
plt.xticks(x)          # Bu komutu x eksenindeki sayıların 100 er 100 er artarak ekranda yazması için yaptım.
plt.grid(True)
plt.show()
