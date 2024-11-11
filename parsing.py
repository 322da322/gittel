from bs4 import BeautifulSoup
import requests, asyncio

solutins = []
answers = []
qeustions = []



async def one():
    url = 'https://mathb-ege.sdamgia.ru/test?id=19435384&nt=True&pub=False&print=true'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    qeustion = soup.find_all("div", class_="pbody")
    answer = soup.find_all("div", class_="answer")
    solution = soup.find_all("div", style="clear:both;display:none")
    for i in range(len(qeustion)):
        qeustions.append(qeustion[i].text.replace("­", ""))
        answers.append(answer[i].text)
        #solutins.append(solution.text.replace("­", ""))
    return qeustions,answers, solutins

    

