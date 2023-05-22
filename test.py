import chardet
with open('googleplaystore.csv', 'rb') as f:
    result = chardet.detect(f.read())
    print(result['encoding'])
