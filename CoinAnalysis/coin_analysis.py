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
    def halving_performance(self, year: int):

        

        if year in self.halving_years_occured:
            # Get the date of the halving. 
            halving_date = bitcoin_halvings[year]
            # Get the date 100 days after the halving. 
            halving_post_100_days = self.add_days_to_date(source_date=halving_date, days_to_add=100)
            halving_post_1_year = self.add_days_to_date(source_date=halving_date, days_to_add=365)

            # Get the closest file to the havling in the year specified. 
            closest_halving_csv = self.find_file_closest_to_halving(year)

            csv_path = f"{csv_root_path}{year}\\{closest_halving_csv}"    
            # Read file into dataframe. 
            df = pd.DataFrame(closest_halving_csv)

            # Check if the specified ticker exists in the year. 
            ticker_data = df[df["symbol"] == self.ticker]

            print(f"Ticker Data: {ticker_data}")







        else:
            print(f"[Halving Error] Halving error did not occur in the specified year: {year}")
        




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
    '''-----------------------------------'''
    '''-----------------------------------'''