import pandas as pd

finaldata2019 = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\datastore manipulation\new2019\BIST100_2019_indsec.csv", index_col=0)
finaldata2020 = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\datastore manipulation\new2020\BIST100_2020_indsec.csv", index_col=0)
finaldata2021 = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\datastore manipulation\new2021\BIST100_2021_indsec.csv", index_col=0)
finaldata2022 = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\datastore manipulation\new2022\BIST100_2022_indsec.csv", index_col=0)

a = finaldata2022.merge(finaldata2021, on="HISSE", how="outer")
b = finaldata2020.merge(finaldata2019, on="HISSE", how="outer")

finaldata = a.merge(b, on="HISSE", how="outer")
finaldatasorted = finaldata.sort_values(by="HISSE").reset_index(drop=True)

print(finaldata.head())

finaldatasorted.to_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\datastore manipulation\finaldata.csv")