
import numpy as np
import pandas as pd
df = pd.read_csv(r'./S&P500_information_and_reportss.csv')
df = df.replace({'0':np.nan, 0:np.nan})

pearson_correlatation = df.corr(method="pearson")
pearson_stock_increase = pearson_correlatation["enterprise_value.annual_stock_increase"].sort_values(ascending=False)
print(pearson_stock_increase)
# # pearson_stock_increase.to_csv("end_pearson_correlation.csv")

spearman_correlation = df.corr(method="spearman")
spearman_stock_increase = spearman_correlation["enterprise_value.annual_stock_increase"].sort_values(ascending=False)
print(spearman_correlation)
# # spearman_stock_increase.to_csv("end_spearman_correlation.csv")

