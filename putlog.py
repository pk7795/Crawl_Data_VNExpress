from connection import selectlog
import codecs
def putlog1():
    slog = selectlog()
    f = codecs.open("data1.txt", "a", encoding='utf8')
    for i in slog:

        f.write(i[3])
        print(i[3])
    f.close()
putlog1()