# 11--DENEY-TASARIMI

# 🧪 Deney Tasarımı (Experimental Design) README

## 📌 Giriş (Introduction)
Deney Tasarımı (Experimental Design), değişkenlerin etkilerini anlamak ve veri odaklı kararlar almak için kullanılan bilimsel bir yöntemdir. Bu yöntem, özellikle **istatistik, veri bilimi, psikoloji, ekonomi ve mühendislik** gibi alanlarda kullanılır. 🚀

Bu repo, deney tasarımının temel prensipleri, istatistiksel testler ve Python ile uygulamalar içermektedir. 📊

---

## 🚀 Kurulum (Installation)
Aşağıdaki komutla gerekli Python kütüphanelerini yükleyebilirsiniz:

```bash
pip install numpy pandas scipy statsmodels matplotlib seaborn
```

---

## 🔥 Kullanılan Kütüphaneler (Libraries Used)

1. **NumPy** 🔢 - Sayısal işlemler.
2. **Pandas** 📊 - Veri manipülasyonu.
3. **SciPy** 📈 - İstatistiksel testler.
4. **Statsmodels** 🧮 - Regresyon analizleri ve ANOVA testleri.
5. **Matplotlib & Seaborn** 🎨 - Veri görselleştirme.

---

## 📚 Deney Tasarımı Temel Kavramları
Deney tasarımında aşağıdaki temel bileşenler kullanılır:

- **Bağımsız Değişken (Independent Variable)**: Manipüle edilen değişken.
- **Bağımlı Değişken (Dependent Variable)**: Etkisi ölçülen değişken.
- **Kontrol Grubu (Control Group)**: Deneysel müdahale yapılmayan grup.
- **Deney Grubu (Experimental Group)**: Müdahale edilen grup.
- **Örnekleme (Sampling)**: Rastgele veya belirli yöntemlerle seçilen örnekler.

### 📌 Deney Türleri
- **Tek Faktörlü Deneyler**: Tek bağımsız değişken incelenir.
- **Faktöriyel Deneyler**: Birden fazla bağımsız değişkenin etkisi analiz edilir.
- **A/B Testleri**: İki farklı versiyonun performansı karşılaştırılır.
- **Tam Rastgele Deneyler**: Denekler rastgele gruplara atanır.

---

## 🏗️ Örnek Kullanım (Examples)

### 📌 A/B Testi için Örnek Python Kodu
```python
import numpy as np
import scipy.stats as stats

# Rastgele oluşturulan dönüşüm oranları
A = np.random.binomial(n=1000, p=0.12, size=1)  # A grubu (kontrol)
B = np.random.binomial(n=1000, p=0.15, size=1)  # B grubu (deney)

# İstatistiksel anlamlılık testi (Chi-Square)
chi2, p_value = stats.chisquare([A, B])
print(f"Chi-Square Test Sonucu: {chi2}, P-değeri: {p_value}")
```

### 📊 ANOVA Testi ile Birden Fazla Grubu Karşılaştırma
```python
import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd

# Örnek veri seti
data = pd.DataFrame({
    "grup": np.repeat(["A", "B", "C"], 10),
    "skor": np.random.randint(50, 100, 30)
})

# ANOVA modeli oluşturma
model = ols("skor ~ grup", data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)
```

---

## 📚 Ek Kaynaklar (Additional Resources)
- [A/B Testing Explained](https://www.optimizely.com/ab-testing/)
- [Statsmodels Documentation](https://www.statsmodels.org/)
- [ANOVA in Python](https://www.pythonfordatascience.org/anova-python/)

---

## 📌 Katkı Yapma (Contributing)
Projeye katkı sağlamak isterseniz fork'layın, geliştirin ve PR gönderin! 🚀

---

## 📜 Lisans (License)
Bu proje MIT lisansı altındadır, dilediğiniz gibi kullanabilirsiniz! 😊

