import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_gdp_data():
    WIKI_URL = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

    response = requests.get(WIKI_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table with the data (assuming it's the first table)
    table = soup.find_all('table')[0] 

    # Parse table data and convert it to dataframe
    df = pd.read_html(str(table))[0]

    # Clean the data (e.g., remove rows with missing values)
    df = df.dropna()

    return df

def main():
    df = get_gdp_data()
    df.to_csv('gdp_data.csv', index=False)
    print("Data saved to gdp_data.csv")

if __name__ == "__main__":
    main()
