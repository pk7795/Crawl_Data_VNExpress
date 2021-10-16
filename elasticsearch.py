import elasticsearch

def send_data_to_es(data):
    es=elasticsearch(['localhost:9200'])
    res=es.index(index='employee',doc_type='devops',body=data)
    print(res)

def get_data_from_es():
    es=elasticsearch(['localhost:9200'])
    r=es.search