import newspaper
import requests
from bs4 import BeautifulSoup
from connection import insertCategoriesTable
from connection import insertLinkArticleCategory
from connection import returnIdCategory
from connection import selectCategories

express_paper = newspaper.build('https://vnexpress.net/')

def getResponse(category, payload):
    response = requests.get(category)
    soup = BeautifulSoup(response.content, "html.parser")
    thumb = soup.findAll('div', class_='thumb-art')
    links = [link.find('a').attrs["href"] for link in thumb]
    idcategory = returnIdCategory(payload)

    for j in links:
        news = requests.get(j)
        soup_2 = BeautifulSoup(news.content, "html.parser")
        date = soup_2.find('span', {'class': 'date'}).text
        titles = soup_2.find('h1', {"class": "title-detail"}).text
        contents = soup_2.findAll('p', {"class": "Normal"})
        description = soup_2.find('p', {"class": "description"}).text
        ct = ""
        author = ""
        try:
            author = soup_2.find('p', {'class': 'author_mail'}).text
        except:
            author=""

        if(author == ""):
            try:
                author = contents[-1].text
                text_condition_1 = '>> Bài viết không nhất thiết trùng với quan điểm VnExpress.net. Gửi bài tại đây.'
                text_condition_2 = '>> Các ý kiến không nhất thiết trùng với quan điểm VnExpress.net. Gửi bài tại đây.'
                text_condition_3 = 'Mời độc giả đặt câu hỏi tại đây'
                text_condition_4 = 'Độc giả quan tâm có thể gửi câu hỏi tới các diễn giả tại đây'
                if (author == text_condition_1 or author == text_condition_2 or author == text_condition_3 or author == text_condition_4):
                    author = contents[-2].text
                if (len(author) > 50):
                    author = ""
            except:
                author = ""
        for content in contents:
            if content.text != author:
                ct = ct + content.text + '\n'
        insertLinkArticleCategory(j, titles, description + '\n' + ct, author, date, idcategory)

listCategory = []
selectCategories = selectCategories()

if (selectCategories == []):
    for category in express_paper.category_urls():
        if (category == 'https://vnexpress.net/the-gioi-p4' or category == 'https://vnexpress.net/the-gioi-p3' or category == 'https://vnexpress.net/the-gioi-p2' or category == 'https://vnexpress.net' or category == 'https://e.vnexpress.net' or category == 'https://video.vnexpress.net' or category == 'https://vnexpress.net/goc-nhin'):
            continue
        listCategory.append(category)
    listCategory = list(set(listCategory))
    for category in listCategory:
        insertCategoriesTable(category)

for category in selectCategories:
    for i in range(1, 1800):
        try:
            f=open("log.txt","a")
            f.write(str(category)+'-p'+str(i)+'\n')
            print(str(category)+'-p'+str(i))
            getResponse(category[1] + '-p' + str(i), category[1])
            f.close()
        except:
            continue
