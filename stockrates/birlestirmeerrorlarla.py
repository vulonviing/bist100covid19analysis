import pandas as pd
import xarray as xr

openclosedata2019 = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2019.csv", index_col=0)
openclosedata2020 = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2020.csv", index_col=(0))
openclosedata2021 = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2021.csv", index_col=(0))
openclosedata2022 = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2022.csv", index_col=(0))
bioen2021 = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\bioen21.xlsx", index_col=(0)).round(2)
esen2021 = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\esen21.xlsx", index_col=(0)).round(2)
krvgd2021 = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\krvgd21.xlsx", index_col=(0)).round(2)
TRILC2021 = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\TRILC21.xlsx", index_col=(0)).round(2)
zrgyo2021 = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\zrgyo21.xlsx", index_col=(0)).round(2)

# openclosedata2021fixed = openclosedata2021.loc[:,["dim_1","BIOEN.IS"]] = 
openclosedata2019a = openclosedata2019.to_xarray()
print(openclosedata2019a.head())

