import requests
from bs4 import BeautifulSoup

url = 'https://redaktor.az/'

response = requests.get(url)
html_content = response.text
xeberler_list =[]

soup = BeautifulSoup(html_content, 'html.parser')
link=soup.find_all("a",class_="news-i-inner")
for link_1 in link:
    link_2=link_1["href"]
    umumi_link='https://redaktor.az/'+link_2
    xeberler_list.append(umumi_link)
    response_new=requests.get(umumi_link).text
for i in xeberler_list:
    response_new_link=requests.get(i)
    soup_news=BeautifulSoup(response_new_link.text,"html.parser")
    title=soup_news.find("h1").get_text()
    content=soup_news.find("div",class_="content").get_text()

    print(title)
    print(content)