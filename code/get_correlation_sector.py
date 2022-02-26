# single_secotrs
import numpy as np
import pandas as pd
df = pd.read_csv(r'./S&P500_information_and_reportss.csv')
df = df.replace({'0':np.nan, 0:np.nan})

sectors = ["Industrials", "Information Technology", "Financials", "Health Care", "Consumer Discretionary", "Consumer Staples", "Real Estate", "Materials", "Utilities", "Communication Services", "Energy"]


for sector in sectors:
    df_sector = df[df['S&P500_INFO.GICS_Sector'] == sector]
    # describe
    sector_described = df_sector["enterprise_value.annual_stock_increase"].describe()
    # Pearson
    pearson_correlatation = df_sector.corr(method="pearson")
    pearson_stock_increase = pearson_correlatation["enterprise_value.annual_stock_increase"].sort_values(ascending=False)
    # Spearman
    spearman_correlation = df_sector.corr(method="spearman")
    spearman_stock_increase = spearman_correlation["enterprise_value.annual_stock_increase"].sort_values(ascending=False)
    # combine results
    combined_df = pd.DataFrame()
    combined_df = combined_df.append([sector_described, pearson_stock_increase, spearman_stock_increase], ignore_index=True).transpose()
    combined_df.rename(columns = {0:'describe', 1:'Pearson', 2:'Spearman'}, inplace = True)
    # combined_df.to_csv(sector + ".csv")
    print(combined_df)
