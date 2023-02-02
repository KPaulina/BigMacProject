import pandas as pd
from consts import DATA_DIR, API_KEY
import os
import requests

#country codes in csv where taken from here: https://data.nasdaq.com/data/ECONOMIST-the-economist-big-mac-index/documentation


def get_country_codes() -> list[str]:
    '''
    Function created to get country codes for data.nasdaq.com
    csv has been taken from this link
    https://data.nasdaq.com/data/ECONOMIST-the-economist-big-mac-index/documentation
    :return:
    '''
    df_country_codes = pd.read_csv(os.path.join(DATA_DIR, 'economist_country_codes.csv'), sep='|')
    return df_country_codes['CODE'].to_list()


def scrape_api_for_big_mac_data(country_codes_list: list[str]) -> pd.DataFrame:
    '''
    Function created to get big mac data for all the countries from July 2021 that have values in data.nasdaq.com
    :param country_codes_list:
    :return:
    '''
    list_of_dataframes = []
    for country_code in country_codes_list:
        url = f'https://data.nasdaq.com/api/v3/datasets/ECONOMIST/BIGMAC_{country_code}?start_date=2021-07-01&end_date=2021-07-31&api_key={API_KEY}'
        res = requests.request("GET", url)
        json_data = res.json()
        column_names = json_data["dataset"]["column_names"]
        df_nasdaq = pd.json_normalize(json_data["dataset"], record_path=["data"])
        if len(column_names) != 0 and not df_nasdaq.empty:
            df_nasdaq.columns = column_names
            df_nasdaq['country_code'] = country_code
            list_of_dataframes.append(df_nasdaq)

    return pd.concat(list_of_dataframes)
