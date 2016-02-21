
def clean_mongo(result):
    cleaned = { str(key): val for key, val in result.iteritems()}
    return cleaned
