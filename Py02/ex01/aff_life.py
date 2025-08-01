import matplotlib.pyplot as plt
import seaborn as sns
#import numpy as np
from load_csv import load

def main() :
    lifeExpCsv = load("life_expectancy_years.csv")
    if lifeExpCsv is None :
        print("Error loading dataset.")
        return

    country = "France"

    FranceLifeExp = lifeExpCsv[lifeExpCsv["country"] == country]
    if FranceLifeExp.empty:
        print(f"No data found for country: {country}")
        return

    years = FranceLifeExp.columns[1:]
    lifeExp = FranceLifeExp.iloc[0, 1:].values.astype(float)

    plt.figure(figsize=(12,6))
    sns.lineplot(x=years, y=lifeExp)
    plt.title(f"{country} Life Expectancy Projections ")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy (years)")
    plt.xticks([])
    plt.legend([country])
    plt.tight_layout()
    plt.show()
    

if __name__ == "__main__" :
    main()
