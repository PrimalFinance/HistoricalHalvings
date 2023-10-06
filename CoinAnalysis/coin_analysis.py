# Operating system imports
import os

# Date & Time imports
import time
import datetime as dt
from dateutil.relativedelta import relativedelta

# Pandas imports
import pandas as pd




cwd = os.getcwd()

# Path to the folder with the csv data.
csv_root_path = f"{cwd}\\CSV_Data\\"

interest_rates_path = f"{cwd}\\Interest_Rates\\interest_rates.csv"
cpi_path = f"{cwd}\\CPI\\cpi.csv"



bitcoin_halvings = {
    2012: "2012-11-28",
    2016: "2016-07-09",
    2020: "2020-05-11"
}




class CoinAnalysis:
    def __init__(self, ticker: str):
        self.ticker = ticker
        # List of years a halving occured that occured. 
        self.halving_years_occured = list(bitcoin_halvings.keys())
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''----------------------------------- CSV File Handling -----------------------------------'''
    def halving_performance(self, year: int, include_BTC: bool = False, include_rates: bool = False, include_cpi: bool = False):
        '''
        :param year: The year that a halving occured. 
        :param include_BTC: Include the performance of Bitcoin to track alongside an alt-coin.
        :param interest_rates: Include interest rates during the period.
        :param include_cpi: Include inflation data (consumer-price-index).
        
        '''
        days_to_add = 100
        years_to_add = 1
        

        if year in self.halving_years_occured:
            # Get the date of the halving. 
            halving_date = bitcoin_halvings[year]
            # Get the date 100 days after the halving. 
            halving_post_x_days = self.add_days_to_date(source_date=halving_date, days_to_add=days_to_add)
            halving_post_x_year = self.add_days_to_date(source_date=halving_date, days_to_add=(years_to_add * 365))

            # Get the closest file to the havling in the year specified. 
            closest_halving_csv = self.find_file_closest_to_halving(year)

            csv_path = f"{csv_root_path}{year}\\{closest_halving_csv}"   
            # Read file into dataframe. 
            df = pd.read_csv(csv_path)
            df = self.format_dataframe(df)
            # Check if the specified ticker exists in the year. 
            ticker_data = df[df["symbol"] == self.ticker]
            if ticker_data.empty:
                print(f"[Coin Error] Coin did not exist during this halving period: {year}")
            
            else:
                display_str = f"""[{year}]  {bitcoin_halvings[year]}\n-------------------------------------\n"""
                # Get csv files closest to the dates. 
                post_x_days_csv = self.find_file_closest_to_custom_date(halving_post_x_days)
                post_x_years_csv = self.find_file_closest_to_custom_date(halving_post_x_year)
                # Create paths 
                post_x_days_csv_path = f"{csv_root_path}{post_x_days_csv.split('_')[0]}\\{post_x_days_csv}"
                post_x_years_csv_path = f"{csv_root_path}{post_x_years_csv.split('_')[0]}\\{post_x_years_csv}"
                # Read the csv files into the dataframe. 
                post_x_days_df = pd.read_csv(post_x_days_csv_path)
                post_x_years_df = pd.read_csv(post_x_years_csv_path)
                # Format the dataframes.
                post_x_days_df = self.format_dataframe(df=post_x_days_df)
                post_x_years_df = self.format_dataframe(df=post_x_years_df)

                post_x_days_ticker_data = post_x_days_df[post_x_days_df["symbol"] == self.ticker]
                post_x_years_ticker_data = post_x_years_df[post_x_years_df["symbol"] == self.ticker]


                start_price = float(ticker_data.price.values[0])
                post_x_days_price = float(post_x_days_ticker_data.price.values[0])
                post_x_years_price = float(post_x_years_ticker_data.price.values[0])
                
                


                post_x_days_perc_change = round(((post_x_days_price-start_price)/abs(start_price)) * 100, 2)
                post_x_years_perc_change = round(((post_x_years_price-start_price)/abs(start_price)) * 100, 2)

                # If the price is greater than 1, format it to have only 2 leading decimal places. For prices less than 1, any leading decimal places are acceptable. Since some coin prices can be 0.000034, for example. 
                if start_price > 1:
                    start_price = "{:,.2f}".format(start_price)
                if post_x_days_price > 1:
                    post_x_days_price = "{:,.2f}".format(post_x_days_price)
                if post_x_years_price > 1:
                    post_x_years_price = "{:,.2f}".format(post_x_years_price)

                main_coin_str = f"{self.ticker} Start: ${start_price}\nAfter {days_to_add} days: ${post_x_days_price} ({post_x_days_perc_change:,.2f}%)\nAfter {years_to_add} Year(s): ${post_x_years_price} ({post_x_years_perc_change:,.2f}%)\nMCAP Rank Start: {ticker_data.index[0]+1}\nMCAP Rank End: {post_x_years_ticker_data.index[0]+1}"

                display_str += main_coin_str

                
                # We only want this statement to activate if the ticker being examined is not already BTC. Because there is not point in comparing BTC with BTC.
                if include_BTC and self.ticker != "BTC":
                    # Collect bitcoin data from the dataframes. 
                    btc_data = df[df["symbol"] == "BTC"]
                    post_x_days_btc = post_x_days_df[post_x_days_df["symbol"] == "BTC"]
                    post_x_years_btc = post_x_years_df[post_x_years_df["symbol"] == "BTC"]
                    # Get the prices of Bitcoin from the dataframes. 
                    btc_start_price = float(btc_data.price.values[0])
                    post_x_days_btc_price = float(post_x_days_btc.price.values[0])
                    post_x_years_btc_price = float(post_x_years_btc.price.values[0])

                    post_x_days_btc_perc_change = round(((post_x_days_btc_price-btc_start_price)/abs(btc_start_price)) * 100, 2)
                    post_x_years_btc_perc_change = round(((post_x_years_btc_price-btc_start_price)/abs(btc_start_price)) * 100, 2)

                    if btc_start_price > 1:
                        btc_start_price = "{:,.2f}".format(btc_start_price)
                    if post_x_days_btc_price > 1:
                        post_x_days_btc_price = "{:,.2f}".format(post_x_days_btc_price)
                    if post_x_years_btc_price > 1:
                        post_x_years_btc_price = "{:,.2f}".format(post_x_years_btc_price)

                    btc_coin_str = f"\n\nBTC Start: ${btc_start_price}\nAfter {days_to_add} days: ${post_x_days_btc_price} ({post_x_days_btc_perc_change:,.2f}%)\nAfter {years_to_add} Year(s): {post_x_years_btc_price} ({post_x_years_btc_perc_change:,.2f}%)"

                    display_str += btc_coin_str

                print(f"{display_str}")
                


                                        







        else:
            print(f"[Halving Error] Halving did not occur in the specified year: {year}")
        




    '''-----------------------------------'''
    '''-----------------------------------'''
    '''----------------------------------- CSV File Handling -----------------------------------'''
    def find_file_closest_to_halving(self, year: int) ->str:
        '''
        :param year: The year represents the halving, and what folder to search for the csv files. 
        :returns: String that represents the name of the closest file to the halving date. 
        '''
        
        # Path to the folder for the desired year. 
        year_csv_path = f"{csv_root_path}{year}"
        files = os.listdir(year_csv_path)

        # Get all of the csv file names in the desired year. 
        csv_files = [file for file in files if file.endswith(".csv")]

        havling_date = bitcoin_halvings[year]
        halving_year_str, halving_month_str, halving_day_str = havling_date.split("-")

        halving_date_obj = dt.datetime(int(halving_year_str), int(halving_month_str), int(halving_day_str))
        closest_file = ""
        for file in csv_files:

            year_str, month_str, day_str = file.split("_")
            day_str = day_str.split(".")[0]

            year, month, day = int(year_str), int(month_str), int(day_str)
            # Create datetime object for the csv file name.
            date_obj = dt.datetime(year, month, day)
            # Calculate the difference
            time_difference = date_obj - halving_date_obj
            # Get the days difference 
            days_diff = time_difference

            # Return the first file that has a positive difference. Meaning it is the closest file to the halving date. 
            if days_diff > dt.timedelta(0):
                return file
    '''-----------------------------------'''
    def find_file_closest_to_custom_date(self, custom_date) ->str:
        '''
        :param custom_date: User custom date to determine the closest file to it. 
        :returns: String that represents the name of the closest file to the custom date. 
        '''
        if type(custom_date) == str:
            c_year, c_month, c_day = custom_date.split("-")
            custom_date = dt.datetime(int(c_year), int(c_month), int(c_day))



        # Path to the folder for the desired year. 
        year_csv_path = f"{csv_root_path}{custom_date.year}"
        files = os.listdir(year_csv_path)

        # Get all of the csv file names in the desired year. 
        csv_files = [file for file in files if file.endswith(".csv")]

        closest_file = ""
        for file in csv_files:

            year_str, month_str, day_str = file.split("_")
            day_str = day_str.split(".")[0]

            year, month, day = int(year_str), int(month_str), int(day_str)
            # Create datetime object for the csv file name.
            date_obj = dt.datetime(year, month, day)
            # Calculate the difference
            time_difference = date_obj - custom_date
            # Get the days difference 
            days_diff = time_difference

            # Return the first file that has a positive difference. Meaning it is the closest file to the halving date. 
            if days_diff > dt.timedelta(0):
                return file
    '''-----------------------------------'''
    '''----------------------------------- Date Handling -----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    def add_days_to_date(self, source_date, days_to_add: int):
        '''
        :param source_date: The original date.
        :param days_to_add: The number of days to add to the "source_date".
        '''

        # This function can accepts data types of "str" or "datetime". If it's a string, convert it to datetime. 
        if type(source_date) == str:
            source_year, source_month, source_day = source_date.split("-")
            source_date = dt.datetime(int(source_year), int(source_month), int(source_day))

        # Define a timedelta with the number of days to add.abs. 
        delta = dt.timedelta(days=days_to_add)

        # New datetime. 
        new_datetime = source_date + delta

        # Return the new datetime. 
        return new_datetime


    '''-----------------------------------'''
    def subtract_days_from_date(self, source_date, days_to_sub: int):
        '''
        :param source_date: The original date.
        :param days_to_sub: The number of days to subtract from the "source_date".
        '''

        # This function can accepts data types of "str" or "datetime". If it's a string, convert it to datetime. 
        if type(source_date) == str:
            source_year, source_month, source_day = source_date.split("-")
            source_date = dt.datetime(int(source_year), int(source_month), int(source_day))

        # Define a timedelta with the number of days to add.abs. 
        delta = dt.timedelta(days=days_to_sub)

        # New datetime. 
        new_datetime = source_date - delta

        # Return the new datetime. 
        return new_datetime
    '''-----------------------------------'''
    def add_months_to_date(self, source_date, months_to_add: int):
        '''
        :param source_date: The original date.
        :param months_to_add: The number of months to add to the "source_date".
        '''

        # This function can accepts data types of "str" or "datetime". If it's a string, convert it to datetime. 
        if type(source_date) == str:
            source_year, source_month, source_day = source_date.split("-")
            source_date = dt.datetime(int(source_year), int(source_month), int(source_day))

        # New datetime. 
        new_datetime = source_date + relativedelta(months=months_to_add)

        # Return the new datetime. 
        return new_datetime
    '''-----------------------------------'''
    def subtract_months_from_date(self, source_date, months_to_sub: int):
        '''
        :param source_date: The original date.
        :param months_to_sub: The number of months to subtract from the "source_date".
        '''

        # This function can accepts data types of "str" or "datetime". If it's a string, convert it to datetime. 
        if type(source_date) == str:
            source_year, source_month, source_day = source_date.split("-")
            source_date = dt.datetime(int(source_year), int(source_month), int(source_day))

        # New datetime. 
        new_datetime = source_date - relativedelta(months=months_to_sub)

        # Return the new datetime. 
        return new_datetime
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''----------------------------------- General Utilities -----------------------------------'''
    '''-----------------------------------'''
    def format_dataframe(self, df: pd.DataFrame):
        '''
        param df: Dataframe to format rows to be properly displayed. 
        
        Description: Sometimes when data is read from a csv file into a dataframe, it dipslays "{:,2f} instead of the float.
                     This function will correct this issue. 
        '''
        df["marketcap"] = df["marketcap"].apply(lambda x: f'{x:.2f}')
        df["price"] = df["price"].apply(lambda x: f'{x:.2f}')
        return df
    '''-----------------------------------'''