import pycountry_convert as pc
import pandas as pd


df = pd.read_csv('data/2022-04-20.csv')

def country_to_continent(country_name):
    country_continent_name = ''
    try:
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)
        country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    except Exception:
        pass
    return country_continent_name

continents = [country_to_continent(country)for country in df['Country']] 

df['Continent'] = continents

df.to_csv('data/2022-04-20(modify).csv', index=False)