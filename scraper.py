
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    bbr_url = "https://www.basketball-reference.com/"

    # Use requests to retrieve data from a given URL
    bbreference_response = requests.get(bbr_url)  # <class 'requests.models.Response'>
    