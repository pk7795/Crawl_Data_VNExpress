from connection import selectCate
from connection import selectAll
from connection import insertLog
import codecs
def PutLog():
    selectcate = selectCate()
    selectall = selectAll()
    # cat= selectcate[1]
    # link= selectall[2]
    # title= selectall[3]
    # author= selectall[4]
    # date= selectall[5]
    # para= selectall[6]
    # sent= selectall[7]
    # sentence= selectall[8]
    f = codecs.open("C:\elk\data2.json", "a", encoding='utf8')
    r = 401
    for i in selectcate:
        for j in selectall:
            try:
                if (j[0]==i[0]):
                    # insertLog(i[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8])
                    try:
                        f.write("{\"index\": {\"_index\": \"express\",\"_id\":"+str(r)+"}}"+"\n"+"{\"IdLog\": "+str(r)+", \"Category\":\""+i[1]+"\",\"Link\" :\""+j[2]+"\",\"Title\":\""+j[3]+"\",\"Author\":\""+j[4]+"\",\"Date_Created\":\""+j[5]+"\",\"Locate_Paragraph\":"+str(j[6])+",\"Locate_Sentence\":"+str(j[7])+",\"Sentence\":\""+j[8]+"\"}"+"\n")
                    except:
                        break
                        print("loi roi")
                    print("ban ghi thu: "+str(r))
                    r+=1
            except:
                continue
    f.close()
PutLog()