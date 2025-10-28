import pandas as pd
import os


def print_range(name, df):
    print(f"{name}: {df['Date'].min().date()} - {df['Date'].max().date()}  rows: {len(df)}")


def load_stock(path, name):
    df = pd.read_csv(path)
    df.drop(columns=['Low', 'High', 'Open', "Vol.", "Change %"], inplace=True, errors='ignore')
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Date'] = df['Date'].dt.to_period('M').dt.to_timestamp()
    df.rename(columns={'Price': f'Price_{name}'}, inplace=True)
    return df[['Date', f'Price_{name}']].sort_values('Date')


os.makedirs(r'F:\WORK\Python\actual work', exist_ok=True)

# S&P500
SP500 = load_stock("STOCKS/SP500.csv", "SP500")

# Consumer Sector
consumer_paths = {
    "Coke": "STOCKS/Consumer/Coke.csv",
    "Pepsi": "STOCKS/Consumer/Pepsi.csv",
    "Nike": "STOCKS/Consumer/Nike.csv",
    "PG": "STOCKS/Consumer/PG.csv"
}

Coke = load_stock(consumer_paths["Coke"], "Coke")
Pepsi = load_stock(consumer_paths["Pepsi"], "Pepsi")
Nike = load_stock(consumer_paths["Nike"], "Nike")
PG = load_stock(consumer_paths["PG"], "PG")

Consumer = pd.merge(Coke, Pepsi, on='Date', how='outer')
Consumer = pd.merge(Consumer, Nike, on='Date', how='outer')
Consumer = pd.merge(Consumer, PG, on='Date', how='outer')
Consumer.sort_values('Date', inplace=True)
Consumer.reset_index(drop=True, inplace=True)

# Energy Sector
energy_paths = {
    "Shell": "STOCKS/Energy/shell.csv",
    "Exxon": "STOCKS/Energy/Exxon.csv",
    "BP": "STOCKS/Energy/BP.csv",
    "Chevron": "STOCKS/Energy/Chevron.csv"
}

Shell = load_stock(energy_paths["Shell"], "Shell")
Exxon = load_stock(energy_paths["Exxon"], "Exxon")
BP = load_stock(energy_paths["BP"], "BP")
Chevron = load_stock(energy_paths["Chevron"], "Chevron")

Energy = pd.merge(Shell, Exxon, on='Date', how='outer')
Energy = pd.merge(Energy, BP, on='Date', how='outer')
Energy = pd.merge(Energy, Chevron, on='Date', how='outer')
Energy.sort_values('Date', inplace=True)
Energy.reset_index(drop=True, inplace=True)

# Finance Sector
finance_paths = {
    "BlackRock": "STOCKS/Finance/BlackRock.csv",
    "Goldman": "STOCKS/Finance/Goldman.csv",
    "JP": "STOCKS/Finance/JP.csv",
    "MasterCard": "STOCKS/Finance/MasterCard.csv"
}

BlackRock = load_stock(finance_paths["BlackRock"], "BlackRock")
Goldman = load_stock(finance_paths["Goldman"], "Goldman")
JP = load_stock(finance_paths["JP"], "JP")
MasterCard = load_stock(finance_paths["MasterCard"], "MasterCard")

Finance = pd.merge(BlackRock, Goldman, on='Date', how='outer')
Finance = pd.merge(Finance, JP, on='Date', how='outer')
Finance = pd.merge(Finance, MasterCard, on='Date', how='outer')
Finance.sort_values('Date', inplace=True)
Finance.reset_index(drop=True, inplace=True)

# Tech Sector
tech_paths = {
    "Apple": "STOCKS/Tech/Apple.csv",
    "Google": "STOCKS/Tech/Google.csv",
    "NVIDIA": "STOCKS/Tech/NVIDIA.csv"
}

Apple = load_stock(tech_paths["Apple"], "Apple")
Google = load_stock(tech_paths["Google"], "Google")
NVIDIA = load_stock(tech_paths["NVIDIA"], "NVIDIA")

Tech = pd.merge(Apple, Google, on='Date', how='outer')
Tech = pd.merge(Tech, NVIDIA, on='Date', how='outer')
Tech.sort_values('Date', inplace=True)
Tech.reset_index(drop=True, inplace=True)

for df in [Finance, Consumer, Energy, Tech]:
    for col in df.columns:
        if 'Price_' in col:
            df[col] = pd.to_numeric(df[col].replace({',': '', '\$': ''}, regex=True), errors='coerce')

Finance['average_finance'] = Finance[['Price_BlackRock', 'Price_Goldman', 'Price_JP', 'Price_MasterCard']].mean(axis=1)
Consumer['average_consumer'] = Consumer[['Price_Coke', 'Price_Pepsi', 'Price_Nike', 'Price_PG']].mean(axis=1)
Energy['average_energy'] = Energy[['Price_Shell', 'Price_Exxon', 'Price_BP', 'Price_Chevron']].mean(axis=1)
Tech['average_tech'] = Tech[['Price_Apple', 'Price_Google', 'Price_NVIDIA']].mean(axis=1)

Finance.to_csv("Finance_av.csv", index=False)
Consumer.to_csv("Consumer_av.csv", index=False)
Tech.to_csv("Tech_av.csv", index=False)
Energy.to_csv("Energy_av.csv", index=False)
SP500.to_csv("SP500_ready.csv", index=False)