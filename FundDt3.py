#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 22:05:27 2017

@author: liushuhan
"""

from urllib.parse import urlencode
import urllib.request
import json
import pandas as pd
import numpy as np
import csv

base_url = "https://www.licai.com/api/v1/private/rankList"

headers = {
#            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
#            'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
            'Connection':'keep-alive',
#            'Content-Length':79,
            'Content-Type':'application/json;charset=UTF-8',
#            'Cookie':"safedog-flow-item=2EA61BA166A91E3F20A7B48CD95F2CEB; BIGipServerpool_gs_sm_nginx=1695197376.20480.0000; TS0113febd=014c43903a0d62254a9577a7ff89ecbb209d80c6165991fe8f5ef0621c7bf713d8b81a657effd207dddc2efdebb8a6e86ae55bf57f; _uab_collina=150925877987307991539616; pageReferrInSession=https%3A//www.google.com.hk/; firstEnterUrlInSession=https%3A//www.licai.com/; Qs_lvt_81890=1509258780; _jzqckmp=1; LXB_REFER=www.google.com.hk; VisitorCapacity=1; hasVisited=true; _umdata=0823A424438F76AB1A462A228033BC2E779E93C9AE268A5DE4C922AAE3A01362BAAFABB7D3A79D77CD43AD3E795C914CA802098D6ADBF66100F76A54C3FA2CF7; _jzqx=1.1509258781.1509261893.2.jzqsr=google%2Ecom%2Ehk|jzqct=/.jzqsr=licai%2Ecom|jzqct=/; mediav=%7B%22eid%22%3A%22192106%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22FQ%23UtVPYbf%3A*qX%24H%3Efv'%22%2C%22ctn%22%3A%22%22%7D; ASP.NET_SessionId=i5m5cjjg0cqfo2fwqnizybm0; _gat=1; __utmt=1; sessionid=gn3xmbblk0qm9x1v94xnpgq9da4hdit1; _ga=GA1.2.1999198489.1509258781; __utma=119783701.1999198489.1509258781.1509258781.1509261893.2; __utmb=119783701.20.10.1509261893; __utmc=119783701; __utmz=119783701.1509258781.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); Hm_lvt_c09b6af925ee0121f9617c3f09d2a088=1509258781; Hm_lpvt_c09b6af925ee0121f9617c3f09d2a088=1509266559; Qs_pv_81890=1612309258068548400%2C575734369986357570%2C907960142548209200%2C1924311749777355000%2C4419002337383226000; _jzqa=1.1669436742600093700.1509258781.1509258781.1509261893.2; _jzqc=1; _qzja=1.828124228.1509258781428.1509258781428.1509261893192.1509266114333.1509266559051..0.0.21.2; _qzjb=1.1509261893192.20.0.0.0; _qzjc=1; _qzjto=21.2.0; Hm_lvt_2e0ae38a699bc0db3f8f784ca1e310c7=1509258781; Hm_lpvt_2e0ae38a699bc0db3f8f784ca1e310c7=1509266559; _jzqb=1.20.10.1509261893.1; TS0149003d=014c43903acf6466ff3b28a6b8a5d43ec140d846d03fcbaf818ce72ab1cb6766f86e0c6781d92e771be19334edb07bc0ec0a1e052a55dcf5a0ca7c83439d9e2cda735e1f6de00658556c2242ba0c8a74538f7a9c2bb96ac03401ce60c8e530308f1c838c47",
            'Host':'www.licai.com',
            'Origin':'https://www.licai.com',
            'Referer':'https://www.licai.com/simu/paihang.html',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }


fundlist=[]
for i in range(0,100,50):
    try:
        data = {"htmlType": "paihang",
                "offset": i,
                "query": "",
                "sortName": "jz_jn",
                "sortType": -1}

        #data = urlencode(data).encode("UTF-8")
  #      print(data)
        request = urllib.request.Request("https://www.licai.com/api/v1/private/rankList", data=json.dumps(data).encode("UTF-8"), headers=headers)
        response = urllib.request.urlopen(request)
        #print(response.read())    
        fund = json.loads(response.read())
    except:
        print('cannot get data offset' + str(i))
#    print(fund.values())
    fundlist.extend(fund["result"])

print(fundlist[0].keys())
headers = ["company_abbr_name",
           "product_abbr_name",
           "establishment_date",
           "annualized_rr_since_start",
           "rr_in_single_year",
           "investment_strategy_1",
           "investment_strategy_2",
           "unit_nv"
           ]
with open("out_3.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    for fund in fundlist:
        try:
            row = {i: fund[i] for i in headers}
            writer.writerow(row)
        except Exception as e:
            print(e)
