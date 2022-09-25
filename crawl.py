#내장 모듈
import sys
import time
from collections import deque
import requests

#외부 모듈
from bs4 import *
import matplotlib.pyplot as p
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def extractLastPrice(webUrl, DN):
    pList = []
    for i in range(DN):
        req = requests.get(webUrl + str(i+1), headers={"User-agent":"Mozilla/5.0"})
        soup = BeautifulSoup(req.text, 'html.parser')
        trList = soup.find_all('tr', onmouseover='mouseOver(this)')
        for tr in trList:
            if tr.select('td')[0].text.strip():
                temp = tr.find_all('td')[1].text.strip()
                temp = float(temp.replace(',', ''))
                pList.append(temp)
    return pList

def makeMA (pList, numMA) :  
    q = deque(numMA*[pList[0]], maxlen=numMA)
    mList = []
    for i in range(len(pList)):
        q.append(pList[i])
        mList.append(sum(q)/numMA)
    return mList

def inputCompanyAndDays ():
    #회사 선택
    print ('1:samsung, 2:lge, 3:hynix')
    inputName = input('회사를 고르세요 : ')
    if (inputName == '1'):
        webUrl = 'https://finance.naver.com/item/frgn.nhn?code=005930&page='
        companyName = 'samsung'
    elif (inputName == '2'):
        webUrl = 'https://finance.naver.com/item/frgn.nhn?code=066570&page='
        companyName = 'lge'
    elif (inputName == '3'):
        webUrl = 'https://finance.naver.com/item/frgn.nhn?code=000660&page='
        companyName = 'hynix'
    else:
        print("잘못된 입력입니다. 프로그램을 종료합니다.")
        sys.exit()

    #추출할 종가의 날 수를 입력받는다.
    inputNumber = input ('종가 추출 기간을 입력하세요(20의 배수가 되도록 상향 조정합니다) : ')
    if (inputNumber.isdigit() and int(inputNumber) > 0) :
        days = int (inputNumber)
        if days%20:
            days += 20 - days%20
    else:
        print("잘못된 입력입니다. 프로그램을 종료합니다.")
        sys.exit()

    return companyName, webUrl, days

def drawGraph (pList):
    days = len(pList)
    #그래프의 x값 list 생성
    xAxis = list(range(-days + 1, 1)) # 100개면 -99~0개까지 x축을 만든다.

    #이동평균선 생성
    MA5List  = makeMA(pList,  5)
    MA20List = makeMA(pList, 20)
    MA60List = makeMA(pList, 60)

    #종가와 이동평균선 그리기
    p.plot (xAxis, pList,    'r', label = stockName) #종가를 그린다.
    p.plot (xAxis, MA5List,  'b', label = '5MA')     # 5일 이동평균선
    p.plot (xAxis, MA20List, 'g', label = '20MA')    # 20일 이동평균선
    p.plot (xAxis, MA60List, 'y', label = '60MA')    # 60일 이동평균선

    #그래프의 레이블 및 비주얼 효과 생성
    p.xlabel ('Day')
    p.ylabel ('Last Price')
    p.grid (True)
    p.legend(loc = 'upper left')
    p.show()

    return


"""***메인 프로그램: 주식 종가 추출 및 그리기***"""

stockName, stockAddr, days = inputCompanyAndDays() # 회사 선택

startTime = time.time()            # 현재 시각 기록

pList = extractLastPrice(stockAddr, days) # 종가 추출

exeTime = time.time() - startTime  # 경과 시간 체크
print("\n추출 완료(소요 시간 = %.2f 초)" %exeTime)

drawGraph(pList) # 그리기

""" ***The End of Main*** """

