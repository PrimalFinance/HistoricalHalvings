# Operating system imports
import os

# Time & Date imports
import time

# Import the scraper template
import Scraper.scraper_template

# Pandas imports 
import pandas as pd

# Requests imports
import requests 

# Selenium import
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException


# Pandas imports
import pandas as pd

cwd = os.getcwd()
cpi_file_path = f"{cwd}\\CPI\\cpi.csv"
interest_rates_path = f"{cwd}\\Interest_Rates\\interest_rates.csv"



class MacroScraper(Scraper.scraper_template.ScraperTemplate):
    def __init__(self):
        self.cpi_url = "https://www.rateinflation.com/inflation-rate/usa-historical-inflation-rate/"
        self.interest_rates_url = "https://fred.stlouisfed.org/series/FEDFUNDS"
        super().__init__()

    '''-----------------------------------'''
    def update_cpi(self):
        # Get the cpi data in the form of a dataframe. 
        cpi_df = self.get_cpi()
        # Write the dataframe to the csv file.
        cpi_df.to_csv(cpi_file_path, index=False)

    '''-----------------------------------'''
    def get_cpi(self):
        '''
        Scrape the CPI data from the "CPI url". 
        '''

        if self.browser == None:
            self.create_browser(url=self.cpi_url)

        # Index should start at 1. 
        index = 1

        year_xpath = "/html/body/div/div/div[2]/main/div[3]/table/tbody/tr[{}]/td[1]"
        jan_xpath = "/html/body/div/div/div[2]/main/div[3]/table/tbody/tr[{}]/td[2]"
        feb_xpath = "/html/body/div/div/div[2]/main/div[3]/table/tbody/tr[{}]/td[3]"
        mar_xpath = "/html/body/div/div/div[2]/main/div[3]/table/tbody/tr[{}]/td[4]"
        apr_xpath = "/html/body/div/div/div[2]/main/div[3]/table/tbody/tr[{}]/td[5]"
        may_xpath = "/html/body/div/div/div[2]/main/div[3]/table/tbody/tr[{}]/td[6]"
        jun_xpath = "/html/body/div/div/div[2]/main/div[3]/table/tbody/tr[{}]/td[7]"
        jul_xpath = "/html/body/div/div/div[2]/main/div[3]/table/tbody/tr[{}]/td[8]"
        aug_xpath = "/html/body/div/div/div[2]/main/div[3]/table/tbody/tr[{}]/td[9]"
        sep_xpath = "/html/body/div/div/div[2]/main/div[3]/table/tbody/tr[{}]/td[10]"
        oct_xpath = "/html/body/div/div/div[2]/main/div[3]/table/tbody/tr[{}]/td[11]"
        nov_xpath = "/html/body/div/div/div[2]/main/div[3]/table/tbody/tr[{}]/td[12]"
        dec_xpath = "/html/body/div/div/div[2]/main/div[3]/table/tbody/tr[{}]/td[13]"
        annual_xpath = "/html/body/div/div/div[2]/main/div[3]/table/tbody/tr[{}]/td[14]"
        
        scraping_cpi = True

        cpi_data = []
        #cpi_dict = {}
        error_count = 0
        error_threshold = 3

        while scraping_cpi:

            try:
                year = self.read_data(xpath=year_xpath.format(index))
                jan_data = self.read_data(xpath=jan_xpath.format(index))
                feb_data = self.read_data(xpath=feb_xpath.format(index))
                mar_data = self.read_data(xpath=mar_xpath.format(index))
                apr_data = self.read_data(xpath=apr_xpath.format(index))
                may_data = self.read_data(xpath=may_xpath.format(index))
                jun_data = self.read_data(xpath=jun_xpath.format(index))
                jul_data = self.read_data(xpath=jul_xpath.format(index))
                aug_data = self.read_data(xpath=aug_xpath.format(index))
                sep_data = self.read_data(xpath=sep_xpath.format(index))
                oct_data = self.read_data(xpath=oct_xpath.format(index))
                nov_data = self.read_data(xpath=nov_xpath.format(index))
                dec_data = self.read_data(xpath=dec_xpath.format(index))
                annual_data = self.read_data(xpath=annual_xpath.format(index))

                # Create a list holding the data. 
                data_vars = [jan_data, feb_data, mar_data, 
                             apr_data, may_data, jun_data,
                             jul_data, aug_data, sep_data,
                             oct_data, nov_data, dec_data]

                # Create an empty dictionary to hold the cpi data for the year.
                cpi_dict = {}
                for i in range(len(data_vars)):
                    if data_vars[i].strip() == '':
                        data_vars[i] = "N\A"

                    if "%" in data_vars[i]:
                        data_vars[i] = data_vars[i].replace("%","")

                    # Assign data to the dictionary
                    month = len(data_vars) - i # Logic to determine the month. The length of "data_vars" should always be 12, so we use i to work down the list. Ex: Iter1: 12 - 0, Iter2: 12-1, Iter3: 12-2. We do this because we want the data to be stored in the dict in reverese. 
                    cpi_dict[f"{year}-{month}"] = data_vars[month-1]

                    



                """   cpi_dict = {
                    f"{year}-12": dec_data,
                    f"{year}-11": nov_data,
                    f"{year}-10": oct_data,
                    f"{year}-9": sep_data,
                    f"{year}-8": aug_data,
                    f"{year}-7": jul_data,
                    f"{year}-6": jun_data,
                    f"{year}-5": may_data,
                    f"{year}-4": apr_data,
                    f"{year}-3": mar_data,
                    f"{year}-2": feb_data,
                    f"{year}-1": jan_data,
                }"""
            except NoSuchElementException:
                error_count += 1

            if error_count == error_threshold:
                scraping_cpi = False

            cpi_data.append(cpi_dict)

            index += 1
        # Create a DataFrame
        cpi_df = pd.DataFrame([(k, v) for d in cpi_data for k, v in d.items()], columns=["Date", "CPI_val"])

        return cpi_df




    '''-----------------------------------'''
    def update_interest_rates(self):
        rates_df = self.get_interest_rates()
        # Write the dataframe to the csv file.
        rates_df.to_csv(interest_rates_path, index=False)
    '''-----------------------------------'''
    def get_interest_rates(self):

        csv_file_link = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1319&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=FEDFUNDS&scale=left&cosd=1954-07-01&coed=2023-09-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-05&revision_date=2023-10-05&nd=1954-07-01"
        csv_data = requests.get(csv_file_link)

        # Decode to a string. 
        csv_content = csv_data.content.decode('utf-8').split("\n")

        prev_year = None

        data_collected = []
        yearly_data = {}

        for c in csv_content:

            if c == "DATE,FEDFUNDS" or c == "":
                pass
            else:
                try:
                    date, value = c.split(",")
                    year, month, day = date.split("-")
                    formatted_date = f"{year}-{int(month)}"
                    data_collected.append((formatted_date, float(value)))
                # Occurs when trying to split blank value. 
                except ValueError:
                    pass

        df = pd.DataFrame(data_collected, columns=["Date", "Rate"])
        # Convert rate column to properly display the rate. Previously {:,2f} would be displayed. Still haven't figured out why.
        df["Rate"] = df["Rate"].apply(lambda x: f'{x:.2f}')
        # Reverse the rows so the newest entries are on top. 
        df = df[::-1]
        df.reset_index(drop=True, inplace=True)
        return df
        #download_directory = f"{cwd}\\Interest_Rates\\"
        #WebDriverWait(self.browser, 10).until(EC.presence_of_file(download_directory + 'interest_rates.csv'))

    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''