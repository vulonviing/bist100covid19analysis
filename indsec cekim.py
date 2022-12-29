import pandas as pd

ind_2020_4 = pd.read_csv("C:/Users/emrec/Desktop/TUBITAK 22 DOSYASI/BIST100_2020/BIST100_2020_4_industryS.csv", index_col=0)
sec_2020_4 = pd.read_csv("C:/Users/emrec/Desktop/TUBITAK 22 DOSYASI/BIST100_2020/BIST100_2020_4_SECTORS.csv", index_col=0)

indsec_2020_4 = pd.merge(ind_2020_4,sec_2020_4,on="HISSE")

#----

ind_2020_3 = pd.read_csv("C:/Users/emrec/Desktop/TUBITAK 22 DOSYASI/BIST100_2020/BIST100_2020_3_industryS.csv", index_col=0)
sec_2020_3 = pd.read_csv("C:/Users/emrec/Desktop/TUBITAK 22 DOSYASI/BIST100_2020/BIST100_2020_3_SECTORS.csv", index_col=0)

indsec_2020_3 = pd.merge(ind_2020_3,sec_2020_3,on="HISSE")

#----

ind_2020_2 = pd.read_csv("C:/Users/emrec/Desktop/TUBITAK 22 DOSYASI/BIST100_2020/BIST100_2020_2_industryS.csv", index_col=0)
sec_2020_2 = pd.read_csv("C:/Users/emrec/Desktop/TUBITAK 22 DOSYASI/BIST100_2020/BIST100_2020_2_SECTORS.csv", index_col=0)

indsec_2020_2 = pd.merge(ind_2020_2,sec_2020_2,on="HISSE")

#----

ind_2020_1 = pd.read_csv("C:/Users/emrec/Desktop/TUBITAK 22 DOSYASI/BIST100_2020/BIST100_2020_1_industryS.csv", index_col=0)
sec_2020_1 = pd.read_csv("C:/Users/emrec/Desktop/TUBITAK 22 DOSYASI/BIST100_2020/BIST100_2020_1_SECTORS.csv", index_col=0)

indsec_2020_1 = pd.merge(ind_2020_1,sec_2020_1,on="HISSE")

indsec_2020a = pd.merge(indsec_2020_3, indsec_2020_4, on="HISSE", how= "outer", suffixes=("-3", "-4"))
indsec_2020b = pd.merge(indsec_2020_1, indsec_2020_2, on="HISSE", how= "outer", suffixes=("-1", "-2"))
indsec_2020 = pd.merge(indsec_2020b, indsec_2020a, on="HISSE", how= "outer", suffixes=("-a", "-b"))

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

print(indsec_2020_1)

# yol = r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\BIST100_2020_indsec.csv"

#indsec_2020.to_csv(yol)