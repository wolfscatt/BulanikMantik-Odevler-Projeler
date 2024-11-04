import numpy as np
import matplotlib.pyplot as plt

# Evrensel Küme
evrensel_kume = np.arange(20, 81, 1)

# Low ve Medium üyelik fonksiyonları
def low_uyelik(x):
    if 20 <= x <= 25:
        return (x - 20) / (25 - 20)
    elif 25 < x <= 35:
        return 1
    elif 35 < x <= 40:
        return (40 - x) / (40 - 35)
    else:
        return 0

def medium_uyelik(x):
    if 30 <= x <= 42:
        return (x - 30) / (42 - 30)
    elif 42 < x <= 55:
        return 1
    elif 55 < x <= 80:
        return (80 - x) / (80 - 55)
    else:
        return 0

# Low ve Medium kümeleri için üyelik değerleri
low_values = np.array([low_uyelik(x) for x in evrensel_kume])
medium_values = np.array([medium_uyelik(x) for x in evrensel_kume])

# s-norm yöntemleri (birleşim)
birlesim_max = np.maximum(low_values, medium_values)  # Maksimum
birlesim_algebraic_sum = low_values + medium_values - (low_values * medium_values)  # Cebirsel Toplam
birlesim_bounded_sum = np.minimum(1, low_values + medium_values)  # Sınırlı Toplam
birlesim_drastic_sum = np.where(np.maximum(low_values, medium_values) == 0, 0, 1)  # Güçlü Toplam

# t-norm yöntemleri (kesişim)
kesisim_min = np.minimum(low_values, medium_values)  # Minimum
kesisim_algebraic_product = low_values * medium_values  # Cebirsel Çarpım
kesisim_bounded_product = np.maximum(0, low_values + medium_values - 1)  # Sınırlı Çarpım
kesisim_drastic_product = np.where(np.minimum(low_values, medium_values) == 1, np.minimum(low_values, medium_values), 0)  # Güçlü Çarpım

# Low ve Medium kümeleri grafiği
plt.figure(figsize=(8, 4))
plt.plot(evrensel_kume, low_values, label="Low", color="blue")
plt.plot(evrensel_kume, medium_values, label="Med", color="orange")
plt.xlabel("Sıcaklık")
plt.ylabel("Üyelik Derecesi")
plt.title("Low ve Medium Kümeleri")
plt.legend()
plt.grid(True)

# Birleşim grafikleri (s-norm yöntemleri)
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(evrensel_kume, birlesim_max, label="Birleşim - Maksimum", color="red")
plt.xlabel("Sıcaklık")
plt.ylabel("Üyelik Derecesi")
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(evrensel_kume, birlesim_algebraic_sum, label="Birleşim - Cebirsel Toplam", color="purple")
plt.xlabel("Sıcaklık")
plt.ylabel("Üyelik Derecesi")
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(evrensel_kume, birlesim_bounded_sum, label="Birleşim - Sınırlı Toplam", color="green")
plt.xlabel("Sıcaklık")
plt.ylabel("Üyelik Derecesi")
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(evrensel_kume, birlesim_drastic_sum, label="Birleşim - Güçlü Toplam", color="brown")
plt.xlabel("Sıcaklık")
plt.ylabel("Üyelik Derecesi")
plt.legend()
plt.grid(True)

# Kesişim grafikleri (t-norm yöntemleri)
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(evrensel_kume, kesisim_min, label="Kesişim - Minimum", color="red")
plt.xlabel("Sıcaklık")
plt.ylabel("Üyelik Derecesi")
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(evrensel_kume, kesisim_algebraic_product, label="Kesişim - Cebirsel Çarpım", color="purple")
plt.xlabel("Sıcaklık")
plt.ylabel("Üyelik Derecesi")
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(evrensel_kume, kesisim_bounded_product, label="Kesişim - Sınırlı Çarpım", color="green")
plt.xlabel("Sıcaklık")
plt.ylabel("Üyelik Derecesi")
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(evrensel_kume, kesisim_drastic_product, label="Kesişim - Güçlü Çarpım", color="brown")
plt.xlabel("Sıcaklık")
plt.ylabel("Üyelik Derecesi")
plt.legend()
plt.grid(True)

# Grafiklerin gösterilmesi
plt.show()
