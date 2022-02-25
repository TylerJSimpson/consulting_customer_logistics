#IN PROGRESS

#CLEAN DRAYAGE.COM WEBSCRAPE
#Python3, Pandas

#import packages
import numpy as np
import pandas as pd

#show more columns on .head()
pd.set_option('display.max_columns', 10)

#column names
col_names = ["Customer"]

#read csv file
data = pd.read_csv(r"C:\Users\simpsont\Downloads\output.csv", names=["Customer"], encoding="unicode_escape")

#print(data.head())
#set column name
# data.columns = ["1"]
#drop null value columns to avoid errors
data.dropna(inplace = True)
#print(data.head())
#new data frame splitting based on \n
df = data["Customer"].str.split("\n", n=100, expand=True)

#drop columns
df = df.iloc[: , 1:]

df.rename(columns={df.columns[0]: "Company"}, inplace=True)
df.rename(columns={df.columns[1]: "Address"}, inplace=True)
df.rename(columns={df.columns[2]: "Address Cont"}, inplace=True)
#Clean column 1
# df["Company"] = df["Company"].str.replace("Company: ", "")

df["Company"] = df["Company"].str.replace("Company: ", "")

df.insert(0, "Port Serviced", "Savannah")
df.insert(2, "Company Cont", "null")

# a_is_digit = df.A.str[0].str.isdigit()
# neither_is_digit = ~df.A.str[0].str.isdigit() & ~df.B.str[0].str.isdigit()
# mask = a_is_digit | neither_is_digit
# df['C'] = np.where(mask, df.A, df.B)

print(df.head(11))

#write cleaned to CSV
df.to_csv("cleaned_output.csv", index=False)

