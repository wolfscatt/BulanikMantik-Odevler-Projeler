import numpy as np
import matplotlib.pyplot as plt

# S-Şekilli Sigmoid fonksiyonu
def S_fonksiyonu(u, a, b, c):
    if u <= a:
        return 0
    elif a < u <= b:
        return 2 * ((u - a) / (c - a)) ** 2
    elif b < u < c:
        return 1 - 2 * ((u - c) / (c - a)) ** 2
    else:
        return 1

# Temel sınıf: Üyelik Fonksiyonu
class UyelikFonksiyonu:
    def hesapla(self, u):
        raise NotImplementedError("Bu metot alt sınıflar tarafından implemente edilmelidir.")
    
    def grafikte_goster(self, x_range, u, label):
        y = [self.hesapla(x) for x in x_range]
        plt.plot(x_range, y, label=label)
        
        # U değeri için kesikli çizgiler ve nokta gösterimi
        uyelik_derecesi = self.hesapla(u)
        plt.axvline(x=u, ymin=0, ymax=uyelik_derecesi, color='red', linestyle='--')  # Dikey kesikli çizgi
        plt.axhline(y=uyelik_derecesi, xmin=0, xmax=u, color='red', linestyle='--')  # Yatay kesikli çizgi
        plt.scatter([u], [uyelik_derecesi], color='red')
        plt.text(u, uyelik_derecesi, f"({u}, {uyelik_derecesi:.2f})", fontsize=12, verticalalignment='bottom')

# Pi-Üyelik Fonksiyonu
class PiUyelikFonksiyonu(UyelikFonksiyonu):
    def __init__(self, b, c):
        self.b = b
        self.c = c
    
    def hesapla(self, u):
        if u <= self.c:
            return S_fonksiyonu(u, self.c - self.b, self.c - self.b / 2, self.c)
        else:
            return 1 - S_fonksiyonu(u, self.c, self.c + self.b / 2, self.c + self.b)

# Üçgen Üyelik Fonksiyonu
class UcgenUyelikFonksiyonu(UyelikFonksiyonu):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def hesapla(self, u):
        if u < self.a or u > self.c:
            return 0
        elif self.a <= u < self.b:
            return (u - self.a) / (self.b - self.a)
        elif self.b <= u < self.c:
            return (self.c - u) / (self.c - self.b)
        else:
            return 0

# Yamuk Üyelik Fonksiyonu
class YamukUyelikFonksiyonu(UyelikFonksiyonu):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def hesapla(self, u):
        if u < self.a or u > self.d:
            return 0
        elif self.a <= u < self.b:
            return (u - self.a) / (self.b - self.a)
        elif self.b <= u <= self.c:
            return 1
        elif self.c < u <= self.d:
            return (self.d - u) / (self.d - self.c)
        else:
            return 0

# Pi üyelik fonksiyonunu ayrı grafikle gösterme
def pi_uyelik_grafik(u, x_range):
    plt.figure(figsize=(10, 6))
    pi_fonksiyon = PiUyelikFonksiyonu(20, 50)
    pi_fonksiyon.grafikte_goster(x_range, u, label="Pi Üyelik Fonksiyonu")
    plt.xlabel('u')
    plt.ylabel('Üyelik Derecesi')
    plt.title(f'Pi Üyelik Fonksiyonu ve u={u} için üyelik derecesi')
    plt.grid(True)
    plt.legend()
    plt.show()

# Üçgen üyelik fonksiyonunu ayrı grafikle gösterme
def ucgen_uyelik_grafik(u, x_range):
    plt.figure(figsize=(10, 6))
    ucgen_fonksiyon = UcgenUyelikFonksiyonu(10, 40, 70)
    ucgen_fonksiyon.grafikte_goster(x_range, u, label="Üçgen Üyelik Fonksiyonu")
    plt.xlabel('u')
    plt.ylabel('Üyelik Derecesi')
    plt.title(f'Üçgen Üyelik Fonksiyonu ve u={u} için üyelik derecesi')
    plt.grid(True)
    plt.legend()
    plt.show()

# Yamuk üyelik fonksiyonunu ayrı grafikle gösterme
def yamuk_uyelik_grafik(u, x_range):
    plt.figure(figsize=(10, 6))
    yamuk_fonksiyon = YamukUyelikFonksiyonu(10, 30, 50, 70)
    yamuk_fonksiyon.grafikte_goster(x_range, u, label="Yamuk Üyelik Fonksiyonu")
    plt.xlabel('u')
    plt.ylabel('Üyelik Derecesi')
    plt.title(f'Yamuk Üyelik Fonksiyonu ve u={u} için üyelik derecesi')
    plt.grid(True)
    plt.legend()
    plt.show()

# Kullanıcıdan u değeri alalım
u_degeri = float(input("Bir u değeri girin: "))

# Örnek kullanım
x_range = np.arange(0, 100, 1)

# Her üyelik fonksiyonunu ayrı ayrı göster
pi_uyelik_grafik(u_degeri, x_range)
ucgen_uyelik_grafik(u_degeri, x_range)
yamuk_uyelik_grafik(u_degeri, x_range)
