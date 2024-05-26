#moneycontrol.com - news scraping
# create a dataset(data_set): some NULL values must be there in dataset, else create it thru numpy.nan 
#1 data preprocessing  DATA: bigbasket
#2 data cleaning
#3 data transformation using aggregation functions, groupby, merge, joins 
#4 data visualization , expiring soon will be bigger in scatter plot and price will be lower as comparison to when it was fresh
#5 advertisements - 2 types of advertisements - for the products which are expiring soon(lower prices) 

import requests
from bs4 import BeautifulSoup

def scrape_line(url, target_line):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')

  for line in soup.get_text().splitlines():
    if target_line in line:
      return line

# Example usage
url = "https://www.moneycontrol.com/"  
target_line = "More than 50 Uttarakhand Chardham"  
result = scrape_line(url, target_line)
print(result)
