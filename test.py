from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import numpy as np


def combine(year,soc):
    myurl = soc[0]+year+soc[1]
    return myurl

def see(years,soc):
    orgs=[]
    for year in years:
        myurl= combine(year,soc)
        uClient = uReq(myurl)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html,"html.parser")
        headings = page_soup.findAll("h4",{"class":"organization-card__name"})
        # print(f'{year}\n\n')
        
        for heading in headings:
            # print(soup.prettify(heading))
            orgs.append(heading.text)
            # print(orgs)
    return orgs
    # print(orgs)

def consistent(orgs):
    # uniqueOrgs = set(orgs)
    finalres=dict()
    orgsRepeat = {org:orgs.count(org) for org in orgs}
    
    for org,times in orgsRepeat.items():
        if times>1:
            finalres[org]=times
    for key,val in finalres.items():
        print(f"{key}:{val}")


if __name__ == "__main__":
    soc = ['https://summerofcode.withgoogle.com/archive/','/organizations']
    years = ['2017','2018','2019']
    orgs=see(years,soc)
    # print(orgs)
    consistent(orgs)
