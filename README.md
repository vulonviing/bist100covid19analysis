# project B
big data analyzing about sectoral based BIST100 stocks correlation with Covid-19, maded for TUBITAK. **all using Python and it's libraries.** <br />

BIST100 divided into three as pre-pandemic, pandemic and post-pandemic named new normal.<br /> so, with this method, we're analyzing years like: <br />
2019-2020 pre-pandemic,<br />
2020-2021 pandemic,<br />
2021-2022 new normal.<br />

## libraries & sources
| library | function | 
| ------ | ------ |
| [pandas](https://github.com/pandas-dev/pandas "pandas") | data building |
| [numpy](https://github.com/numpy/numpy "numpy") | data building |
| [yfinance](https://github.com/ranaroussi/yfinance "yfinance") | data collecting |
| [matplotlib](https://github.com/matplotlib/matplotlib "matplotlib") | data visualization |
| [seaborn](https://github.com/mwaskom/seaborn "seaborn") | data visualization |
| [pingouin](https://github.com/raphaelvallat/pingouin "pingouin") | hypotesis testing |
| [empiricaldist](https://github.com/AllenDowney/empiricaldist "empiricaldist") | hypotesis testing |

[yahoo finance](https://finance.yahoo.com/ "yahoo finance") and [DataStore](https://datastore.borsaistanbul.com/ "DataStore") from Borsa Istanbul

## data collecting & building

data, were collected in 2 steps for accuarcy. first step is getting data from DataStore and second step is verifying on KAP (public disclosure platform). this method was used for every divide of data.

data builded with pandas on multi-indexing methods. [here is](https://medium.com/@emrecanulu/pandas-multiindex-kullan%C4%B1m%C4%B1-ve-3d-veri-seti-olu%C5%9Fturma-e264ebc6a07 "here is") some information about multi-indexing. multi-indexing, or **3d data building**, helped us a lot for easily taking every data for analysis.

and covid data taken from [owid](https://ourworldindata.org/ "owid") data. **owid is totally trustable source about covid and the platform is supported by Oxford.**

also all data about stocks are divided their **sectors and industries with categorizing**, this categorizing based on yahoo database and taken with yfinance library.

## time series analysis

we are using **seaborn and matplotlib for all graphical analysis.** every line in graph has their own unique name and color, they are gived on graphs. **for easy analyzing we created some visualization functions**, you can see what function do and how can you use detailed under functions for time series analysis section. also you will able to see example graphs when i add.

**all data divided yearly 10 part for more significant visualizations.** every part has 10 stocks. of course we can see 100 stocks on one time series visualization but it is not readible on logarithmic style.

we splitted every stock by VWMP  (volume weighted market price) prices first day of quarter. **method is splitting stocks by their VWMP values on the first day of each quarter, and then sorting them in descending order.** here is example:<br />

let's take quarter 1 of year 19, first trading day is 2019-02-01.<br />
| date | stock code | VWMP price | 
| ------ | ------ | ------ |
| 2019-02-01 | IHLAS.E | 0.317 |
| 2019-02-01 | METRO.E | 0.769 |
| 2019-02-01 | TSKB.E | 0.788 |
| 2019-02-01 | GSDHO.E | 0.792 |
| 2019-02-01 | CEMAS.E | 0.822 |
| 2019-02-01 | HURGZ.E | 0.913 |
| 2019-02-01 | DOHOL.E | 1.002 |
| 2019-02-01 | ISGYO.E | 1.050 |
| 2019-02-01 | IHLGM.E | 1.057 |
| 2019-02-01 | SKBNK.E | 1.075 |

when we sorted VWMP values, here is first 10 stocks, so here is part 1 for quarter 1 of year 19. we have 10 part like that.

### what is VWMP?

**volume wweighted market price (VWMP) is a measure of the average price of a security, weighted by the volume of shares traded at each price.** it gives more weight to trades that occurred at higher volumes and reflects the overall sentiment of the market for that security.

the formula for VWMP is:<br />
**VWMP = (sum of (price x volume)) / (sum of volume)**<br />
Where:<br />
price is the price of each trade<br />
volume is the number of shares traded in that trade<br />
the sum of (price x volume) is the total value of all shares traded at each price<br />
the sum of volume is the total number of shares traded for the day.<br />

### functions for time series analysis

you can choose variables gived with table on functions if it is avaliable. table doesn't mean like you can choose only highest price with new cases, you can make whatever variable combination you want.

| PRICES | COVID |
| ------ | ------ |
| 'HIGHEST PRICE' | "NEW CASES" |
| 'LOWEST PRICE' | "TOTAL CASES" |
| 'OPENING PRICE' | "TOTAL VACCINATIONS" |
| 'CLOSING PRICE' | "NEW VACCINATIONS" |
| 'CHANGE TO PREVIOUS CLOSING (%)' | "TOTAL DEATHS" |
| 'REMAINING BID' | "NEW DEATHS" |
| 'REMAINING ASK' | "TOTAL CASES PER MILLION" |
| 'VWAP' | "NEW CASES PER MILLION" |
| 'TOTAL TRADED VALUE' | ------ |
| 'TOTAL TRADED VOLUME' | ------ |

**--)ortalamaparthepsi(): it gives all parts for choosen year and quarter.**<br />
year, 'quarter', 'listed value', 'covid','NEW CASES'<br />
example if you don't need covid : 22, 'q2', 'HIGHEST PRICE'<br />
example if you need covid : 22, 'q2', 'HIGHEST PRICE', 'random', 'NEW CASES'<br />
covid closed by default, HIGHEST PRICE is default<br />
NEW CASES is default if you'll open covid<br />

**--)ortalamapart(): it gives choosen part on choosen year and quarter.**<br />
year, 'quarter', 'part', 'listed value', 'error','covid','NEW CASES'<br />
if you need error just change error variable to str like error='something', error is always std<br />
example if you don't need covid: 22, 'q2', 'p1', 'HIGHEST PRICE'<br />
example if you need covid : 22, 'q2', 'p1', HIGHEST PRICE', 'random', 'NEW CASES'<br />
error and covid closed by default, HIGHEST PRICE is default<br />
NEW CASES is default if you'll open covid<br />

**--)ortalamapartyearly(): it gives choosen part on choosen year for all quarters.**<br />
year, 'part', 'error','covid','NEW CASES'<br />
if you need error just change error variable to str like error='something', error is always std<br />
example if you don't need covid: 22, 'p2', 'HIGHEST PRICE'<br />
example if you need covid : 22, 'p2', 'HIGHEST PRICE', 'random', 'NEW CASES'<br />
error and covid closed by default, HIGHEST PRICE is default<br />
NEW CASES is default if you'll open covid<br />

**--)part(): it gives choosen stocks of choosen part for choosen year and quarter.**<br />
SKBNK.E = loc1<br />
ODAS.E = loc2<br />
TSKB.E = loc3<br />
ZOREN.E = loc4<br />
ALBRK.E = loc5<br />
GLYHO.E = loc6<br />
EKGYO.E = loc7<br />
IZMDC.E = loc8<br />
ZRGYO.E = loc9<br />
ISGYO.E = loc10<br />
use shematic for determinating:<br />
'QUARTER''WHICHPART'_'WHICHYEAR'<br />
example: q4part4_21<br />
you can locate texts with using givenlocinfo = -+value<br />
it is listed to HIGHEST PRICE, youcan list by with using;<br />
listedby = 'HIGHEST PRICE'<br />
listedby = 'LOWEST PRICE'<br />
listedby = 'OPENING PRICE'<br />
listedby = 'CLOSING PRICE'<br />
listedby = 'CHANGE TO PREVIOUS CLOSING (%)'<br />
listedby = 'REMAINING BID'<br />
listedby = 'REMAINING ASK'<br />
listedby = 'VWAP'<br />
listedby = 'TOTAL TRADED VALUE'<br />
listedby = 'TOTAL TRADED VOLUME'<br />
covid closed by default, HIGHEST PRICE is default<br />
if you wanna see with covid data, add these variables:<br />
NEW CASES is default if you'll open covid<br />
covid = 'QUARTERYEARcovid' example: covid='q1year22covid'<br />
for different variables: covidvar = 'NEW CASES' or like ['NEW CASES', 'NEW DEATHS']<br />

