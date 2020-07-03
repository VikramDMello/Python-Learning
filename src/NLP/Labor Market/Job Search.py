# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # VIK EXPLORATION: Search Engine Results
# %% [markdown]
# ### NOTES & TIPS
# 
# - Remember to set Python kernel to 3 (not later).
# - Import packag `os`, `requests`, `BeautifulSoup`, `csv`, `datetime`,es `textblob`, `wordcloud`, and `gensim`.
# - `get` works in conjunction with `requests`.
# - `BeautifulSoup` must have a particular HTML element from a webpage to work on.
#   E.g., , `class="post-content">`, and the *p* is from `<p style=...>`.
#   + Each website might have its own HTML structure; so might need different `soup.find` argument for each site being scraped.  
#     * E.g., `class_="css-53u6y8"` works for a NYTimes.com article, along with  *p* which is standard in HTML to represent a paragraph of text.
#     * E.g., `class_="repo-list"` works for GitHub search results.
#     * E.g., `li class_="b_algo"` with *a* works for Bing search result
#   + Can be tricky depending on webpage HTML structure; requires careful inspection even for different pages of same website, which might be slightly different.s    * What you see online is **not** an accurate representation of what `BeautifulSoup` sees; you must save the parsed HTML document to file and study that version..
# 
# %% [markdown]
# ### Import packages for scraping webpage contents and making sense of them

# %%
import os
import requests
from bs4 import BeautifulSoup
import html5lib
import csv 
from datetime import datetime

# %% [markdown]
# ### Set search query values from lists - this needs to be formalized

# %%
search_query_job = ['research scientist','sales manager','virologist'] # To be expanded from some source of top job titles
search_query_location = ['topeka','madison','houston','rhode island','billings'] # To be expanded from some source of top metros

# %% [markdown]
# ### Set query URLs, conduct search, parse necessary information, and save to file

# %%
with open('/Volumes/GoogleDrive/My Drive/Market Insights Library/00_Sources (needs organization)/Labor Market/Supply-Demand Dynamics/Job_Search_Results_Combined.csv','a') as csv_file: # Keep output file open at the beginning of all loops
    csv_writer = csv.writer(csv_file)

    for qj in search_query_job: # For each query's job keyword...
        for ql in search_query_location: # ...and location keyword...
            search_query = qj+" "+ql # ...form combined search query phrase
            
            # For Google:
            query_url_google = 'https://www.google.com/search?q=' + str(qj) + " jobs " + str(ql) # ...which populates query URL for search engine
            query_results_google = requests.get(query_url_google).text # Actually perform the search, resulting in unparsed HTML page object...
            query_results_parsed_google = BeautifulSoup(query_results_google, 'lxml') # ...which is parsed by BeautifulSoup for structured searching

            for result_google in query_results_parsed_google.find_all('div', attrs = {'class':'ZINbbc xpd O9g5cc uUPGi'}): # Iterate through each result...
                try:
                    result_google_title = result_google.find('div', attrs = {'class':'BNeawe vvjwJb AP7Wnd'}).text # ...looking for listing title...
                except:
                    pass
                try:
                    result_google_source = result_google.find('div', attrs = {'class':'BNeawe UPmit AP7Wnd'}).text # ...listing source...
                except:
                    pass
                try:
                    result_google_stub = result_google.find('div', attrs = {'class':'BNeawe s3v9rd AP7Wnd'}).text # ...and miscellaneous information below listing
                except:
                    pass
                
                csv_writer.writerow([datetime.today(),"Google",search_query,result_google_title,result_google_source,result_google_stub]) # Save this single result's values to file, before moving to the next result



            # For Indeed:
            query_url_indeed = 'https://www.indeed.com/jobs?q=' + str(qj) + " jobs " + str(ql)
            query_results_indeed = requests.get(query_url_indeed).text
            query_results_parsed_indeed = BeautifulSoup(query_results_indeed, 'lxml')

            for result_indeed in query_results_parsed_indeed.find_all('div', attrs = {'class':'jobsearch-SerpJobCard unifiedRow row result'}):
                try:
                    result_indeed_title = result_indeed.find('h2', attrs = {'class':'title'}).text
                    result_indeed_title = result_indeed_title.strip()
                except:
                    pass
                try:
                    result_indeed_employer = result_indeed.find('span', attrs = {'class':'company'}).text
                    result_indeed_employer =result_indeed_employer.strip()
                except:
                    pass
                try:
                    result_indeed_location = result_indeed.find('span', attrs = {'class':'location accessible-contrast-color-location'}).text
                    result_indeed_location = result_indeed_location.strip()
                except:
                    result_indeed_location=""
                try:
                    result_indeed_summary = result_indeed.find('li').text
                    result_indeed_summary = result_indeed_summary.strip()
                except:
                    pass
                try:
                    result_indeed_postingdate = result_indeed.find('span', attrs = {'class':'date'}).text
                    result_indeed_postingdate = result_indeed_postingdate.strip()
                except:
                    pass

                csv_writer.writerow([datetime.today(),"Indeed",search_query,result_indeed_title,"","",result_indeed_employer,result_indeed_location,result_indeed_summary,result_indeed_postingdate])

