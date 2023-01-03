import pandas as pd
from datetime import datetime as datetime
import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#-----year 2019-------
bist1001901a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.201901.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1001901 = bist1001901a[bist1001901a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1001902a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.201902.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1001902 = bist1001902a[bist1001902a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1001903a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.201903.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1001903 = bist1001903a[bist1001903a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1001904a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.201904.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1001904 = bist1001904a[bist1001904a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1001905a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.201905.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1001905 = bist1001905a[bist1001905a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1001906a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.201906.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1001906 = bist1001906a[bist1001906a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1001907a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.201907.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1001907 = bist1001907a[bist1001907a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1001908a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.201908.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1001908 = bist1001908a[bist1001908a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1001909a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.201909.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1001909 = bist1001909a[bist1001909a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1001910a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.201910.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1001910 = bist1001910a[bist1001910a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1001911a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.201911.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1001911 = bist1001911a[bist1001911a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1001912a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.201912.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1001912 = bist1001912a[bist1001912a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
q1year19a = [bist1001901, bist1001902, bist1001903]
q2year19a = [bist1001904, bist1001905, bist1001906]
q3year19a = [bist1001907, bist1001908, bist1001909]
q4year19a = [bist1001910, bist1001911, bist1001912]
q1year19 = pd.concat(q1year19a).reset_index()
q1year19["DATE"] = pd.to_datetime(q1year19['DATE'])
q2year19 = pd.concat(q2year19a).reset_index()
q2year19["DATE"] = pd.to_datetime(q2year19['DATE'])
q3year19 = pd.concat(q3year19a).reset_index()
q3year19["DATE"] = pd.to_datetime(q3year19['DATE'])
q4year19 = pd.concat(q4year19a).reset_index()
q4year19["DATE"] = pd.to_datetime(q4year19['DATE'])



#-----year 2020-------
bist1002001a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202001.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002001 = bist1002001a[bist1002001a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002002a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202002.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002002 = bist1002002a[bist1002002a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002003a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202003.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002003 = bist1002003a[bist1002003a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002004a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202004.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002004 = bist1002004a[bist1002004a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002005a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202005.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002005 = bist1002005a[bist1002005a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002006a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202006.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002006 = bist1002006a[bist1002006a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002007a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202007.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002007 = bist1002007a[bist1002007a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002008a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202008.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002008 = bist1002008a[bist1002008a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002009a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202009.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002009 = bist1002009a[bist1002009a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002010a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202010.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002010 = bist1002010a[bist1002010a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002011a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202011.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002011 = bist1002011a[bist1002011a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002012a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202012.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002012 = bist1002012a[bist1002012a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
q1year20a = [bist1002001, bist1002002, bist1002003]
q2year20a = [bist1002004, bist1002005, bist1002006]
q3year20a = [bist1002007, bist1002008, bist1002009]
q4year20a = [bist1002010, bist1002011, bist1002012]
q1year20 = pd.concat(q1year20a).reset_index()
q1year20["DATE"] = pd.to_datetime(q1year20['DATE'])
q2year20 = pd.concat(q2year20a).reset_index()
q2year20["DATE"] = pd.to_datetime(q2year20['DATE'])
q3year20 = pd.concat(q3year20a).reset_index()
q3year20["DATE"] = pd.to_datetime(q3year20['DATE'])
q4year20 = pd.concat(q4year20a).reset_index()
q4year20["DATE"] = pd.to_datetime(q4year20['DATE'])

#-----year 2021-------
bist1002101a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202101.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002101 = bist1002101a[bist1002101a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002102a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202102.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002102 = bist1002102a[bist1002102a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002103a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202103.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002103 = bist1002103a[bist1002103a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002104a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202104.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002104 = bist1002104a[bist1002104a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002105a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202105.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002105 = bist1002105a[bist1002105a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002106a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202106.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002106 = bist1002106a[bist1002106a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002107a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202107.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002107 = bist1002107a[bist1002107a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002108a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202108.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002108 = bist1002108a[bist1002108a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002109a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202109.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002109 = bist1002109a[bist1002109a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002110a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202110.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002110 = bist1002110a[bist1002110a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002111a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202111.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002111 = bist1002111a[bist1002111a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002112a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202112.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002112 = bist1002112a[bist1002112a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
q1year21a = [bist1002101, bist1002102, bist1002103]
q2year21a = [bist1002104, bist1002105, bist1002106]
q3year21a = [bist1002107, bist1002108, bist1002109]
q4year21a = [bist1002110, bist1002111, bist1002112]
q1year21 = pd.concat(q1year21a).reset_index()
q1year21["DATE"] = pd.to_datetime(q1year21['DATE'])
q2year21 = pd.concat(q2year21a).reset_index()
q2year21["DATE"] = pd.to_datetime(q2year21['DATE'])
q3year21 = pd.concat(q3year21a).reset_index()
q3year21["DATE"] = pd.to_datetime(q3year21['DATE'])
q4year21 = pd.concat(q4year21a).reset_index()
q4year21["DATE"] = pd.to_datetime(q4year21['DATE'])

#-----year 2022-------
bist1002201a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202201.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002201 = bist1002201a[bist1002201a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002202a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202202.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002202 = bist1002202a[bist1002202a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002203a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202203.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002203 = bist1002203a[bist1002203a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002204a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202204.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002204 = bist1002204a[bist1002204a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002205a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202205.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002205 = bist1002205a[bist1002205a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002206a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202206.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002206 = bist1002206a[bist1002206a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002207a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202207.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002207 = bist1002207a[bist1002207a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002208a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202208.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002208 = bist1002208a[bist1002208a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002209a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202209.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002209 = bist1002209a[bist1002209a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002210a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202210.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002210 = bist1002210a[bist1002210a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002211a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202211.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002211 = bist1002211a[bist1002211a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
bist1002212a = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\fromdatastore\PP_GUNSONUFIYATHACIM.M.202212.csv")[["TRADE DATE", "INSTRUMENT SERIES CODE", "BIST 100 INDEX", "HIGHEST PRICE", "LOWEST PRICE", "OPENING PRICE", "CLOSING PRICE", "CHANGE TO PREVIOUS CLOSING (%)", "REMAINING BID", "REMAINING ASK", "VWAP", "TOTAL TRADED VALUE", "TOTAL TRADED VOLUME"]].sort_values("TRADE DATE").rename(columns={"TRADE DATE":"DATE", "INSTRUMENT SERIES CODE":"STOCK CODE"}).set_index("DATE")
bist1002212 = bist1002212a[bist1002212a["BIST 100 INDEX"] == 1].drop(columns=['BIST 100 INDEX'])
q1year22a = [bist1002201, bist1002202, bist1002203]
q2year22a = [bist1002204, bist1002205, bist1002206]
q3year22a = [bist1002207, bist1002208, bist1002209]
q4year22a = [bist1002210, bist1002211, bist1002212]
q1year22 = pd.concat(q1year22a).reset_index()
q1year22["DATE"] = pd.to_datetime(q1year22['DATE'])
q2year22 = pd.concat(q2year22a).reset_index()
q2year22["DATE"] = pd.to_datetime(q2year22['DATE'])
q3year22 = pd.concat(q3year22a).reset_index()
q3year22["DATE"] = pd.to_datetime(q3year22['DATE'])
q4year22 = pd.concat(q4year22a).reset_index()
q4year22["DATE"] = pd.to_datetime(q4year22['DATE'])

#----covid data------
virus = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\covid data\owid-covid-data.csv")
turkiye_covid = pd.DataFrame(data = virus[virus["location"]=="Turkey"]) #taking data
tur_covid = turkiye_covid[["date","total_cases", "new_cases","total_vaccinations","new_vaccinations","total_deaths","new_deaths","total_cases_per_million","new_cases_per_million","total_deaths_per_million","new_deaths_per_million","stringency_index","gdp_per_capita"]].rename(columns={"date":"Date"}).reset_index().drop(columns="index")
tur_covid["Date"] = pd.to_datetime(tur_covid['Date'])
tur_covid = tur_covid.set_index("Date")

tur_cases = tur_covid[["total_cases"]] #cases total
tur_newcases = tur_covid[["new_cases"]] #daily new cases
tur_vac = tur_covid[["total_vaccinations"]] #vaccianations total
tur_newvac = tur_covid[["new_vaccinations"]] #daily new vaccianations
tur_deaths = tur_covid[["total_deaths"]]  # deaths total
tur_newdeaths = tur_covid[["new_deaths"]]  # daily new deaths
tur_casespermillion = tur_covid[["total_cases_per_million"]] #total cases per million
tur_newcasespermillion = tur_covid[["new_cases_per_million"]] #total daily cases per million
tur_deathspermillion = tur_covid[["total_deaths_per_million"]] #total deaths per million
tur_newdeathspermillion = tur_covid[["new_deaths_per_million"]] #total daily deaths per million
tur_strindex = tur_covid[["stringency_index"]] #stringency index
tur_gdppercapita = tur_covid[["gdp_per_capita"]] #gpd per capita

q1year19covid = tur_covid.loc[q1year19.iloc[0]["DATE"] : q1year19.iloc[-1]["DATE"]]
q2year19covid = tur_covid.loc[q2year19.iloc[0]["DATE"] : q2year19.iloc[-1]["DATE"]]
q3year19covid = tur_covid.loc[q3year19.iloc[0]["DATE"] : q3year19.iloc[-1]["DATE"]]
q4year19covid = tur_covid.loc[q4year19.iloc[0]["DATE"] : q4year19.iloc[-1]["DATE"]]
q1year20covid = tur_covid.loc[q1year20.iloc[0]["DATE"] : q1year20.iloc[-1]["DATE"]]
q2year20covid = tur_covid.loc[q2year20.iloc[0]["DATE"] : q2year20.iloc[-1]["DATE"]]
q3year20covid = tur_covid.loc[q3year20.iloc[0]["DATE"] : q3year20.iloc[-1]["DATE"]]
q4year20covid = tur_covid.loc[q4year20.iloc[0]["DATE"] : q4year20.iloc[-1]["DATE"]]
q1year21covid = tur_covid.loc[q1year21.iloc[0]["DATE"] : q1year21.iloc[-1]["DATE"]]
q2year21covid = tur_covid.loc[q2year21.iloc[0]["DATE"] : q2year21.iloc[-1]["DATE"]]
q3year21covid = tur_covid.loc[q3year21.iloc[0]["DATE"] : q3year21.iloc[-1]["DATE"]]
q4year21covid = tur_covid.loc[q4year21.iloc[0]["DATE"] : q4year21.iloc[-1]["DATE"]]
q1year22covid = tur_covid.loc[q1year22.iloc[0]["DATE"] : q1year22.iloc[-1]["DATE"]]
q2year22covid = tur_covid.loc[q2year22.iloc[0]["DATE"] : q2year22.iloc[-1]["DATE"]]
q3year22covid = tur_covid.loc[q3year22.iloc[0]["DATE"] : q3year22.iloc[-1]["DATE"]]
q4year22covid = tur_covid.loc[q4year22.iloc[0]["DATE"] : q4year22.iloc[-1]["DATE"]]


dfm = q2year20covid[["new_cases"]].reset_index().melt('Date', var_name='var', value_name='cases').rename(columns={"Date":"DATE"})

print(q2year20)

#----ANAWLIZ Q1-------------------------------------------------------------------------------------------

#year19***
q1part1_19Hm = q1year19.sort_values(by=['DATE', 'HIGHEST PRICE', "STOCK CODE"]).iloc[:100].iloc[0:10][["STOCK CODE"]].reset_index(drop=True)
q1part1_19H = q1year19.merge(q1part1_19Hm, on="STOCK CODE").sort_values("DATE")
q1part1_19H["PART INFO"] = "Part 1"
q1part2_19Hm = q1year19.sort_values(by=['DATE', 'HIGHEST PRICE', "STOCK CODE"]).iloc[:100].iloc[10:20]["STOCK CODE"].reset_index(drop=True)
q1part2_19H = q1year19.merge(q1part2_19Hm, on="STOCK CODE").sort_values("DATE")
q1part2_19H["PART INFO"] = "Part 2"
q1part3_19Hm = q1year19.sort_values(by=['DATE', 'HIGHEST PRICE', "STOCK CODE"]).iloc[:100].iloc[20:30]["STOCK CODE"].reset_index(drop=True)
q1part3_19H = q1year19.merge(q1part3_19Hm, on="STOCK CODE").sort_values("DATE")
q1part3_19H["PART INFO"] = "Part 3"
q1part4_19Hm = q1year19.sort_values(by=['DATE', 'HIGHEST PRICE', "STOCK CODE"]).iloc[:100].iloc[30:40]["STOCK CODE"].reset_index(drop=True)
q1part4_19H = q1year19.merge(q1part4_19Hm, on="STOCK CODE").sort_values("DATE")
q1part4_19H["PART INFO"] = "Part 4"
q1part5_19Hm = q1year19.sort_values(by=['DATE', 'HIGHEST PRICE', "STOCK CODE"]).iloc[:100].iloc[40:50]["STOCK CODE"].reset_index(drop=True)
q1part5_19H = q1year19.merge(q1part5_19Hm, on="STOCK CODE").sort_values("DATE")
q1part5_19H["PART INFO"] = "Part 5"
q1part6_19Hm = q1year19.sort_values(by=['DATE', 'HIGHEST PRICE', "STOCK CODE"]).iloc[:100].iloc[50:60][["STOCK CODE"]].reset_index(drop=True)
q1part6_19H = q1year19.merge(q1part6_19Hm, on="STOCK CODE").sort_values("DATE")
q1part6_19H["PART INFO"] = "Part 6"
q1part7_19Hm = q1year19.sort_values(by=['DATE', 'HIGHEST PRICE', "STOCK CODE"]).iloc[:100].iloc[60:70]["STOCK CODE"].reset_index(drop=True)
q1part7_19H = q1year19.merge(q1part7_19Hm, on="STOCK CODE").sort_values("DATE")
q1part7_19H["PART INFO"] = "Part 7"
q1part8_19Hm = q1year19.sort_values(by=['DATE', 'HIGHEST PRICE', "STOCK CODE"]).iloc[:100].iloc[70:80]["STOCK CODE"].reset_index(drop=True)
q1part8_19H = q1year19.merge(q1part8_19Hm, on="STOCK CODE").sort_values("DATE")
q1part8_19H["PART INFO"] = "Part 8"
q1part9_19Hm = q1year19.sort_values(by=['DATE', 'HIGHEST PRICE', "STOCK CODE"]).iloc[:100].iloc[80:90]["STOCK CODE"].reset_index(drop=True)
q1part9_19H = q1year19.merge(q1part9_19Hm, on="STOCK CODE").sort_values("DATE")
q1part9_19H["PART INFO"] = "Part 9"
q1part10_19Hm = q1year19.sort_values(by=['DATE', 'HIGHEST PRICE', "STOCK CODE"]).iloc[:100].iloc[90:]["STOCK CODE"].reset_index(drop=True)
q1part10_19H = q1year19.merge(q1part10_19Hm, on="STOCK CODE").sort_values("DATE")
q1part10_19H["PART INFO"] = "Part 10"

#filtreleme yılın ilk günü baz alınarak birbirine yakın hisseleri onarlı olarak çekmeyle gerçekleştiriliyor

print(q1part1_19H)

sns.set(font_scale=1.5)
sns.set_theme(style="ticks")
ax= sns.relplot(
    data=q1year19, 
    x="DATE", y="HIGHEST PRICE", hue="STOCK CODE", 
    height=10, aspect=1.5, 
    kind="line",
    legend=False,
    marker="o",
 )#.set(title="0-10 Stocks of Q1 2019",  ylabel="Highest Price", xlabel="Date")
plt.yscale('log')
plt.savefig(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\anawliz\q1\part_19HALL", bbox_inches="tight")


renklerq1part1_19H = {
           q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[0]["STOCK CODE"]:'#e6194B', 
           q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[1]["STOCK CODE"]:'#3cb44b', 
           q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[2]["STOCK CODE"]:'#800000', 
           q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[3]["STOCK CODE"]:'#4363d8', 
           q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[4]["STOCK CODE"]:'#f58231', 
           q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[5]["STOCK CODE"]:'#42d4f4', 
           q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[6]["STOCK CODE"]:'#f032e6', 
           q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[7]["STOCK CODE"]:'#9A6324', 
           q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[8]["STOCK CODE"]:'#469990', 
           q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[9]["STOCK CODE"]:'#911eb4'
           } #colors
sns.set(font_scale=1.5)
sns.set_style("ticks")
sns.relplot(
    data=q1part1_19H, 
    x="DATE", y="HIGHEST PRICE", hue="STOCK CODE", 
    height=10, aspect=1.5, 
    kind="line",
    legend=False,
    marker="o",
    linewidth = 1.5,
    palette=renklerq1part1_19H
).set(title=str(q1part1_19H["PART INFO"].head(1).values[0]) + " Stocks of Q1 " + str(q1part1_19H["DATE"].head(1).dt.strftime("%Y").values[0]),  ylabel="Highest Price", xlabel="Date")
plt.yscale('log')
plt.text(q1part1_19H.iloc[-1]["DATE"] + datetime.timedelta(days=1),q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[0]["HIGHEST PRICE"],q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[0]["STOCK CODE"], c=list(renklerq1part1_19H.values())[0], fontsize=13)
plt.text(q1part1_19H.iloc[-1]["DATE"] + datetime.timedelta(days=1),q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[1]["HIGHEST PRICE"]- 0.017,q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[1]["STOCK CODE"], c=list(renklerq1part1_19H.values())[1], fontsize=13)
plt.text(q1part1_19H.iloc[-1]["DATE"] + datetime.timedelta(days=1),q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[2]["HIGHEST PRICE"],q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[2]["STOCK CODE"], c=list(renklerq1part1_19H.values())[2], fontsize=13)
plt.text(q1part1_19H.iloc[-1]["DATE"] + datetime.timedelta(days=1),q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[3]["HIGHEST PRICE"]+ 0.022,q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[3]["STOCK CODE"], c=list(renklerq1part1_19H.values())[3], fontsize=13)
plt.text(q1part1_19H.iloc[-1]["DATE"] + datetime.timedelta(days=1),q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[4]["HIGHEST PRICE"],q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[4]["STOCK CODE"], c=list(renklerq1part1_19H.values())[4], fontsize=13)
plt.text(q1part1_19H.iloc[-1]["DATE"] + datetime.timedelta(days=1),q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[5]["HIGHEST PRICE"],q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[5]["STOCK CODE"], c=list(renklerq1part1_19H.values())[5], fontsize=13)
plt.text(q1part1_19H.iloc[-1]["DATE"] + datetime.timedelta(days=1),q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[6]["HIGHEST PRICE"] - 0.027,q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[6]["STOCK CODE"], c=list(renklerq1part1_19H.values())[6], fontsize=13)
plt.text(q1part1_19H.iloc[-1]["DATE"] + datetime.timedelta(days=1),q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[7]["HIGHEST PRICE"],q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[7]["STOCK CODE"], c=list(renklerq1part1_19H.values())[7], fontsize=13)
plt.text(q1part1_19H.iloc[-1]["DATE"] + datetime.timedelta(days=1),q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[8]["HIGHEST PRICE"],q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[8]["STOCK CODE"], c=list(renklerq1part1_19H.values())[8], fontsize=13)
plt.text(q1part1_19H.iloc[-1]["DATE"] + datetime.timedelta(days=1),q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[9]["HIGHEST PRICE"],q1part1_19H.set_index("DATE").loc[q1part1_19H.iloc[-1]["DATE"]].sort_values("HIGHEST PRICE").iloc[9]["STOCK CODE"], c=list(renklerq1part1_19H.values())[9], fontsize=13)
plt.savefig(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\stockrates\anawliz\q1\q1part1_19H2", bbox_inches="tight")


