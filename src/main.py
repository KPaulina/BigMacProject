from consts import DATA_DIR
from extract import get_country_codes, scrape_api_for_big_mac_data
from load import upload_file
import os


if __name__ == "__main__":
    country_codes_list = get_country_codes()
    df_big_mac_values_for_all_countries = scrape_api_for_big_mac_data(country_codes_list)
    df_big_mac_values_for_all_countries.to_excel(os.path.join(DATA_DIR, 'big_mac_data.xlsx'), index=False)
    upload_file(os.path.join(DATA_DIR, 'big_mac_data.xlsx'), 'bucketbigmac', 'big_mac_data.xlsx')
