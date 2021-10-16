import newspaper
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from connection import add_category
from connection import add_news
from connection import get_category_by_id
from connection import get_category

express_paper = newspaper.build('https://vnexpress.net/')
def getResponse(category, payload):
    response = requests.get(category)
    soup = BeautifulSoup(response.content, "html.parser")
    thumb = soup.findAll('p', class_='description')
    links = [link.find('a').attrs["href"] for link in thumb]
    category_id = get_category_by_id(payload)
    count=0
    rec=0
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
        add_news(titles, description + '\n' + ct, j, author, date, category_id)

        count+=1
    rec+=count
    now = datetime.now()
    ngaygio = now.strftime("%d/%m/%Y %H:%M:%S")
    # f = open("log.txt", "a")
    # f.write(str(category) + '-p' + str(i) + '\n')
    f.write('---------records: '+str(rec)+' records'+'\n')
    f.write('---------'+str(ngaygio)+'\n')
    f.close()
    print(rec)
    print(ngaygio)
listCategory = []
selectCategories = get_category()

if (selectCategories == []):
    for category in express_paper.category_urls():
        if (category == 'https://vnexpress.net/the-gioi-p4'
                or category == 'https://vnexpress.net/the-gioi-p3'
                or category == 'https://vnexpress.net/the-gioi-p2'
                or category == 'https://vnexpress.net/'
                or category == 'https://vnexpress.net'
                or category == 'https://e.vnexpress.net'
                or category == 'https://video.vnexpress.net'
                or category == 'https://vnexpress.net/goc-nhin'
                or category == 'https://vnexpress.net/tin-tuc-24h'
                or category == 'https://vnexpress.net/y-kien'):

            continue
        listCategory.append(category)
    listCategory = list(set(listCategory))
    for category in listCategory:
        t = category[22:].split("-")
        cat = ""
        for i in t:
            cat += i + " "
        print(cat)
        print(category)
        add_category(cat, category)


for category in selectCategories:
    for i in range(1, 10):
            try:
                f = open("db1.log1.txt", "a")
                f.write(str(category) + '-p' + str(i) + '\n')
                print('-----'+str(category)+'-p'+str(i)+'-----')
                getResponse(category[2] + '-p' + str(i), category[2])
            except:
                continue
