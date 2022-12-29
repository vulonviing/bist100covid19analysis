import pandas as pd
import numpy as np

pd = pd.read_excel(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\datastore manipulation\datastoresource\exsrk2019.xlsx")



bist2022stocks1c = pd[pd["1ceyrek"] == "XU100"]
bist2022stocks2c = pd[pd["2ceyrek"] == "XU100"]
bist2022stocks3c = pd[pd["3ceyrek"] == "XU100"]
bist2022stocks4c = pd[pd["4ceyrek"] == "XU100"]
#bist2022stocks5c = pd[pd["5ceyrek"] == "XU100"]
b = bist2022stocks3c.merge(bist2022stocks4c, how="outer")
a = bist2022stocks1c.merge(bist2022stocks2c, how="outer")
#c = b.merge(bist2022stocks5c, how="outer")
bist2022stocksds = a.merge(b, how="outer")

bist2022stocksds.to_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\datastore manipulation\bist2019stocksds.csv")

print(a)