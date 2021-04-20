# SP500_correlation
Results of correlation calculations for S&amp;P500 companies, which were included in the index on the date of 2020.12.04.

The S&P500_information_and_reportss.csv holds data that was scraped from the Financial Modeling Prep API.  
In total 8 endpoints were used.

  1.	https://financialmodelingprep.com/api/v3/income-statement/
  2.	https://financialmodelingprep.com/api/v3/balance-sheet-statement/
  3.	https://financialmodelingprep.com/api/v3/cash-flow-statement/
  4.	https://financialmodelingprep.com/api/v3/ratios/
  5.	https://financialmodelingprep.com/api/v3/financial-growth/
  6.	https://financialmodelingprep.com/api/v3/income-statement-growth/
  7.	https://financialmodelingprep.com/api/v3/key-metrics/
  8.	https://financialmodelingprep.com/api/v3/enterprise-values/

A single row holds the combined info from the 8 endpoints and also the data about the company that can be seen in the [Wikipedia page](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies ).


## annual_stock_increase
"enterprise_value.annual_stock_increase" column holds the %age by which the stock price had increased from the previously reported value.
The column is used as the main value that is compared to the other variables in the gathered data.

## Used methods
Pearsons and Spearmans correlation using pandas.  
OLS Linear Regression using statsmodel.  

## Note on results

The "correlation_all" holds the results that are based on all of the scraped info.  
The "correlation_sectors" holds the results, based on the sector in which the company operates.  
The OLS results are sorted descendingly by R_SQ (R Squared column).  
