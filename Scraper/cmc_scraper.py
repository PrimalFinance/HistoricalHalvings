# Operating system imports
import os

# Time & Date imports
import time

# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Pandas imports
import pandas as pd


chrome_driver = "D:\\ChromeDriver\\chromedriver.exe"
""" --- Chrome driver options ---"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--disable-cookies")
#chrome_options.add_argument("--headless")

cwd = os.getcwd()
parent_dir = os.path.dirname(cwd)
csv_root_path = f"{cwd}\\CSV_Data\\"


historical_snapshots = {
    2013: {
        "Apr": [28],
        "May": [5, 12, 19, 26],
        "Jun": [2, 9, 16, 23, 30],
        "Jul": [7, 14, 21, 28],
        "Aug": [4, 11, 18, 25],
        "Sep": [1, 8, 15, 22, 29],
        "Oct": [6, 13, 20, 27],
        "Nov": [3, 10, 17, 24],
        "Dec": [1, 8, 15, 22, 29],
    },
    2014: {
        "Jan": [5, 12, 19, 26],
        "Feb": [2, 9, 16, 23],
        "Mar": [2, 9, 16, 23, 30],
        "Apr": [6, 13, 20, 27],
        "May": [4, 11, 18, 25],
        "Jun": [1, 8, 15, 22, 29],
        "Jul": [6, 13, 20, 27],
        "Aug": [3, 10, 17, 24, 31],
        "Sep": [7, 14, 21, 28],
        "Oct": [5, 12, 19, 26],
        "Nov": [2, 9, 16, 23, 30],
        "Dec": [7, 14, 21, 28],
    },
    2015: {
        "Jan": [4, 11, 18, 25],
        "Feb": [1, 8, 15, 22],
        "Mar": [1, 8, 15, 22, 29],
        "Apr": [5, 12, 19, 26],
        "May": [3, 10, 17, 24, 31],
        "Jun": [7, 14, 21, 28],
        "Jul": [5, 12, 19, 26],
        "Aug": [2, 9, 16, 23, 30],
        "Sep": [6, 13, 20, 27],
        "Oct": [4, 11, 18, 25],
        "Nov": [1, 8, 15, 22, 29],
        "Dec": [6, 13, 20, 27],
    },
    2016: {
        "Jan": [3, 10, 17, 24, 31],
        "Feb": [7, 14, 21, 28],
        "Mar": [6, 13, 20, 27],
        "Apr": [3, 10, 17, 24],
        "May": [1, 8, 15, 22, 29],
        "Jun": [5, 12, 19, 26],
        "Jul": [3, 10, 17, 24, 31],
        "Aug": [7, 14, 21, 28],
        "Sep": [4, 11, 18, 25],
        "Oct": [2, 9, 16, 23, 30],
        "Nov": [6, 13, 20, 27],
        "Dec": [4, 11, 18, 25],
    },
    2017: {
        "Jan": [1, 8, 15, 22, 29],
        "Feb": [5, 12, 19, 26],
        "Mar": [5, 12, 19, 26],
        "Apr": [2, 9, 16, 23, 30],
        "May": [7, 14, 21, 28],
        "Jun": [4, 11, 18, 25],
        "Jul": [2, 9, 16, 23, 30],
        "Aug": [6, 13, 20, 27],
        "Sep": [3, 10, 17, 24],
        "Oct": [1, 8, 15, 22, 29],
        "Nov": [5, 12, 19, 26],
        "Dec": [3, 10, 17, 24, 31],
    }, 
    2018: {
        "Jan": [7, 14, 21, 28],
        "Feb": [4, 11, 18, 25],
        "Mar": [4, 11, 18, 25],
        "Apr": [1, 8, 15, 22, 29],
        "May": [6, 13, 20, 27],
        "Jun": [3, 10, 17, 24],
        "Jul": [1, 8, 15, 22, 29],
        "Aug": [5, 12, 19, 26],
        "Sep": [2, 9, 16, 23, 30],
        "Oct": [7, 14, 21, 28],
        "Nov": [4, 11, 18, 25],
        "Dec": [2, 9, 16, 23, 30],
    },
    2019: {
        "Jan": [6, 13, 20, 27],
        "Feb": [3, 10, 17, 24],
        "Mar": [3, 10, 17, 24, 31],
        "Apr": [7, 14, 21, 28],
        "May": [5, 12, 19, 26],
        "Jun": [2, 9, 16, 23, 30],
        "Jul": [7, 14, 21, 28],
        "Aug": [4, 11, 18, 25],
        "Sep": [1, 8, 15, 22, 29],
        "Oct": [6, 13, 20, 27],
        "Nov": [3, 10, 17, 24],
        "Dec": [1, 8, 15, 22, 29],
    },
    2020: {
        "Jan": [5, 12, 19, 26],
        "Feb": [2, 9, 16, 23],
        "Mar": [1, 8, 15, 22, 29],
        "Apr": [5, 12, 19, 26],
        "May": [3, 10, 17, 24, 31],
        "Jun": [7, 14, 21, 28],
        "Jul": [5, 12, 19, 26],
        "Aug": [2, 9, 16, 23, 30],
        "Sep": [6, 13, 20, 27],
        "Oct": [4, 11, 18, 25],
        "Nov": [1, 8, 15, 22, 29],
        "Dec": [6, 13, 20, 27],
    },
    2021: {
        "Jan": [3, 10, 17, 24, 31],
        "Feb": [7, 14, 21, 28],
        "Mar": [7, 14, 21, 28],
        "Apr": [4, 11, 18, 25],
        "May": [2, 9, 16, 23, 30],
        "Jun": [6, 13, 20, 27],
        "Jul": [4, 11, 18, 25],
        "Aug": [1, 8, 15, 22, 29],
        "Sep": [5, 12, 19, 26],
        "Oct": [3, 10, 17, 24, 31],
        "Nov": [7, 14, 21, 28],
        "Dec": [5, 12, 19, 26],
    }, 
    2022: {
        "Jan": [2, 9, 16, 23, 30],
        "Feb": [6, 13, 20, 27],
        "Mar": [6, 13, 20, 27],
        "Apr": [3, 10, 17, 24],
        "May": [1, 8, 15, 22, 29],
        "Jun": [5, 12, 19, 26],
        "Jul": [3, 10, 17, 24, 31],
        "Aug": [7, 14, 21, 28],
        "Sep": [4, 11, 18, 25],
        "Oct": [2, 9, 16, 23, 30],
        "Nov": [6, 13, 20, 27],
        "Dec": [4, 11, 18, 25],
    }, 
    2023: {
        "Jan": [1, 8, 15, 22, 29],
        "Feb": [5, 12, 19, 26],
        "Mar": [5, 12, 19, 26],
        "Apr": [2, 9, 16, 23, 30],
        "May": [7, 14, 21, 28],
        "Jun": [4, 11, 18, 25],
        "Jul": [2, 9, 16, 23, 30],
        "Aug": [6, 13, 20, 27],
        "Sep": [3, 10, 17, 24],
        "Oct": [1],
        "Nov": [],
        "Dec": [],
    }
}


month_dict = {
    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04", 
    "May": "05", 
    "Jun": "06",
    "Jul": "07",
    "Aug": "08", 
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12"
}


class CmcScraper: 
    wait_time = 5
    def __init__(self):
        self.histroical_url = "https://coinmarketcap.com/historical/{}/"
        self.browser = None
        self.cookies_rejected = False

    '''----------------------------------- Snapshot Utilities -----------------------------------'''
    '''-----------------------------------'''
    def get_snapshots_by_year(self, year: int):
        # Access the data within the year specified. Ex: ("May", [5, 12, 19, 26])
        for i in historical_snapshots[year].items():
            # Access the first element in the tuple. Ex: "May"
            month = i[0]
            # Loop through the days within the month Ex: [5, 12, 19, 26]
            for j in i[1]:
                snapshot_url = self.build_snapshot_url(year, month, j)
                snapshot_df = self.scrape_snapshot_data(url=snapshot_url)
                day = self.add_leading_zeros(j)
                # Create the csv path. Access the folder associated with the year. 
                csv_path = csv_root_path + f"{year}\\" + f"{year}_{month_dict[month]}_{day}.csv"
                self.write_to_csv(csv_path=csv_path, data=snapshot_df)
                #print(f"Snapshot: {snapshot_url}")
    '''-----------------------------------'''
    def scrape_snapshot_data(self, url: str, recursive: bool = False):
        
        # If a browser has not been created. 

        if self.browser == None:
            self.create_browser(url=url)
        else:
            self.browser.get(url=url)

        name_xpath = "/html/body/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/table/tbody/tr[{}]/td[2]/div/a[2]"
        symbol_xpath = "/html/body/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/table/tbody/tr[{}]/td[3]"
        marketcap_xpath = "/html/body/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/table/tbody/tr[{}]/td[4]"
        price_xpath = "/html/body/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/table/tbody/tr[{}]/td[5]"
        supply_xpath = "/html/body/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/table/tbody/tr[{}]/td[6]"
        load_more_xpath = "/html/body/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/button"
        reject_cookies_xpath = "/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/button[2]"

        scraping = True
        rejected_cookies = False
        # Index should start at 1.
        index = 1
        error_count = 0
        error_threshold = 3
        # List to hold the tickers collected. This is used to make sure we don't get duplicate entries. 
        tickers_collected = []
        # List to hold dictionary of the data collected.
        data_collected = []

        


        #self.browser.maximize_window()
        # If the cookies have not been rejected yet. Since cookies only need to be rejected once, when we redirect to another url, we do not need to reject them again (assuming the url is accessing the same website)
        if not self.cookies_rejected:
            self.click_button(xpath=reject_cookies_xpath, wait=True)
            self.cookies_rejected = True
        #self.click_button(xpath=load_more_xpath, wait=True)
        # Get the width & height of the webpage.
        width, height = self.get_webpage_dimensions()
        print(f"Height: {height}")
        #self.scroll_page(pixel_to_scroll=5000, by_pixel=True)
        #cookies_displayed = cookies_element.is_displayed()
        cur_pixel = height
        pixel_increment = 100

        while scraping:
            try:

                name = self.read_data(name_xpath.format(index))
                if name in tickers_collected:
                    pass
                else:
                
                    symbol = self.read_data(symbol_xpath.format(index), wait=True)
                    marketcap = self.read_data(marketcap_xpath.format(index), wait=True)
                    price = self.read_data(price_xpath.format(index), wait=True)
                    supply = self.read_data(supply_xpath.format(index), wait=True)

                    tickers_collected.append(name)

                    # Clean prices to remove "$" and commas so we can convert it to float. 
                    marketcap = self.clean_number(data=marketcap, remove_comma=True)
                    price = self.clean_number(data=price, remove_comma=True)
                    supply = self.clean_number(data=supply, remove_comma=True)
                    data_collected.append({
                         "name": name,
                         "symbol": symbol,
                         "marketcap": marketcap,
                         "price": price,
                         "supply": supply.split(" ")[0] # Split the supply string, and grab the first element. Ex: 12,189,925 BTC -> 12,189,925 
                    })
            except NoSuchElementException:
                print(f"Failed Xpath: {name_xpath.format(index)}")
                error_count += 1

                    
                
          
            
            # If the error count exceeds the threshold, stop the loop. 
            if error_count >= error_threshold:
                scraping = False

            # Perform action every 50 indexes. 
            if index % 20 == 0:
                cur_pixel += pixel_increment
                self.scroll_page(pixel_to_scroll=cur_pixel, by_pixel=True)

            if index % 200 == 0:
                self.click_button(xpath=load_more_xpath, wait=True)
                time.sleep(5)

            index += 1
        df = pd.DataFrame(data_collected)
        print(f"Data: {data_collected}  Length: {len(data_collected)}")
        return df

    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''----------------------------------- Csv Utilities -----------------------------------'''
    '''-----------------------------------'''
    def write_to_csv(self, csv_path: str, data: pd.DataFrame) -> None:
        data.to_csv(csv_path, mode="w", index=False)
        print("[CSV Write] {}".format(csv_path.split('\\')[-1]))

    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''----------------------------------- Browser Utilities -----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    def read_data(self, xpath: str, wait: bool = False, _wait_time: int = wait_time, tag: str = "") -> str:
        '''
        :param xpath: Path to the web element.
        :param wait: Boolean to determine if selenium should wait until the element is located.
        :param wait_time: Integer that represents how many seconds selenium should wait, if wait is True.  
        :return: (str) Text of the element. 
        '''

        if wait:
            try:
                data = WebDriverWait(self.browser, _wait_time).until(EC.presence_of_element_located((By.XPATH, xpath))).text
            except TimeoutException:
                print(f"[Failed Xpath] {xpath}")
                if tag != "":
                    print(f"[Tag]: {tag}")
                raise NoSuchElementException("Element not found")
        else:
            data = self.browser.find_element("xpath", xpath).text
        # Return the text of the element found.
        return data
    '''-----------------------------------'''
    def click_button(self, xpath: str, wait: bool = False, _wait_time: int = wait_time, scroll: bool = False, tag: str = "") -> None:
        '''
        :param xpath: Path to the web element. 
        :param wait: Boolean to determine if selenium should wait until the element is located.
        :param wait_time: Integer that represents how many seconds selenium should wait, if wait is True.  
        :return: None. Because this function clicks the button but does not return any information about the button or any related web elements. 
        '''


        if wait:
            try:
                element = WebDriverWait(self.browser, _wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
                # If the webdriver needs to scroll before clicking the element. 
                if scroll:
                    self.browser.execute_script("arguments[0].click();", element)
                element.click()
            except TimeoutException:
                print(f"[Failed Xpath] {xpath}")
                if tag != "":
                    print(f"[Tag]: {tag}")
                raise NoSuchElementException("Element not found")
        else:
            element = self.browser.find_element("xpath", xpath)
            if scroll:
                    self.browser.execute_script("arguments[0].click();", element)
            element.click()
    '''-----------------------------------'''
    def build_snapshot_url(self, year, month, day):
        # Build the date url
        date = self.format_date(year, month, day)

        snapshot_url = self.histroical_url.format(date)
        return snapshot_url
    '''-----------------------------------'''
    def create_browser(self, url=None):
        '''
        :param url: The website to visit.
        :return: None
        '''
        service = Service(executable_path=chrome_driver)
        self.browser = webdriver.Chrome(
            service=service, options=chrome_options)
        # Default browser route
        if url == None:
            self.browser.get(url=self.sec_annual_url)
        # External browser route
        else:
            self.browser.get(url=url)
    '''-----------------------------------'''
    def scroll_page(self, pixel_to_scroll: int = 500, element_to_scroll = "", by_pixel: bool = True, by_element: bool = False) -> None:
        '''
        :param element_to_scroll: Scroll to the specified element on the webpage. 
        :returns: There is no data to return. 
        '''
        if by_pixel:
            self.browser.execute_script(f"window.scrollBy(0, {pixel_to_scroll})", "")
        
        if by_element:
            self.browser.execute_script("arguments[0].scrollIntoView(true);", element_to_scroll)
        
    '''-----------------------------------'''
    def create_element(self, xpath: str) -> webdriver.remote.webelement.WebElement:
        '''
        :param  xpath: The xpath to the element that we are creating. 
        '''
        element = self.browser.find_element("xpath", xpath)
        return element
    '''-----------------------------------'''
    def get_webpage_dimensions(self):
        '''
        Get the webpage width and height for the current url. 
        '''
        width = self.browser.execute_script("return window.outerWidth")
        height = self.browser.execute_script("return window.outerHeight")
        return width, height
    '''----------------------------------- Data Cleaning Utilities -----------------------------------'''
    '''-------------------------------'''
    def clean_number(self, data: str, remove_comma: bool = True):
        '''
        :param data: The string of data to be "cleaned". Cleaning in this instance means removing any "$" or converting numbers in accounting format such as (100,000) to -100,000

        '''
        # Remove dollar sign and leading/trailing white spaces
        if "$" in data:
            data = data.replace("$", "").strip()
        
        if "(" in data:
            # Remove parentheses and add a "-" at the beginning
            data = "-" + data.replace("(", "").replace(")", "")

        if remove_comma:
            if "," in data:
                data = data.replace(",","")
        return data
    '''-----------------------------------'''
    def format_date(self, year, month, day):
        # Get the numerical value for the month. Ex: Jan -> 01
        month_str = month_dict[month]

        # Turn day into a string. If the day is less than 10, add a leading 0. Ex: 5 -> 05
        if day < 10:
            day = str(day).zfill(2)

        return f"{year}{month_str}{day}"
    
    '''-----------------------------------'''
    def add_leading_zeros(self, num, leading_zeros: int = 1, day_threshold: int = 10) -> str:
        """
        param num: The number to make the edits to.
        param leading_zeros: The number of leading zeros in front of the number.
        param day_threshold: If the day is less than the threshold, add the leading zeros, if not skip it. 
                             This is because we want to match a date format. So 5 -> 05, but 10 should not equal 010. 
        returns: String with the leading zeros applied if the conditions are met. 
        """
        # Turn day into a string. If the day is less than 10, add a leading 0. Ex: 5 -> 05
        if num < day_threshold:
            num = str(num).zfill(leading_zeros+1)

        return num

        