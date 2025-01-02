import skfuzzy as fuzz
import skfuzzy.membership as mf
import numpy as np
import matplotlib.pyplot as plt

#region Optimize Code
var_model=np.arange(2002,2013,1)
var_km=np.arange(0,100001,1)
var_fiyat=np.arange(0,40001,1)

# Bu uygulama için üçgen üyelik fonksiyonlarını oluşturmak için bu fonksiyon yazıldı.
def ucgenUyelikFun(var_kume, abc,) :
   if(len(abc) == 0):
      return
   if(len(abc) == 1):
      set_model_dusuk = mf.trimf(var_kume, abc[0])
      return set_model_dusuk
   if(len(abc) == 2):
      set_model_dusuk = mf.trimf(var_kume, abc[0])
      set_model_orta = mf.trimf(var_kume, abc[1])
      return set_model_dusuk, set_model_orta
   if(len(abc) == 3):
      set_model_dusuk = mf.trimf(var_kume, abc[0])
      set_model_orta = mf.trimf(var_kume, abc[1])
      set_model_yuksek = mf.trimf(var_kume, abc[2])
      return set_model_dusuk, set_model_orta, set_model_yuksek


set_model_dusuk, set_model_orta, set_model_yuksek = ucgenUyelikFun(var_model, [[2002,2002,2007], [2002,2007,2012], [2007, 2012, 2012]])
set_km_dusuk, set_km_orta, set_km_yuksek = ucgenUyelikFun(var_km, [[0,0,50000], [0,50000,100000], [50000,100000,100000]])
set_fiyat_dusuk, set_fiyat_orta, set_fiyat_yuksek = ucgenUyelikFun(var_fiyat, [[0,0,20000], [0,20000,40000], [20000,40000,40000]])

set_model = [set_model_dusuk, set_model_orta, set_model_yuksek]
set_km = [set_km_dusuk, set_km_orta, set_km_yuksek]
set_fiyat = [set_fiyat_dusuk, set_fiyat_orta, set_fiyat_yuksek]

# Çizdirme işlemleri için figür oluşturuluyor
fig,(ax0,ax1,ax2,ax3,ax4)=plt.subplots(nrows=5,figsize=(15,20))

# Genel çizdirme fonksiyonu
def plot_membership_functions(ax, var, sets, labels, title, colors, linestyles):
   if linestyles == None:
      for s, label, color in zip(sets, labels, colors):
         ax.plot(var, s, color, linewidth=2, label=label)
   else:
      for s, label, color, linestyle in zip(sets, labels, colors, linestyles):
         ax.plot(var, s, color, linestyle = linestyle, linewidth=2, label=label)
   ax.set_title(title)
   ax.legend()

plot_membership_functions(ax0, var_model, set_model, ["Düşük", "Orta", "Yüksek"], "Model", ["r", "g", "b"], None)
plot_membership_functions(ax1, var_km, set_km, ["Düşük", "Orta", "Yüksek"], "Kilometre", ["r", "g", "b"], None)
plot_membership_functions(ax2, var_fiyat, set_fiyat, ["Düşük", "Orta", "Yüksek"], "Fiyat", ["r", "g", "b"], None)

input_model=2011
input_km=25000

def interp_membership(var_kume, sets, input):
      return [fuzz.interp_membership(var_kume, s, input) for s in sets]

model_fit_dusuk, model_fit_orta, model_fit_yuksek = interp_membership(var_model, set_model, input_model)
km_fit_dusuk, km_fit_orta, km_fit_yuksek = interp_membership(var_km, set_km, input_km)

fit_model = [model_fit_dusuk, model_fit_orta, model_fit_yuksek]
fit_km = [km_fit_dusuk, km_fit_orta, km_fit_yuksek]

# Üyelik fonksiyonlarının grafikleri üzerinde inputların denk geldiği nokta ve çizgiler çiziliyor.
def plot_membership_lines(ax, input, fits, var, color):
    for fit in fits:
        ax.plot([input, input], [0, fit], color, linewidth=1, linestyle='--')
        ax.plot([var[0], input], [fit, fit], color, linewidth=1, linestyle='--')

plot_membership_lines(ax0, input_model, fit_model, var_model, "r")
plot_membership_lines(ax1, input_km, fit_km, var_km, "r")

# Kurallar
rule1 = np.fmin(np.fmin(model_fit_dusuk, km_fit_yuksek), set_fiyat_dusuk)
rule2 = np.fmin(np.fmin(model_fit_orta, km_fit_orta), set_fiyat_orta)
rule3 = np.fmin(np.fmin(model_fit_yuksek, km_fit_dusuk), set_fiyat_yuksek)

plot_membership_functions(ax3, var_fiyat, [rule1, rule2, rule3], ["Rule-1", "Rule-2", "Rule-3"], "Her bir kuraldan elde edilen çıkış kümeleri", ["r", "b", "g"], ["--","-.",":"])

def combine_rules(*args):
    out = args[0]
    for rule in args[1:]:
        out = np.fmax(out, rule)
    return out

out_set_final = combine_rules(rule1, rule2, rule3)
ax4.fill_between(var_fiyat,out_set_final, 'b', linestyle=':', linewidth=2, label='out')
ax4.set_title("Çıkış-Bulanık Küme Birleşimi")

#Durulama Yöntemleri
# 'centroid' — Centroid of the area under the output fuzzy set
# 'bisector' — Bisector of the area under the output fuzzy set
# 'mom' — Mean of the values for which the output fuzzy set is maximum
# 'lom' — Largest value for which the output fuzzy set is maximum
# 'som' — Smallest value for which the output fuzzy set is maximum

def defuzzify_all(var_fiyat, out_set_final):
   defuzzified_values = {
      'centroid': fuzz.defuzz(var_fiyat, out_set_final, 'centroid'),
      'bisector': fuzz.defuzz(var_fiyat, out_set_final, 'bisector'),
      'mom': fuzz.defuzz(var_fiyat, out_set_final, 'mom'),
      'lom': fuzz.defuzz(var_fiyat, out_set_final, 'lom'),
      'som': fuzz.defuzz(var_fiyat, out_set_final, 'som')
   }
    
    # Sonuçları yazdır
   for method, value in defuzzified_values.items():
      print(f"Fiyat({method}) = {value}")
        
   return defuzzified_values["centroid"]

centroid = defuzzify_all(var_fiyat, out_set_final)
result = fuzz.interp_membership(var_fiyat, out_set_final, centroid)
ax4.plot([0,centroid],[result,result],'r')
ax4.plot([centroid,centroid],[0,result],'r')

plt.show()
#endregion
