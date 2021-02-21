import os
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
import json

nltk.download("punkt")
nltk.download("stopwords")


def preProcess(file):
    file = file.lower()
    punc = """!()-[]{};:'"\, <>./?@#$%^&*_~"""
    for ele in file:
        if ele in punc:
            file = file.replace(ele, " ")

    text_tokens = word_tokenize(file)
    tokens_without_sw = set(
        [word for word in text_tokens if not word in stopwords.words()]
    )
    return tokens_without_sw


def tokenize(index, tokens, filePath):
    for i in tokens:
        if i in index:
            index[i].append(filePath)
        else:
            index[i] = [filePath]


allFiles = os.walk("stories")
index = {}
for i in allFiles:
	for j in i[2]:
		filePath = i[0] + "/" + j
		print(filePath)
		try:
			file = open(filePath, encoding="utf8")
			read = file.read()
			file.seek(0)
			tokens = preProcess(read)
			tokenize(index, tokens, filePath)
			json.dump(index, open("output.json", "w"))

		except:
			print("error")