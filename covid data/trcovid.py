import pandas as pd
pd.set_option("display.max_rows", 9999)
pd.set_option("display.max_columns", 100)
pd.set_option("display.max_colwidth", 100)
pd.set_option("display.width", 100) #visualization configs

virus = pd.read_csv(r"C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\covid data\owid-covid-data.csv")
turkiye_covid = pd.DataFrame(data = virus[virus["location"]=="Turkey"]) #taking data
tur_covid = turkiye_covid[["date","total_cases", "new_cases","total_vaccinations","new_vaccinations","total_deaths","new_deaths","total_cases_per_million","new_cases_per_million","total_deaths_per_million","new_deaths_per_million","stringency_index","gdp_per_capita"]]

tur_cases = turkiye_covid["total_cases"] #cases total
tur_newcases = turkiye_covid["new_cases"] #daily new cases
tur_vac = turkiye_covid["total_vaccinations"] #vaccianations total
tur_newvac = turkiye_covid["new_vaccinations"] #daily new vaccianations
tur_deaths = turkiye_covid["total_deaths"]  # deaths total
tur_newdeaths = turkiye_covid["new_deaths"]  # daily new deaths
tur_casespermillion = turkiye_covid["total_cases_per_million"] #total cases per million
tur_newcasespermillion = turkiye_covid["new_cases_per_million"] #total daily cases per million
tur_deathspermillion = turkiye_covid["total_deaths_per_million"] #total deaths per million
tur_newdeathspermillion = turkiye_covid["new_deaths_per_million"] #total daily deaths per million

tur_strindex = turkiye_covid["stringency_index"] #stringency index
tur_gdppercapita = turkiye_covid["gdp_per_capita"] #gpd per capita
print(tur_covid)
tur_covid.to_csv(r'C:\Users\emrec\Desktop\TUBITAK 22 DOSYASI\covid data\tur_covid.csv')