from bs4 import BeautifulSoup
import requests


url = 'https://mathb-ege.sdamgia.ru/test?id=19435384&nt=True&pub=False&print=true'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
qeustion = soup.find_all("p", class_="left_margin")
answer = soup.find_all("span", style="letter-spacing: 2px;")
for i in range(len(qeustion)):
    print(qeustion[i].text.replace("­", ""))
    print(answer[i].text)