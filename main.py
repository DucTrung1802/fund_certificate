# from selenium import webdriver  # py -m pip install selenium
# import pandas as pd  # py -m pip install pandas
import requests  # py -m pip install requests
from bs4 import BeautifulSoup  # py -m pip install beautifulsoup4

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find("p", class_="location")
# print(results.prettify())
print("|{}|".format(job_elements.text.strip()))
