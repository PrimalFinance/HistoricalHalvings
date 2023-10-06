import csv
import pandas as pd

pd.set_option('display.float_format', lambda x: '{:,2f}' % x)

import datetime as dt

from Scraper.cmc_scraper import CmcScraper
from CoinAnalysis.coin_analysis import CoinAnalysis
from Scraper.macro_scraper import MacroScraper



if __name__ == "__main__":
    cmc = CmcScraper()
    mac = MacroScraper()

    ca = CoinAnalysis("BTC")
    #ca.find_file_closest_to_halving(2016)
    #ca.halving_performance(2016)
    #cmc.get_snapshots_by_year(2023)
    mac.update_interest_rates()
    #cmc.scrape_snapshot_data(url_2023)


