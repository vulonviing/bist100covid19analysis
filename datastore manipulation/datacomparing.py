import pandas as pd

prepared = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\datastore manipulation\new2019\BIST100_2019_indsec.csv")
preparedsorted = prepared.sort_values("HISSE").set_index('HISSE').reset_index()
datastore = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\datastore manipulation\bist2019stocksds.csv")
datastoresorted = datastore.sort_values("pay kodu").set_index('pay kodu').reset_index()
comparingwithdb = pd.concat((preparedsorted, datastoresorted), axis = 1)
comparingwithdb.to_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\datastore manipulation\comparingwithdb2019.csv")