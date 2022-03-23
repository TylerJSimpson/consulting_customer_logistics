#CLEAN DRAYAGE.COM WEBSCRAPE
#Python3, Pandas, Regular

#import packages
import pandas as pd
import re as re

#show more columns on .head()
pd.set_option('display.max_columns', 10)

#read csv file
data = pd.read_csv(r"C:\Users\simpsont\Downloads\output.csv", names=["Customer"], encoding="unicode_escape")

#drop null value columns to avoid errors
data.dropna(inplace = True)

#define base dataframe
df = pd.DataFrame(data, columns=["Customer"])

#define dataframe1 for email and phone extraction
df1 = pd.DataFrame(data, columns=["Customer"])

#function to find emails and add it to email column
def find_email(text):
    email = re.findall(r"[\w\.-]+@[\w\.-]+",str(text))
    return ",".join(email)
df1["Email"]=df["Customer"].apply(lambda x: find_email(x))

#function to find phone numbers and add it to phone column
def find_phone(text):
    phone = re.findall(r"[\d]{3}-[\d]{3}-[\d]{4}",str(text))
    return ",".join(phone)
df1["Phone"]=df["Customer"].apply(lambda x: find_phone(x))

#function to find hazmat status and add it to the hazmat column
def find_hazmat(text):
    hazmat = re.findall(r"\wmat=\b(\w*)",str(text))
    return ",".join(hazmat)
df1["Hazmat"]=df["Customer"].apply(lambda x: find_hazmat(x))

#drop first column leaving only phone and email
df1 = df1.iloc[: ,1:]

print(df1.head(10))

#define dataframe 2 out of 2
df2 = df["Customer"].str.split("\n", n=70, expand=True)

#drop column 1 "COMPANY DETAIL" text
df2 = df2.iloc[: , 1:]

#rename column as "Company"
df2.rename(columns={df2.columns[0]: "Company"}, inplace=True)

#create a "Port Serviced" column -- each extraction will need to be renamed
df2.insert(0, "Port Serviced", "Savannah")

print(df2)


