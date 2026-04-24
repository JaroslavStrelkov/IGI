import pandas as pd
import kagglehub
import os

data = [
    12000, 45000, 23000, 15000, 67000, 8900, 1200, 54000, 32000, 41000,
    22000, 33000, 27000, 31000, 29000, 1500, 8000, 7600, 9100, 11000,
    14000, 17500, 21000, 26000, 30000, 35000]

countries = ["USA", "India", "Brazil", "Russia", "France", "Germany", "Italy", "Spain", "UK", "Turkey", "Argentina", "Colombia", "Poland", "Iran", 
            "Mexico", "Chile", "Canada", "Peru", "Netherlands", "Belgium", "Sweden", "Portugal", "Ukraine", "Czechia", "Romania", "Greece"]

active_cases = pd.Series(data, index=countries, name="Active Cases")

print("Страны с индексами 20–25:")
print(active_cases.iloc[20:26])

df = pd.read_csv("D:\\4_sem\\453505_STRELKOV_12\\IGI\\LR4\\Task6\\country_wise_latest.csv")

if "New cases" not in df.columns:
    df["New cases"] = df.groupby("Country")["Confirmed"].diff().fillna(0)

q95 = df["Confirmed"].quantile(0.95)
q5 = df["Confirmed"].quantile(0.05)

high_cases = df[df["Confirmed"] > q95]
low_cases = df[df["Confirmed"] < q5]

mean_high = high_cases["New cases"].mean()
mean_low = low_cases["New cases"].mean()

if mean_low != 0:
    ratio = mean_high / mean_low
else:
    ratio = float("inf")

ratio_rounded = round(ratio, 2)

print("\nОтвет:")
print(ratio_rounded)