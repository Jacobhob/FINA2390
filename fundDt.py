import requests, re, chardet, urllib2, json
from datetime import date, timedelta
from bs4 import BeautifulSoup


class newURL(object):
    def __init__(self, page, baseURL, condition):
        self.__page = page
        self.__baseURL = baseURL
        self.__condition = condition
        self.__url = baseURL + "get?page=" + str(page) + condition
    def getURL(self):
        return self.__url

if __name__ == "__main__":

    baseURL = "http://dc.simuwang.com/ranking/"
    condition = "&condition=fund_type%3A1%2C6%2C4%2C3%2C8%2C2%3Bret%3A1%3Brating_year%3A1%3Bistiered%3A0%3Bcompany_type%3A1%3Bsort_name%3Aprofit_col2%3Bsort_asc%3Adesc%3Bkeyword%3A"
    pagecount = 174
    counter = 0

    header = {'User-Agent':'Mozilla/5.0'}
    req_timeout = 5

    f = open("out.txt","w+")
    #change this file to ultimate .csv file

    urlList = [newURL(i, baseURL, condition).getURL() for i in range(1, pagecount + 1)]

    for url in urlList:
        counter += 1
        try:
            request = urllib2.Request(url, None,header)
            response = urllib2.urlopen(request, None, req_timeout)
            html = response.read()
            encoding_dict = chardet.detect(html)
            web_encoding = encoding_dict['encoding']
            html_1 = html if web_encoding == 'utf-8' or web_encoding == 'UTF-8' else html.decode(web_encoding).encode('utf-8')
            soup = BeautifulSoup(html_1,'lxml')
            f.write(soup.get_text())
            print("Page " + str(counter) + " completed.")
            # You can use online JSON view to find the field names
        except:
            print("Error: cannot fetch data with pagecount " + str(counter))
    f.close()
