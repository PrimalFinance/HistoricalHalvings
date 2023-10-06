import sys


import csv
import pandas as pd



pd.set_option('display.float_format', lambda x: '{:,2f}' % x)

import datetime as dt

from Scraper.cmc_scraper import CmcScraper
from CoinAnalysis.coin_analysis import CoinAnalysis
from Scraper.macro_scraper import MacroScraper







''' ---------------------- Interest Rates ---------------------- '''
def interest_rates():
    mac = MacroScraper()
    mac.update_interest_rates()


''' ---------------------- CPI ---------------------- '''
def cpi():
    mac = MacroScraper()
    mac.update_cpi()

''' ---------------------- Historical Snapshots ---------------------- '''
def historical_snapshots(year: int):
    cmc = CmcScraper()
    cmc.get_snapshots_by_year(year)

''' ---------------------- Halving Performance ---------------------- '''
def halving_performance(ticker: str, year: int):
    ca = CoinAnalysis(ticker)
    ca.halving_performance(year, include_BTC=True)






if __name__ == "__main__":

    if len(sys.argv) > 0:
        ticker = sys.argv[1]
        year = int(sys.argv[2])
        
    else:
        ticker = "ETH"
        year = 2016
    

    halving_performance(ticker, year)
    #historical_snapshots(year)
    #interest_rates()
    #cpi()


