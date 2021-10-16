from connection import insertSentence
from connection import selectIdParagraph
def spilitpara():
    selectIdPara = selectIdParagraph()
    for j in selectIdPara[1855700::1]:
        if (len(j[1])>1):
            try:
                para = j[1]
                p = para.split(". ")
                cau = 1
                for i in p:
                    print(i + "\n")
                    try:
                        print("câu số: "+str(cau)+" -đoạn số: "+str(j[0]))
                        insertSentence(i,cau, j[0])
                        cau+= 1
                    except:
                        continue
                # print(j[0])
            except:
                continue
spilitpara()