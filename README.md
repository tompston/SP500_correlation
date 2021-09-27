# SP500_correlation analysis

- Results of correlation calculations for S&amp;P500 companies, which were included in the index on the date of 2020.12.04.

- The S&P500_information_and_reports.csv holds data that was scraped from the Financial Modeling Prep API.
  In total 8 API endpoints were used.

- A single row holds the combined info from the 8 endpoints and also the data about the company that can be seen in the [Wikipedia page](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).

- Average value of annual stock increase (mean) = 14%

- 1983 years are used in total for calculations

## annual_stock_increase

"enterprise_value.annual_stock_increase" column holds the percentage by which the stock price had increased from the previously reported value.
The column is used as the main value that is compared to the other variables in the gathered data. These variables include either the values that are

- mentioned in the annual reports or
- financial ratios that are derived out of values from the annual reports

## Used methods

- Pearsons correlation using pandas
- Spearmans correlation using pandas
- OLS Linear Regression using statsmodel

# Results, all sectors

## Pearsons correlation

Highest observed correlation can be seen for "stockBasedCompensationToRevenue", 19%.

## Spearmans correlation

Highest observed correlation can be seen for "enterpriseValueOverEBITDA", 36%.

## Ordinary least squares

Highest observed R Squared value can be seen for "stockBasedCompensationToRevenue", 4%.

# Conclusion

### **Increase in the stock price can hardly explain the increase of a value in financial statements or financial ratios, for the gathered data.**

## Note on results

The "correlation_all" directory holds the results that are based on all of the scraped info.  
The "correlation_sectors" directory holds the results, based on the sector in which the company operates.  
The OLS results are sorted descendingly by R_SQ (R Squared column).

## List of used endpoints

1. https://financialmodelingprep.com/api/v3/income-statement/
2. https://financialmodelingprep.com/api/v3/balance-sheet-statement/
3. https://financialmodelingprep.com/api/v3/cash-flow-statement/
4. https://financialmodelingprep.com/api/v3/ratios/
5. https://financialmodelingprep.com/api/v3/financial-growth/
6. https://financialmodelingprep.com/api/v3/income-statement-growth/
7. https://financialmodelingprep.com/api/v3/key-metrics/
8. https://financialmodelingprep.com/api/v3/enterprise-values/
