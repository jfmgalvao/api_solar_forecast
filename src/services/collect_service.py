from os.path import join

import pandas as pd
from dotenv import dotenv_values

from src.helpers.util import get_config_key
from src.settings import PROJECT_ROOT

env = dotenv_values(join(PROJECT_ROOT[:-3], '.env'))


def collect(payload, local):
    should_filter_day_period = get_config_key('should_filter_day_period')
    should_filter_zeroes = get_config_key('should_filter_zeroes')
    years = range(payload.start_year, payload.end_year + 1)
    leap_year = 'false'
    interval = '60'
    utc = 'false'

    df_from_each_year = (pd.read_csv(
        f'https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-download.csv?wkt=POINT({local.longitude}%20{local.latitude})&names={year}&leap_day={leap_year}&interval={interval}&utc={utc}&full_name={env["your_name"]}&email={env["your_email"]}&affiliation={env["your_affiliation"]}&mailing_list={env["mailing_list"]}&reason={env["reason_for_use"]}&api_key={env["api_key_nrel"]}',
        skiprows=2)
        for year in years)
    concatenated_df = pd.concat(df_from_each_year, ignore_index=True)
    concatenated_df['date'] = pd.date_range('1/1/{yr}'.format(yr=payload.start_year), freq=interval + 'Min',
                                            periods=(525600 * len(years)) / int(interval))
    concatenated_df.set_index('date', inplace=True)
    concatenated_df.drop(['Year', 'Month', 'Day', 'Hour', 'Minute'], inplace=True, axis=1)
    bkp_df = concatenated_df.copy()
    if should_filter_day_period:
        concatenated_df = concatenated_df.between_time('06:00', '17:00')
    elif should_filter_zeroes:
        concatenated_df = concatenated_df[concatenated_df['GHI'] != 0]

    df_group_days = concatenated_df.groupby([concatenated_df.index.year, concatenated_df.index.date]).mean()
    df_group_days.index = df_group_days.index.droplevel(0).rename('date')

    return df_group_days
