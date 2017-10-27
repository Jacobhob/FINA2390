import requests, re, chardet, urllib.request, urllib.error, urllib.parse, json
from datetime import date, timedelta
from bs4 import BeautifulSoup
import sys
import csv

class newURL(object):
    def __init__(self, page, baseURL, condition):
        self.__page = page
        self.__baseURL = baseURL
        self.__condition = condition
        self.__url = baseURL + "get?page=" + str(page) + condition
    def getURL(self):
        return self.__url


if __name__ == "__main__":

    if len(sys.argv) == 1:
        baseURL = "http://dc.simuwang.com/ranking/"
        condition = "&condition=fund_type%3A1%2C6%2C4%2C3%2C8%2C2%3Bret%3A1%3Brating_year%3A1%3Bistiered%3A0%3Bcompany_type%3A1%3Bsort_name%3Aprofit_col2%3Bsort_asc%3Adesc%3Bkeyword%3A"
        pagecount = 1
        counter = 0

        header = {'User-Agent':'Mozilla/5.0'}
        req_timeout = 5

        urlList = [newURL(i, baseURL, condition).getURL() for i in range(1, pagecount + 1)]
        pages = []
        for url in urlList:
            counter += 1
            try:
                request = urllib.request.Request(url, None,header)
                response = urllib.request.urlopen(request, None, req_timeout)
                html = response.read()
                encoding_dict = chardet.detect(html)
                web_encoding = encoding_dict['encoding']
                html_1 = html if web_encoding == 'utf-8' or web_encoding == 'UTF-8' else html.decode(web_encoding).encode('utf-8')
                soup = BeautifulSoup(html_1,'lxml')
                pages.extend(json.loads(soup.get_text())["data"])
                print("Page " + str(counter) + " completed.")
            except:
                print("Error: cannot fetch data with pagecount " + str(counter))
        with open("out.json", "w") as f:
            json.dump(pages, f)
    else:
        with open(sys.argv[1]) as f:
            records = json.loads(f.read())
        headers = ["fund_short_name",
                    "company_short_name",
                    "inception_date",
                    "strategy",
                    "nav",
                    "ret_incep",
                    "ret_1m",
                    "ret_1y_a",
                    "sharperatio_incep"
                    ]
        with open("out.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for fund in records:
                try:
                    row = {i: fund[i] for i in headers}
                    writer.writerow(row)
                except Exception as e:
                    print(e)
