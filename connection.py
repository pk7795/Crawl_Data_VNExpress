import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="khongcogi",
  database="Crawl_Data"
)
# if(mydb):
#     print("kết nối thành công")
mycursor = mydb.cursor()
def insertCategoriesTable(payload):
    sql = "INSERT INTO categories (link_categories) VALUES (%s)"
    val = payload,
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def insertLinkArticleCategory(payload, title, content, author, date, id):
    sql = "INSERT INTO contents (link_article, title, content, author, date_created, idcategories) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (payload, title, content, author, date, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def returnIdCategory(payload):
    mycursor.execute("SELECT idcategories from categories where link_categories='" + str(payload) + "'")
    myresult = mycursor.fetchall()
    return myresult[0][0]

def selectCategories():
    mycursor.execute("SELECT * from categories")
    myresult = mycursor.fetchall()
    return myresult




# returnIdCategory('https://vnexpress.net/the-thao')
# print (returnIdCategory('https://vnexpress.net/the-thao'))
# print(selectCategories())
# for selectCategory in selectCategories():
#     print(selectCategory[1])

# insertLinkArticleCategory('sdfgh','1')
# insertCategoriesTable('test')
# print(returnIdCategory())

# for x in returnIdCategory()[0]:
#     print(x)