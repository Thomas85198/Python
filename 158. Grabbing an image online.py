import bs4
import requests

result = requests.get(
    "https://zh.wikipedia.org/zh-tw/%E5%93%88%E5%88%A9%C2%B7%E6%B3%A2%E7%89%B9")
soup = bs4.BeautifulSoup(result.text, 'lxml')
image = soup.select("img.mw-file-element")

result = requests.get(
    "https:" + image[13]['src'])
with open("harry_image.png", "wb") as f:
    f.write(result.content)
    f.close()
