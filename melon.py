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

print("\n<일간 차트>")
data = []
for i in range(100):
    title = title_list[i].text.replace("\n","")
    singer = singer_list[i].text.replace("\n","")
    like = int(like_list[i].text.replace("\n", "").replace("좋아요", "").replace("총건수", "").replace(",", ""))
    data.append([title, singer, like])
    print(str(i+1)+"위", data[i][0], data[i][1], "(♡: "+str(data[i][2])+")")



def selection_sort(list):
    for a in range(100):
        for b in range(99):
            if list[b][2]<list[b+1][2]:
                temp = list[b+1][0]
                list[b+1][0] = list[b][0]
                list[b][0] = temp
                temp = list[b + 1][1]
                list[b+1][1] = list[b][1]
                list[b][1] = temp
                temp = list[b+1][2]
                list[b+1][2] = list[b][2]
                list[b][2] = temp
            else:
                pass

selection_sort(data)

print("\n<♡ 순위>")
for i in range(100):
    print(str(i+1)+"위", data[i][0], data[i][1], "(♡: "+str(data[i][2])+")")

driver.quit()