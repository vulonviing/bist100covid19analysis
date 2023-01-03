

import pandas as pd
import yfinance as yf
import xarray as xr
from datetime import datetime as datetime

df = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\datastore manipulation\new2020\BIST100_2020_indsecv2.csv").sort_values(by="HISSE")
dfstocks = df["HISSE"]
stocks = [s + ".IS" for s in dfstocks]
_start = datetime(2020,1,2)
_end   = datetime(2020,1,3)
print(stocks[98])

xarray_3d = xr.Dataset({
    stocks[0]: yf.Ticker(stocks[0]).history(start=_start, end=_end, period="1d", interval="1d")
    })

data = yf.download(stocks, start=_start, end=_end)
#data.to_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\test.xlsx")
df_3d = xarray_3d.to_dataframe()
print(df_3d)

#df_3d.to_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\2020openclosedata.csv")
