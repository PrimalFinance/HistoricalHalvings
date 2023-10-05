import csv
import pandas as pd

pd.set_option('display.float_format', lambda x: '{:,2f}' % x)

import datetime as dt

from Scraper.cmc_scraper import CmcScraper



if __name__ == "__main__":
    cmc = CmcScraper()

    cmc.get_snapshots_by_year(2016)
    #cmc.scrape_snapshot_data(url_2023)


