from selenium import webdriver
from bs4 import BeautifulSoup as bs


driver = webdriver.Chrome(executable_path="chromedriver.exe")

url = "https://www.melon.com/chart/day/index.htm"

driver.get(url)
html = driver.page_source
soup = bs(html, "html.parser")


rank_list = soup.find_all("span", {"class": "rank"})
title_list = soup.find_all("div", {"class": "ellipsis rank01"})
singer_list = soup.find_all("span", {"class": "checkEllipsis"})
like_list = soup.find_all("button", {"class": "button_etc like"})

data = []
for i in range(100):
    title = title_list[i].text.replace("\n","")
    like = like_list[i].text.replace("\n", "").replace("좋아요", "").replace("총건수", "")
    singer = singer_list[i].text.replace("\n","")
    data.append([i+1, title, like, singer])
    print(str(data[i][0])+"위", data[i][1], data[i][2])

