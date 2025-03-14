import numpy as np
import scipy.stats as stats

# 📌 1. A/B Grubu Tıklama Verileri
A_grubu_tiklama = np.array([150, 160, 170, 145, 155, 165, 175, 180])  # Mavi Buton
B_grubu_tiklama = np.array([180, 190, 200, 170, 185, 195, 205, 210])  # Yeşil Buton

# 📌 2. Ortalama ve Standart Sapmaları Hesapla
ortalama_A = np.mean(A_grubu_tiklama)
ortalama_B = np.mean(B_grubu_tiklama)
std_A = np.std(A_grubu_tiklama, ddof=1)
std_B = np.std(B_grubu_tiklama, ddof=1)

print(f"A Grubu (Mavi) Ortalama: {ortalama_A}, Standart Sapma: {std_A}")
print(f"B Grubu (Yeşil) Ortalama: {ortalama_B}, Standart Sapma: {std_B}")

# 📌 3. t-Testi Yap (İki grubun farkı anlamlı mı?)
t_stat, p_degeri = stats.ttest_ind(A_grubu_tiklama, B_grubu_tiklama)

print(f"t-İstatistiği: {t_stat}")
print(f"p-Değeri: {p_degeri}")

# 📌 4. Sonucu Değerlendir
alpha = 0.05  # Güven aralığı %95
if p_degeri < alpha:
    print("Sonuç: Yeşil buton, Mavi butona göre anlamlı şekilde daha fazla tıklama aldı! ✅")
else:
    print("Sonuç: Fark istatistiksel olarak anlamlı değil. ❌")
