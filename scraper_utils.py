"""
utility functions used in multiple scraper files
"""

import csv

def write_csv(header:list, rows:list, filename:str) -> None:
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)    # creating a csv writer object
        csvwriter.writerow(header)         # writing the header
        csvwriter.writerows(rows)          # writing the data rows

# site parsing
def get_soup(page_url:str) -> BeautifulSoup:
    site_response = requests.get(page_url)
    soup = BeautifulSoup(site_response.text, 'html.parser')
    return soup