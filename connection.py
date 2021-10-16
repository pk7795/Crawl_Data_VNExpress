import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="crawl_data"
)
mycursor = mydb.cursor()
def add_category(name, url):
    sql = "INSERT INTO categories (name, url) VALUES (%s , %s)"
    val = (name, url)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def add_news(title, description, link, author, date, id):
    sql = "INSERT INTO news (title, description, original_url, author, date_created, category_id) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (title, description, link, author, date, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def get_category_by_id(url):
    mycursor.execute("SELECT id from categories where url='" + str(url) + "'")
    myresult = mycursor.fetchall()
    return myresult[0][0]

def get_category():
    mycursor.execute("SELECT * from categories where id=4")
    myresult = mycursor.fetchall()
    return myresult

def get_news():
    mycursor.execute("SELECT * from news")
    myresult = mycursor.fetchall()
    return myresult
########################################################################################
# def selectIdContent():
#     mycursor.execute("SELECT * from contents")
#     myresult = mycursor.fetchall()
#     return myresult
#
# def selectIdParagraph():
#     mycursor.execute("SELECT * from paragraph")
#     myresult = mycursor.fetchall()
#     return myresult
#
# def insertParagraph(para, doan, payload):
#     sql = "INSERT INTO paragraph (paragraph, doan, idcontent) VALUES (%s, %s, %s)"
#     val = (para, doan, payload)
#     mycursor.execute(sql, val)
#     mydb.commit()
#     print(mycursor.rowcount, "record inserted. ")
#
# def insertSentence(sent, cau, payload):
#     sql = "INSERT INTO sentence (sentence, cau, id_para) VALUES (%s, %s, %s)"
#     val = (sent, cau, payload)
#     mycursor.execute(sql, val)
#     mydb.commit()
#     print(mycursor.rowcount, "record inserted. ")
#
# def selectCate():
#     mycursor.execute("select idcategories, SUBSTRING(link_categories, 23, 12) from categories")
#     return mycursor.fetchall()
#
# def selectAll():
#     mycursor.execute("select contents.idcategories, sentence.id_sen, contents.link_article, contents.title, contents.author, contents.date_created, paragraph.doan, sentence.cau, sentence.sentence from contents join paragraph on contents.idcontent=paragraph.idcontent join sentence on sentence.id_para= paragraph.id_para where sentence.id_sen between 400 and 1000 ")
#     myresult = mycursor.fetchall()
#     return myresult
#
# def insertLog(Category, Link, Title, Author, Date_created, Locate_para, Locate_sent, Sentence):
#     sql = "INSERT INTO log (Category, Link, Title, Author, Date_created, Locate_para, Locate_sent, Sentence) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#     val = (Category, Link, Title, Author, Date_created, Locate_para, Locate_sent, Sentence)
#     mycursor.execute(sql, val)
#     mydb.commit()
#     print(mycursor.rowcount, "record inserted. ")
#
# def selectlog():
#     mycursor.execute("select * from log where Idlog=1")
#     myresult= mycursor.fetchall()
#     return myresult
if __name__ =="__main__":
    print(get_category())