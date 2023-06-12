import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
ua = UserAgent()
headers = {"User-Agent": ua.random}
for sc in range(800,3502,100):
    test = []
    print(f"爬取{sc}中~")
    for i in range(1, 3):
        print("第"+str(i)+"面")
        url = 'https://codeforces.com/problemset/page/' + str(i) + '?tags='+str(sc)+'-'+str(sc)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        div1 = soup.find_all('a', attrs={'href': True}, href=re.compile('/problemset/problem/'))
        for a in div1:
            href = "https://codeforces.com" + a['href']
            if href not in test:
                test.append(href)
    with open(str(sc)+'.txt', 'w') as file:
        file.write('')
    f = open(str(sc)+'.txt', 'a')
    for s in test:
        f.write(s + '\n')
    f.close()
    print("爬取结束")
input("Press Any Key")
