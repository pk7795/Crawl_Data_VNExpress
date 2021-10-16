from connection import insertParagraph
from connection import selectIdContent
def spilitcontent():
    selectIdcontent = selectIdContent()
    for j in selectIdcontent:
        if (j[0] > 138093):
            try:
                content = j[3]
                p = content.split("\n")
                doan = 1
                for i in p:
                    print(i + "\n")
                    try:
                        if(i!=["\n"] or i!=["\""] or len(i)!=0):
                            insertParagraph(i, doan, j[0])
                            doan+= 1
                    except:
                        continue
                print(j[0])
            except:
                continue
spilitcontent()