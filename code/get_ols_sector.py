# get_sector
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats
import seaborn as sns

df = pd.read_csv(r'./S&P500_information_and_reportss.csv')
df = df.replace({'0': np.nan, 0: np.nan})

sectors = ["Industrials", "Information Technology", "Financials", "Health Care", "Consumer Discretionary",
           "Consumer Staples", "Real Estate", "Materials", "Utilities", "Communication Services", "Energy"]

for sector in sectors:
    df_sector = df[df['S&P500_INFO.GICS_Sector'] == sector]

    df_all = pd.DataFrame()

    for financial_variable in df.columns:
        if df_sector[financial_variable].dtype == "float64" and financial_variable != "enterprise_value.annual_stock_increase":
            # get 2 variables into a single df, remove a row if observation empty
            current_columns = df_sector[[
                "enterprise_value.annual_stock_increase", financial_variable]].dropna()

            Q1 = current_columns.quantile(q=.25)
            Q3 = current_columns.quantile(q=.75)
            IQR = current_columns.apply(stats.iqr)
            current_columns = current_columns[~((current_columns < (
                Q1-1.5*IQR)) | (current_columns > (Q3+1.5*IQR))).any(axis=1)]

            y = current_columns[financial_variable]
            x = current_columns["enterprise_value.annual_stock_increase"]
            # train
            if current_columns.shape[1] == 2 and current_columns.shape[0] > 20:
                x = sm.add_constant(x)
                model = sm.OLS(y, x).fit()
                res = model.summary()

                # # split results into different tables
                first_table = pd.read_html(model.summary().tables[0].as_html(), header=0, index_col=0)[0]
                second_table = pd.read_html(model.summary().tables[1].as_html(), header=0, index_col=0)[0]

                # # second_table results
                second_df = pd.DataFrame(second_table.loc["enterprise_value.annual_stock_increase"]).transpose()
                second_df.loc[:, 'dependent_variable'] = financial_variable
                # first_table results
                first_df = pd.DataFrame(first_table)
                # get r_sq
                r_squared = first_df.columns[2]
                # # get f_stat
                first_a = pd.DataFrame(first_df.loc["Method:"]).iloc[2]
                f_stat = first_a[0]

                # n_observations
                first_b = pd.DataFrame(first_df.iloc[4])
                n_observations = first_b.iloc[0][0]

                # add new values
                combined_info = second_df
                combined_info.loc[:, 'R_SQ'] = r_squared
                combined_info.loc[:, 'F_STAT'] = f_stat
                combined_info.loc[:, 'N'] = n_observations
                df_all = df_all.append(combined_info)

            else:
                print("problem for " + financial_variable)

        else:
            print("not applicable " + financial_variable)

    df_all.reset_index(drop=True, inplace=True)
    # df_all.to_csv(sector + " ols_analysis.csv")
    print(df_all)
