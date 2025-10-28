import os
import pandas as pd
import matplotlib.pyplot as plt

Consumer = pd.read_csv("Consumer_av.csv")
Energy = pd.read_csv("Energy_av.csv")
Finance = pd.read_csv("Finance_av.csv")
Tech = pd.read_csv("Tech_av.csv")
SP500 = pd.read_csv("SP500_ready.csv")

for df in [Tech, Finance, Energy, Consumer, SP500]:
    for col in df.columns:
        if 'Price_' in col or 'average_' in col:
            df[col] = pd.to_numeric(df[col].replace({',': '', '\$': ''}, regex=True), errors='coerce')
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')


images_dir = "images"
os.makedirs(images_dir, exist_ok=True)
path = os.path.join(images_dir, "sectors.png")

plt.figure(figsize=(12, 6))
plt.plot(SP500['Date'], SP500['Price_SP500'], label='S&P 500', linewidth=2)
plt.plot(Consumer['Date'], Consumer['average_consumer'], label='Consumer Avg', alpha=0.8)
plt.plot(Energy['Date'], Energy['average_energy'], label='Energy Avg', alpha=0.8)
plt.plot(Finance['Date'], Finance['average_finance'], label='Finance Avg', alpha=0.8)
plt.plot(Tech['Date'], Tech['average_tech'], label='Tech Avg', alpha=0.8)
plt.title("S&P 500 vs Sector Averages")
plt.xlabel("Date")
plt.ylabel("Average Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(path, dpi=300)
plt.show()


path = os.path.join(images_dir, "Consumer_comparison")

plt.figure(figsize=(12, 6))
plt.plot(Consumer['Date'], Consumer['Price_Coke'], label='Coke')
plt.plot(Consumer['Date'], Consumer['Price_Pepsi'], label='Pepsi')
plt.plot(Consumer['Date'], Consumer['Price_Nike'], label='Nike')
plt.plot(Consumer['Date'], Consumer['Price_PG'], label='Procter & Gamble (PG)')
plt.title("Consumer Sector Comparison")
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(path, dpi=300)
plt.show()


path = os.path.join(images_dir, "Energy_comparison")

plt.figure(figsize=(12, 6))
plt.plot(Energy['Date'], Energy['Price_Shell'], label='Shell')
plt.plot(Energy['Date'], Energy['Price_Exxon'], label='Exxon')
plt.plot(Energy['Date'], Energy['Price_BP'], label='BP')
plt.plot(Energy['Date'], Energy['Price_Chevron'], label='Chevron')
plt.title("Energy Sector Comparison")
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(path, dpi=300)
plt.show()


path = os.path.join(images_dir, "Finance_comparison")

plt.figure(figsize=(12, 6))
plt.plot(Finance['Date'], Finance['Price_BlackRock'], label='BlackRock')
plt.plot(Finance['Date'], Finance['Price_Goldman'], label='Goldman Sachs')
plt.plot(Finance['Date'], Finance['Price_JP'], label='J.P. Morgan')
plt.plot(Finance['Date'], Finance['Price_MasterCard'], label='MasterCard')
plt.title("Finance Sector Comparison")
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(path, dpi=300)
plt.show()


path = os.path.join(images_dir, "Tech_comparison")

plt.figure(figsize=(12, 6))
plt.plot(Tech['Date'], Tech['Price_Apple'], label='Apple')
plt.plot(Tech['Date'], Tech['Price_Google'], label='Google')
plt.plot(Tech['Date'], Tech['Price_NVIDIA'], label='NVIDIA')
plt.title("Tech Sector Comparison")
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(path, dpi=300)
plt.show()