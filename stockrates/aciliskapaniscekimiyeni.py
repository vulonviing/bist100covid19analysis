import pandas as pd
import yfinance as yf
from datetime import datetime as datetime
import numpy as np

xr19 = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\datastore manipulation\new2019\BIST100_2019_indsecv2.csv").sort_values(by="HISSE")
xr20 = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\datastore manipulation\new2020\BIST100_2020_indsecv2.csv").sort_values(by="HISSE")
xr21 = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\datastore manipulation\new2021\BIST100_2021_indsecv2.csv").sort_values(by="HISSE")
xr22 = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\datastore manipulation\new2022\BIST100_2022_indsecv2.csv").sort_values(by="HISSE")

xrstocks19 = xr19["HISSE"]
xrstocks20 = xr20["HISSE"]
xrstocks21 = xr21["HISSE"]
xrstocks22 = xr22["HISSE"]

stocks19 = [s1 + ".IS" for s1 in xrstocks19]
stocks20 = [s2 + ".IS" for s2 in xrstocks20]
stocks21 = [s3 + ".IS" for s3 in xrstocks21]
stocks22 = [s4 + ".IS" for s4 in xrstocks22]

_start19 = datetime(2019,1,1)
_end19 = datetime(2020,1,1)
_start20 = datetime(2020,1,1)
_end20 = datetime(2021,1,1)
_start21 = datetime(2021,1,1)
_end21 = datetime(2022,1,1)
_start22 = datetime(2022,1,1)
_end22 = datetime(2023,1,1)

df_3d19a = yf.download(stocks19, start=_start19, end=_end19).round(2)
df_3d20a = yf.download(stocks20, start=_start20, end=_end20).round(2)
df_3d21a = yf.download(stocks21, start=_start21, end=_end21).round(2)
df_3d22a = yf.download(stocks22, start=_start22, end=_end22).round(2)
df_3d19 = df_3d19a[["High", "Low", "Close"]]
df_3d20 = df_3d20a[["High", "Low", "Close"]]
df_3d21 = df_3d21a[["High", "Low", "Close"]]
df_3d22 = df_3d22a[["High", "Low", "Close"]]

#xr_3d19.to_netcdf(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2019.nc")
df_3d19.to_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2019.xlsx")
df_3d19.to_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2019.csv")
#xr_3d20.to_netcdf(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2020.nc")
df_3d20.to_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2020.xlsx")
df_3d20.to_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2020.csv")
#xr_3d21.to_netcdf(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2021.nc")
df_3d21.to_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2021.xlsx")
df_3d21.to_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2021.csv")
#xr_3d22.to_netcdf(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2022.nc")
df_3d22.to_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2022.xlsx")
df_3d22.to_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\BIST100_2022.csv")

A = np.array(["High", "Low", "Close"]) #main columns for 3d error data sets

# for year 21--------------
bioen21a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\bioen21.xlsx")
bioen21a["Tarih"] = pd.to_datetime(bioen21a["Tarih"], format='%d-%m-%Y')
bioen21b = bioen21a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
bioen21c = bioen21b[["Date", "High", "Low", "Close"]]
bioencolumns = np.array(["BIOEN.IS"]*3)
bioendata = np.array(bioen21c[["High", "Low", "Close"]].set_index(bioen21b["Date"]))
bioendates = bioen21c["Date"]
bioen21_3d = pd.DataFrame(bioendata, columns=pd.MultiIndex.from_tuples(zip(A,bioencolumns)), index=bioendates)
df_3d21.loc[:, pd.IndexSlice[:, "BIOEN.IS"]] = bioen21_3d #df_3d21 is still main for 2021---

esen21a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\esen21.xlsx")
esen21a["Tarih"] = pd.to_datetime(esen21a["Tarih"], format='%d-%m-%Y')
esen21b = esen21a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
esen21c = esen21b[["Date", "High", "Low", "Close"]]
esencolumns = np.array(["ESEN.IS"]*3)
esendata = np.array(esen21c[["High", "Low", "Close"]].set_index(esen21b["Date"]))
esendates = esen21c["Date"]
esen21_3d = pd.DataFrame(esendata, columns=pd.MultiIndex.from_tuples(zip(A,esencolumns)), index=esendates)
df_3d21.loc[:, pd.IndexSlice[:, "ESEN.IS"]] = esen21_3d #df_3d21 is still main for 2021---

zrgyo21a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\zrgyo21.xlsx")
zrgyo21a["Tarih"] = pd.to_datetime(zrgyo21a["Tarih"], format='%d-%m-%Y')
zrgyo21b = zrgyo21a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
zrgyo21c = zrgyo21b[["Date", "High", "Low", "Close"]]
zrgyocolumns = np.array(["ZRGYO.IS"]*3)
zrgyodata = np.array(zrgyo21c[["High", "Low", "Close"]].set_index(zrgyo21b["Date"]))
zrgyodates = zrgyo21c["Date"]
zrgyo21_3d = pd.DataFrame(zrgyodata, columns=pd.MultiIndex.from_tuples(zip(A,zrgyocolumns)), index=zrgyodates)
df_3d21.loc[:, pd.IndexSlice[:, "ZRGYO.IS"]] = zrgyo21_3d #df_3d21 is still main for 2021---

krvgd21a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\krvgd21.xlsx")
krvgd21a["Tarih"] = pd.to_datetime(krvgd21a["Tarih"], format='%d-%m-%Y')
krvgd21b = krvgd21a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
krvgd21c = krvgd21b[["Date", "High", "Low", "Close"]]
krvgdcolumns = np.array(["KRVGD.IS"]*3)
krvgddata = np.array(krvgd21c[["High", "Low", "Close"]].set_index(krvgd21b["Date"]))
krvgddates = krvgd21c["Date"]
krvgd21_3d = pd.DataFrame(krvgddata, columns=pd.MultiIndex.from_tuples(zip(A,krvgdcolumns)), index=krvgddates)
df_3d21.loc[:, pd.IndexSlice[:, "KRVGD.IS"]] = krvgd21_3d #df_3d21 is still main for 2021---

TRILC21a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\TRILC21.xlsx")
TRILC21a["Tarih"] = pd.to_datetime(TRILC21a["Tarih"], format='%d-%m-%Y')
TRILC21b = TRILC21a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
TRILC21c = TRILC21b[["Date", "High", "Low", "Close"]]
TRILCcolumns = np.array(["TRILC.IS"]*3)
TRILCdata = np.array(TRILC21c[["High", "Low", "Close"]].set_index(TRILC21b["Date"]))
TRILCdates = TRILC21c["Date"]
TRILC21_3d = pd.DataFrame(TRILCdata, columns=pd.MultiIndex.from_tuples(zip(A,TRILCcolumns)), index=TRILCdates)
df_3d21.loc[:, pd.IndexSlice[:, "TRILC.IS"]] = TRILC21_3d #df_3d21 is still main for 2021---

df_3d21.to_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\eksiklerieklenmis\df_3d21.xlsx")
df_3d21.to_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\eksiklerieklenmis\df_3d21.csv")
# end of year 21-----------

# for year 22--------------
ARASE22a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\ARASE22.xlsx")
ARASE22a["Tarih"] = pd.to_datetime(ARASE22a["Tarih"], format='%d-%m-%Y')
ARASE22b = ARASE22a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
ARASE22c = ARASE22b[["Date", "High", "Low", "Close"]]
ARASEcolumns = np.array(["ARASE.IS"]*3)
ARASEdata = np.array(ARASE22c[["High", "Low", "Close"]].set_index(ARASE22b["Date"]))
ARASEdates = ARASE22c["Date"]
ARASE22_3d = pd.DataFrame(ARASEdata, columns=pd.MultiIndex.from_tuples(zip(A,ARASEcolumns)), index=ARASEdates)
df_3d22.loc[:, pd.IndexSlice[:, "ARASE.IS"]] = ARASE22_3d #df_3d21 is still main for 2022---

ESEN22a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\ESEN22.xlsx")
ESEN22a["Tarih"] = pd.to_datetime(ESEN22a["Tarih"], format='%d-%m-%Y')
ESEN22b = ESEN22a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
ESEN22c = ESEN22b[["Date", "High", "Low", "Close"]]
ESENcolumns = np.array(["ESEN.IS"]*3)
ESENdata = np.array(ESEN22c[["High", "Low", "Close"]].set_index(ESEN22b["Date"]))
ESENdates = ESEN22c["Date"]
ESEN22_3d = pd.DataFrame(ESENdata, columns=pd.MultiIndex.from_tuples(zip(A,ESENcolumns)), index=ESENdates)
df_3d22.loc[:, pd.IndexSlice[:, "ESEN.IS"]] = ESEN22_3d #df_3d21 is still main for 2022---

GENIL22a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\GENIL22.xlsx")
GENIL22a["Tarih"] = pd.to_datetime(GENIL22a["Tarih"], format='%d-%m-%Y')
GENIL22b = GENIL22a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
GENIL22c = GENIL22b[["Date", "High", "Low", "Close"]]
GENILcolumns = np.array(["GENIL.IS"]*3)
GENILdata = np.array(GENIL22c[["High", "Low", "Close"]].set_index(GENIL22b["Date"]))
GENILdates = GENIL22c["Date"]
GENIL22_3d = pd.DataFrame(GENILdata, columns=pd.MultiIndex.from_tuples(zip(A,GENILcolumns)), index=GENILdates)
df_3d22.loc[:, pd.IndexSlice[:, "GENIL.IS"]] = GENIL22_3d #df_3d21 is still main for 2022---

GWIND22a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\GWIND22.xlsx")
GWIND22a["Tarih"] = pd.to_datetime(GWIND22a["Tarih"], format='%d-%m-%Y')
GWIND22b = GWIND22a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
GWIND22c = GWIND22b[["Date", "High", "Low", "Close"]]
GWINDcolumns = np.array(["GWIND.IS"]*3)
GWINDdata = np.array(GWIND22c[["High", "Low", "Close"]].set_index(GWIND22b["Date"]))
GWINDdates = GWIND22c["Date"]
GWIND22_3d = pd.DataFrame(GWINDdata, columns=pd.MultiIndex.from_tuples(zip(A,GWINDcolumns)), index=GWINDdates)
df_3d22.loc[:, pd.IndexSlice[:, "GWIND.IS"]] = GWIND22_3d #df_3d21 is still main for 2022---

KRVGD22a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\KRVGD22.xlsx")
KRVGD22a["Tarih"] = pd.to_datetime(KRVGD22a["Tarih"], format='%d-%m-%Y')
KRVGD22b = KRVGD22a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
KRVGD22c = KRVGD22b[["Date", "High", "Low", "Close"]]
KRVGDcolumns = np.array(["KRVGD.IS"]*3)
KRVGDdata = np.array(KRVGD22c[["High", "Low", "Close"]].set_index(KRVGD22b["Date"]))
KRVGDdates = KRVGD22c["Date"]
KRVGD22_3d = pd.DataFrame(KRVGDdata, columns=pd.MultiIndex.from_tuples(zip(A,KRVGDcolumns)), index=KRVGDdates)
df_3d22.loc[:, pd.IndexSlice[:, "KRVGD.IS"]] = KRVGD22_3d #df_3d21 is still main for 2022---

SMRTG22a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\SMRTG22.xlsx")
SMRTG22a["Tarih"] = pd.to_datetime(SMRTG22a["Tarih"], format='%d-%m-%Y')
SMRTG22b = SMRTG22a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
SMRTG22c = SMRTG22b[["Date", "High", "Low", "Close"]]
SMRTGcolumns = np.array(["SMRTG.IS"]*3)
SMRTGdata = np.array(SMRTG22c[["High", "Low", "Close"]].set_index(SMRTG22b["Date"]))
SMRTGdates = SMRTG22c["Date"]
SMRTG22_3d = pd.DataFrame(SMRTGdata, columns=pd.MultiIndex.from_tuples(zip(A,SMRTGcolumns)), index=SMRTGdates)
df_3d22.loc[:, pd.IndexSlice[:, "SMRTG.IS"]] = SMRTG22_3d #df_3d21 is still main for 2022---

TRILC22a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\TRILC22.xlsx")
TRILC22a["Tarih"] = pd.to_datetime(TRILC22a["Tarih"], format='%d-%m-%Y')
TRILC22b = TRILC22a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
TRILC22c = TRILC22b[["Date", "High", "Low", "Close"]]
TRILCcolumns = np.array(["TRILC.IS"]*3)
TRILCdata = np.array(TRILC22c[["High", "Low", "Close"]].set_index(TRILC22b["Date"]))
TRILCdates = TRILC22c["Date"]
TRILC22_3d = pd.DataFrame(TRILCdata, columns=pd.MultiIndex.from_tuples(zip(A,TRILCcolumns)), index=TRILCdates)
df_3d22.loc[:, pd.IndexSlice[:, "TRILC.IS"]] = TRILC22_3d #df_3d21 is still main for 2022---

YYLGD22a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\YYLGD22.xlsx")
YYLGD22a["Tarih"] = pd.to_datetime(YYLGD22a["Tarih"], format='%d-%m-%Y')
YYLGD22b = YYLGD22a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
YYLGD22c = YYLGD22b[["Date", "High", "Low", "Close"]]
YYLGDcolumns = np.array(["YYLGD.IS"]*3)
YYLGDdata = np.array(YYLGD22c[["High", "Low", "Close"]].set_index(YYLGD22b["Date"]))
YYLGDdates = YYLGD22c["Date"]
YYLGD22_3d = pd.DataFrame(YYLGDdata, columns=pd.MultiIndex.from_tuples(zip(A,YYLGDcolumns)), index=YYLGDdates)
df_3d22.loc[:, pd.IndexSlice[:, "YYLGD.IS"]] = YYLGD22_3d #df_3d21 is still main for 2022---

GESAN22a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\GESAN22.xlsx")
GESAN22a["Tarih"] = pd.to_datetime(GESAN22a["Tarih"], format='%d-%m-%Y')
GESAN22b = GESAN22a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
GESAN22c = GESAN22b[["Date", "High", "Low", "Close"]]
GESANcolumns = np.array(["GESAN.IS"]*3)
GESANdata = np.array(GESAN22c[["High", "Low", "Close"]].set_index(GESAN22b["Date"]))
GESANdates = GESAN22c["Date"]
GESAN22_3d = pd.DataFrame(GESANdata, columns=pd.MultiIndex.from_tuples(zip(A,GESANcolumns)), index=GESANdates)
df_3d22.loc[:, pd.IndexSlice[:, "GESAN.IS"]] = GESAN22_3d #df_3d21 is still main for 2022---

BIOEN22a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\BIOEN22.xlsx")
BIOEN22a["Tarih"] = pd.to_datetime(BIOEN22a["Tarih"], format='%d-%m-%Y')
BIOEN22b = BIOEN22a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
BIOEN22c = BIOEN22b[["Date", "High", "Low", "Close"]]
BIOENcolumns = np.array(["BIOEN.IS"]*3)
BIOENdata = np.array(BIOEN22c[["High", "Low", "Close"]].set_index(BIOEN22b["Date"]))
BIOENdates = BIOEN22c["Date"]
BIOEN22_3d = pd.DataFrame(BIOENdata, columns=pd.MultiIndex.from_tuples(zip(A,BIOENcolumns)), index=BIOENdates)
df_3d22.loc[:, pd.IndexSlice[:, "BIOEN.IS"]] = BIOEN22_3d #df_3d21 is still main for 2022---

BASGZ22a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\BASGZ22.xlsx")
BASGZ22a["Tarih"] = pd.to_datetime(BASGZ22a["Tarih"], format='%d-%m-%Y')
BASGZ22b = BASGZ22a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
BASGZ22c = BASGZ22b[["Date", "High", "Low", "Close"]]
BASGZcolumns = np.array(["BASGZ.IS"]*3)
BASGZdata = np.array(BASGZ22c[["High", "Low", "Close"]].set_index(BASGZ22b["Date"]))
BASGZdates = BASGZ22c["Date"]
BASGZ22_3d = pd.DataFrame(BASGZdata, columns=pd.MultiIndex.from_tuples(zip(A,BASGZcolumns)), index=BASGZdates)
df_3d22.loc[:, pd.IndexSlice[:, "BASGZ.IS"]] = BASGZ22_3d #df_3d21 is still main for 2022---

ZRGYO22a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\ZRGYO22.xlsx")
ZRGYO22a["Tarih"] = pd.to_datetime(ZRGYO22a["Tarih"], format='%d-%m-%Y')
ZRGYO22b = ZRGYO22a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
ZRGYO22c = ZRGYO22b[["Date", "High", "Low", "Close"]]
ZRGYOcolumns = np.array(["ZRGYO.IS"]*3)
ZRGYOdata = np.array(ZRGYO22c[["High", "Low", "Close"]].set_index(ZRGYO22b["Date"]))
ZRGYOdates = ZRGYO22c["Date"]
ZRGYO22_3d = pd.DataFrame(ZRGYOdata, columns=pd.MultiIndex.from_tuples(zip(A,ZRGYOcolumns)), index=ZRGYOdates)
df_3d22.loc[:, pd.IndexSlice[:, "ZRGYO.IS"]] = ZRGYO22_3d #df_3d21 is still main for 2022---

PSGYO22a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\PSGYO22.xlsx")
PSGYO22a["Tarih"] = pd.to_datetime(PSGYO22a["Tarih"], format='%d-%m-%Y')
PSGYO22b = PSGYO22a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
PSGYO22c = PSGYO22b[["Date", "High", "Low", "Close"]]
PSGYOcolumns = np.array(["PSGYO.IS"]*3)
PSGYOdata = np.array(PSGYO22c[["High", "Low", "Close"]].set_index(PSGYO22b["Date"]))
PSGYOdates = PSGYO22c["Date"]
PSGYO22_3d = pd.DataFrame(PSGYOdata, columns=pd.MultiIndex.from_tuples(zip(A,PSGYOcolumns)), index=PSGYOdates)
df_3d22.loc[:, pd.IndexSlice[:, "PSGYO.IS"]] = PSGYO22_3d #df_3d21 is still main for 2022---

INVES22a = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\errors\INVES22.xlsx")
INVES22a["Tarih"] = pd.to_datetime(INVES22a["Tarih"], format='%d-%m-%Y')
INVES22b = INVES22a.rename(columns={"Tarih": "Date", "Kapanış(TL)": "Close", "Min(TL)":"Low", "Max(TL)":"High"})
INVES22c = INVES22b[["Date", "High", "Low", "Close"]]
INVEScolumns = np.array(["INVES.IS"]*3)
INVESdata = np.array(INVES22c[["High", "Low", "Close"]].set_index(INVES22b["Date"]))
INVESdates = INVES22c["Date"]
INVES22_3d = pd.DataFrame(INVESdata, columns=pd.MultiIndex.from_tuples(zip(A,INVEScolumns)), index=INVESdates)
df_3d22.loc[:, pd.IndexSlice[:, "INVES.IS"]] = INVES22_3d #df_3d21 is still main for 2022---

df_3d22.to_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\eksiklerieklenmis\df_3d22.xlsx")
df_3d22.to_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\eksiklerieklenmis\df_3d22.csv")
# end of year 22-----------
