#-*-coding:utf-8-*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from PIL import Image
import numpy as np
import os

'''
wc=WordCloud(
	background_color='white',#设置背景颜色
	mask=backgroud_Image,#设置背景图片
	font_path='./SimHei.ttf',#设置字体，针对中文的情况需要设置中文字体，否则显示乱码
	max_words=100,#最大的字数
	stopwords=STOPWORDS,#设置停用词
		max_font_size=150,#设置字体最大值
		width=2000,#设置画布宽度
		height=1200,#高度
	random_state=30#设置多少种随机状态，即多少种颜色
)
'''

#生产词云
def create_word_cloud(f):
	print('根据词频计算词云')
	text=" ".join(nltk.word_tokenize(f))
	wc=WordCloud(
		background_color='white',
		font_path="./SimHei.ttf",
		max_words=100,
		width=2000,
		height=1200)
	wordcloud=wc.generate(text)
	#写词云图片
	wordcloud.to_file("wordcloud.jpg")
	#显示词云
	plt.imshow(wordcloud)
	plt.axis('off')
	plt.show()

#去掉停用词
def remove_stop_words(f):
	stop_word=['ENERGIES','Journal','energy','IEEE',
			   'Energy','Science','Elsevier','one','day',
			   'using','problem','et','al','cid','based',
			   'impact','user','value','cost','result','given',
			   'higher','will','show','increase']
	for stop_word in stop_word:
		f=f.replace(stop_word,'')
	return f

#要用于生成词云的文件夹
txtDir = "E:\\文献改名\\txt汇总"
#依次读取
f=''
for txt in os.listdir(txtDir):
	textFilename = txtDir + '\\' + txt
	f +=''.join(open(textFilename,encoding='UTF-8').read())
	print(f)
print(f)

f=remove_stop_words(f)
create_word_cloud(f)
'''
keyword
test = pdf_reader.getXmpMetadata().dc_subject
		print(test)
'''