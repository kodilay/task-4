
"""
## 1. read_csv() - CSV Dosyası Okuma
"""
import pandas as pd

# CSV dosyasını okuma
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print("İlk 5 satır:")
print(df.head())

"""
## 2. head() / tail() - İlk/Son Satırları Görüntüleme
"""

# İlk 3 satır
print("İlk 3 satır:")
print(df.head(3))

# Son 2 satır
print("\nSon 2 satır:")
print(df.tail(2))

"""
## 3. info() - DataFrame Bilgileri
"""

# DataFrame hakkında özet bilgi
print(df.info())


"""
## 4. describe() - İstatistiksel Özet
"""

# Sayısal sütunların istatistikleri
print(df.describe())


"""
## 5. groupby() - Gruplandırma
"""

# Türlere göre gruplandırma ve ortalama alma
grouped = df.groupby('species').mean()
print(grouped)

"""
## 6. fillna() - Eksik Veri Doldurma
"""

# Eksik veri içeren örnek DataFrame
import numpy as np
df_nan = pd.DataFrame({'A': [1, np.nan, 3], 'B': [np.nan, 5, 6]})
print("Orijinal DataFrame:")
print(df_nan)

# Eksik değerleri 0 ile doldurma
filled_df = df_nan.fillna(0)
print("\nDoldurulmuş DataFrame:")
print(filled_df)


"""
## 7. merge() - DataFrame Birleştirme
"""

# İki DataFrame oluşturma
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value': [4, 5, 6]})

# Inner join ile birleştirme
merged = pd.merge(df1, df2, on='key', how='inner')
print(merged)

"""
## 8. pivot_table() - Özet Tablosu
"""
# Örnek satış verisi
sales = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02'],
    'Product': ['A', 'B', 'A'],
    'Sales': [100, 200, 150]
})

# Pivot tablosu oluşturma
pivot = pd.pivot_table(sales, values='Sales', index='Date', columns='Product')
print(pivot)

"""
## 9. apply() - Fonksiyon Uygulama
"""

# Sepal_length sütununa fonksiyon uygulama
df['sepal_length_cm'] = df['sepal_length'].apply(lambda x: x * 10)
print(df[['sepal_length', 'sepal_length_cm']].head())

"""
## 10. sort_values() - Sıralama
"""
# Petal_length'e göre sıralama
sorted_df = df.sort_values('petal_length', ascending=False)
print("Büyükten küçüğe sıralama:")
print(sorted_df.head(5))
