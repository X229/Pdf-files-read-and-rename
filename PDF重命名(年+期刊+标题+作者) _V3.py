#-*-coding:utf-8-*-

#IEEE！！！全都改不了！！！而且他们的标题占位的符号一模一样！！！会互相顶掉！！！

import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from shutil import copy2
import re
import xml

src_dir = 'E:\文献改名\模型'  # 源文件目录地址!间隔符使用\\而非\!
des_dir = 'E:\文献改名\模型'  # 新文件目录地址
num = 1	#计数器
paper_title_total=[]	#标题

#源文件与新文件目录相同时，在源文件根目录下创建新文件夹
if src_dir==des_dir:
	des_dir+='\\new'

if not os.path.exists(des_dir):  # 如果没有目标文件夹,新建一个目标文件夹进行存储
	os.makedirs(des_dir)

def paper_rename(src_dir,dirc,des_dir,paper_year,
		   paper_journal,paper_title,paper_author):
	copy2(os.path.join(src_dir, dirc),
		  os.path.join(des_dir,
					   paper_year + '-' +
					   paper_journal + '-' +
					   paper_title + '-' +
					   paper_author) + '.pdf')

def validateTitle(title):
	rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
	title_new = re.sub(rstr, "_", title)  # 替换为下划线
	return title_new

if os.path.exists(src_dir):
	dirs = os.listdir(src_dir)  # 获取源文件的目录地址
	for dirc in dirs:  # 对于目录下的每一个文件
		print(dirc)
		pdf_reader = PdfFileReader(open(os.path.join(src_dir, dirc), 'rb'))  # 打开并建立一个PDF文件对象
		try:
			paper_title = pdf_reader.getDocumentInfo().title	#获取文章标题
			# 获取作者名（有时只能获得一位）
			if pdf_reader.getDocumentInfo().author!= None:
				paper_author=pdf_reader.getDocumentInfo().author
			else:
				paper_author =''
			# 获取发表年份（文件原始创建时间）
			paper_year='XXXX'
			try:
				paper_year=pdf_reader.getXmpMetadata().xmp_createDate.year
				paper_year = str(paper_year)
			except AttributeError as e:
				pass
			#获取期刊名
			paper_journal = pdf_reader.getDocumentInfo().subject
			try:
				if len(paper_journal)>200:
					paper_journal='XXXX'
				else:
					paper_journal_new=''
					for stri in paper_journal:
						if stri!=',':
							paper_journal_new+=''.join(stri)
						else:
							break
					paper_journal=paper_journal_new
			except TypeError:
				paper_journal ='XXXX'
				pass
			#预览
			print("num : %s" % num,'\n',paper_year,
				  '\n', paper_journal,'\n', paper_title,
				  '\n',paper_author)
			print('-'*100)
			num += 1
			#字符化
			paper_journal=str(paper_journal)
			paper_title = str(paper_title)
			paper_author= str(paper_author)
			#存储文件名并查重，重则加上序号
			i=1
			for name in paper_title_total:
				if name==paper_title:
					i+=1
			if i==1:
				paper_title_total.append(paper_title)
			else:
				paper_title_total.append(paper_title)
				paper_title=paper_title+'('+str(i)+')'
			#文件名检查
			paper_journal=validateTitle(paper_journal)
			paper_title = validateTitle(paper_title)
			paper_author = validateTitle(paper_author)
			#生成新文件
			paper_rename(src_dir, dirc, des_dir, paper_year,
						 paper_journal, paper_title, paper_author)
		except xml.parsers.expat.ExpatError:
			print('无法读取')
			copy2(os.path.join(src_dir, dirc),os.path.join(des_dir, dirc))
			print('-' * 100)

else:
	print("该路径下不存在所查找的目录!")
