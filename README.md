# sp500-sector-analysis
A Python project analyzing S&amp;P 500 sector performance using open stock market data.

It analyzes four major market sectors (**Consumer, Energy, Finance, Tech**) and comparing them to the **S&P 500 index**.  
It loads real-world financial data from **World Data Bank**, cleans and aggregates it, and produces visual comparisons using Matplotlib.

---

## 🧠 What I Learned

- Handling real-world CSV data with **Pandas**  
- Aggregating sector averages and working with time series  
- Visualizing trends and comparisons using **Matplotlib**  
- Structuring a small, reproducible analysis workflow  
- Attention to detail in data cleaning, numeric conversions, and plotting  

---

## 🌱 Personal Growth Note

This project reflects my ongoing journey in **data science and finance**.  
I started learning Python to better understand real-world financial markets, and this project represents a milestone in applying theory to practice.  

It helped me:

- Strengthen analytical and logical thinking  
- Work confidently with real datasets from reputable sources  
- Build reproducible and shareable results  

Every chart and analysis step is part of developing a **data-oriented mindset**, which I plan to carry forward into my university studies and future projects in econometrics and finance.

---

## Project Structure

The repository contains:

- `STOCKS/` — CSV data from World Data Bank  
- `images/` — Saved charts  
- Python scripts: `prepare_data.py` and `visualize_data.py`  
- `requirements.txt`  
- `README.md`

---

## ⚙️ How to Run

```bash
pip install -r requirements.txt
python prepare_data.py
python visualize_data.py

---

## All charts will be automatically generated and saved in the `images/` folder when you run `visualize_data.py`.
