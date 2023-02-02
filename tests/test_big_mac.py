import requests
from extract import get_country_codes, scrape_api_for_big_mac_data
import pandas as pd
import os
from consts import DATA_DIR, API_KEY


def test_get_country_codes():
    df_country_codes = pd.read_csv(os.path.join(DATA_DIR, 'economist_country_codes.csv'), sep='|')
    length = len(get_country_codes())
    column_length = df_country_codes['CODE'].str.len()
    return column_length == length


def test_check_url():
    check = []
    country_code_list = ['VNM', 'ARG', 'AUS', 'BRA', 'GBR', 'CAN', 'CHL', 'CHN', 'COL', 'CRI', 'CZE', 'DNK', 'EGY', 'EUR', 'HKG', 'HUN', 'IND', 'IDN', 'ISR', 'JPN', 'LTU', 'MYS', 'MEX', 'NZL', 'NOR', 'PAK', 'PER', 'PHL', 'POL', 'RUS', 'SAU', 'SIN', 'ZAF', 'KOR', 'LKA', 'SWE', 'CHE', 'ROC', 'THA', 'TUR', 'UAE', 'UKR', 'USA', 'URY', 'VEN', 'AUT', 'BEL', 'EST', 'FIN', 'FRA', 'DEU', 'GRC', 'IRL', 'ITA', 'NLD', 'PRT', 'ESP', 'LVA']
    for country_code in country_code_list:
        url = f'https://data.nasdaq.com/api/v3/datasets/ECONOMIST/BIGMAC_{country_code}?start_date=2021-07-01&end_date=2021-07-31&api_key={API_KEY}'
        res = requests.request("GET", url)
        if res.status_code == 200:
            check.append(True)
        else:
            check.append((False, country_code))
    assert all(check)


def test_dataframe_for_null_values_in_dollar_price():
    df = pd.read_excel(os.path.join(DATA_DIR, 'big_mac_data.xlsx'))
    test = df['dollar_price'].isnull().any()
    assert test is False

