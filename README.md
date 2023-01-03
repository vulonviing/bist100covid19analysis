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
| [xarray](https://github.com/pydata/xarray "xarray") | 3d data building |
| [yfinance](https://github.com/ranaroussi/yfinance "yfinance") | data collecting |
| [matplotlib](https://github.com/matplotlib/matplotlib "matplotlib") | data visualization |
| [seaborn](https://github.com/mwaskom/seaborn "seaborn") | data visualization |
| [pingouin](https://github.com/raphaelvallat/pingouin "pingouin") | hypotesis testing |
| [empiricaldist](https://github.com/AllenDowney/empiricaldist "empiricaldist") | hypotesis testing |

[yahoo finance](https://finance.yahoo.com/ "yahoo finance") and [DataStore](https://datastore.borsaistanbul.com/ "DataStore") from Borsa Istanbul

## data collecting & building

data, were collected in 2 steps for accuarcy. first step is getting data from DataStore and second step is verifying on KAP (public disclosure platform). this method was used for every divide of data.
