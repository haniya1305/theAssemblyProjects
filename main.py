import re
from urllib.request import urlopen
import mechanicalsoup
import requests
from bs4 import BeautifulSoup
import csv

# Web Scraping using Regex
# a = urlopen("http://olympus.realpython.org/profiles/aphrodite")
# html_read = a.read()        # store whatever is in website
# html = html_read.decode("utf-8")      # convert everything read into a string
# print(html)
# print("---------------------------------\n")
#
# cd = "<title.*?>.*?</title.*?>"
# data = re.search(cd, html, re.IGNORECASE)
# refined_data = data.group()
# refined_data = re.sub("<.*?>","", refined_data)
# print(refined_data)
# print("---------------------------------\n")

# Web Scraping Project to find a Job using requests, beautifulsoup

URL = "https://pythonjobs.github.io/"
page = requests.get(URL)
# print(page.text)

# Creating a soup object
soup = BeautifulSoup(page.content, "html.parser")
# print(soup)

job_list = []
pythonJobs = soup.select('div[data-tags*="python"][class="job"]')

for job in pythonJobs:
    title_element = job.find("h1")
    iGlobe = job.find("i", class_="i-globe")
    loc_element = iGlobe.parent
    iCalender = job.find("i", class_="i-calendar")
    cal_element = iCalender.parent
    iChair = job.find("i", class_="i-chair")
    chair_element = iChair.parent
    iCompany = job.find("i", class_="i-company")
    com_element = iCompany.parent
    det_element = job.find("p", class_="detail")
    details = {}
    details['Position'] = title_element.text.strip()
    details['Location'] = loc_element.text.strip()
    details['Start date'] = cal_element.text.strip()
    details['Chair'] = chair_element.text.strip()
    details['Company'] = com_element.text.strip()
    details['Detail'] = det_element.text.strip()
    job_list.append(details)
    # print()

# Printing out the data we just saved
# for i in range (len(job_list)):
#     for key, value in job_list[i].items():
#         print(key, ' : ', value)
#     print()

# Saving job_list dictionary into a csv file
filename = 'job_opportunity.csv'
with open(filename, 'w', newline='') as f:
    content = csv.DictWriter(f,['Position','Location','Start date','Chair','Company','Detail'])
    content.writeheader()
    for row in job_list:
        content.writerow(row)

# Alternate Method to select
results = soup.find(id="container")
# print(results.prettify())

job_elements = results.find_all("div", class_="job")
# for job_element in job_elements:
#     print(job_element, end="\n"*2)

python_jobs = results.find_all("h1", string=lambda text: "python" in text.lower())
print(len(python_jobs))









# # Extra Code
# # for job_element in job_elements:
# #     title_element = job_element.find("h1")
# #     # loc_element = job_element.find("span", class_="info")
# #     det_element = job_element.find("p", class_="detail")
# #     print(title_element.text.strip())
# #     # print(loc_element.text.strip())
# #     print(det_element.text.strip())
# #     print()
