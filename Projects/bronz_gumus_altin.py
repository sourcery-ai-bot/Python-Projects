# -*- coding: utf-8 -*-
"""
Automatically generated by Colaboratory.

Original file is located at https://colab.research.google.com/drive/1wsqjmxphjqnMtR2OWHzLxRGuxnpzUAyZ?usp=sharing


Between years 1896-2008, the number of bronze, silver and gold medals won in summer Olympics was recorded. 196 countries participated in the Olympics.
Human Development Index (HDI) is a measure of human development. It is a measure prepared for countries in the world in terms of life expectancy, literacy rate, education and life level.

Links for datasets:
    bronz.xlsx - https://docs.google.com/spreadsheets/d/1ZaRsdZW6aCK1-TBMy8mpaztEjIJERMQ9/edit?usp=sharing&ouid=110194071483775980581&rtpof=true&sd=true
    gumus.xlsx - https://docs.google.com/spreadsheets/d/1ZO-VhtbMXlA8bJdDECqvY1tKXtRCEVR9/edit?usp=sharing&ouid=110194071483775980581&rtpof=true&sd=true
    altin.xlsx - https://docs.google.com/spreadsheets/d/1nFc5PNAyRnfBjuhf3c-c8bnRUfAwuWJd/edit?usp=sharing&ouid=110194071483775980581&rtpof=true&sd=true
    insani_gelisim_indeksi.xlsx - https://docs.google.com/spreadsheets/d/1kDITTt_uR7Um_aP7yYVUg3NMWYCpf1o-/edit?usp=sharing&ouid=110194071483775980581&rtpof=true&sd=true

"""
# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading datasets
bronz_df = pd.read_excel('bronz.xlsx')
gumus_df = pd.read_excel('gumus.xlsx')
altin_df = pd.read_excel('altin.xlsx')
insani_gelisim_indeksi_df = pd.read_excel('insani_gelisim_indeksi.xlsx')

# Merging bronze, silver and gold datasets
bronz_gumus_df = pd.merge(bronz_df, gumus_df, how="outer", on="Country", suffixes=["_Bronz", "_Gumus"])
bronz_gumus_altin_df = pd.merge(altin_df, bronz_gumus_df, how="outer", on="Country", suffixes=["_Altin", "_Medals"])
bronz_gumus_altin_df = bronz_gumus_altin_df.replace(np.nan, 0)
madalya_df = bronz_gumus_altin_df.drop(labels=["NOC_Bronz", "NOC_Gumus"], axis=1)
madalya_df["Total_Medals"] = madalya_df.sum(axis=1)
print(madalya_df)

# Renaming columns' name
df_madalya = madalya_df.rename(
    columns={"Country": "Ulke", "Total": "Altin", "Total_Bronz": "Bronz", "Total_Gumus": "Gumus",
             "Total_Medals": "Toplam"})
print(df_madalya)

# Merging madalya_df with HDI dataset and renaming columns' name
df_ulkeler = pd.merge(madalya_df, insani_gelisim_indeksi_df, how="inner", on="Country")
df_ulkeler = df_ulkeler.rename(
    columns={"Country": "Ulke", "Total": "Altin", "Total_Bronz": "Bronz", "Total_Gumus": "Gumus",
             "Total_Medals": "Toplam", "2008_Human Development Index": "2008_Insani Gelisim Indeksi"})
print(df_ulkeler)

# Plotting scatter graph of distribution chart of countries' human development index by total medals
plt.scatter(df_ulkeler["Toplam"], df_ulkeler["2008_Insani Gelisim Indeksi"], marker="*", color="blue")
plt.xlabel("Toplam Madalya Sayisi")
plt.ylabel("2008 Insani Gelisim Indeksi")
plt.title("Ulkelerin Insani Gelisim Endeksinin Toplam Madalya Sayisina gore Dagilim Grafigi")
plt.show()

# Plotting bar graph of graph of gold and total medal numbers of countries with human development index above 0.9
df_ulkeler_up_09 = df_ulkeler.loc[df_ulkeler["2008_Insani Gelisim Indeksi"] >= 0.9]
plt.bar(df_ulkeler_up_09["Ulke"], df_ulkeler_up_09["Toplam"], color="red", width=0.3)
plt.bar(df_ulkeler_up_09["Ulke"], df_ulkeler_up_09["Altin"], color="blue", width=0.3)
plt.ylabel("Madalya Sayisi")
plt.xlabel("Ulke Isimleri")
plt.xticks(rotation="vertical")
plt.title("Insani Gelisim Indeksi 0.9 Uzeri Olan Ulkelerin Altın ve Toplam Madalya Sayıları Grafigi")
plt.show()
