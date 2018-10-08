fileNoticias = open('noticias.csv', 'rt', encoding="latin-1")
fileStopWords = open('stopwords.txt', 'rt', encoding="utf-8")

stopWordsArray = [stopWord[:-1] for stopWord in fileStopWords]
specialCharacters = stopWordsArray[0:28]
stopWords = stopWordsArray[28:-1]
noticias = [noticia[:-1] for noticia in fileNoticias]
dataToLemmatize = []

def clean():
    for noticia in noticias:
        row = noticia.lower()
        for specialCharacter in specialCharacters:
            row = row.replace(specialCharacter, '')
        row = row.split()
        # para esta noche tormentas intensas, de 75 a 150 milí
        for word in row:
            if word not in stopWords:
                dataToLemmatize.append(word)
                print('++++++++++++++++++++')
                print(word)
                print('++++++++++++++++++++')
            else:
                print(word)
        print('********************')