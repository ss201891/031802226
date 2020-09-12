import jieba
import os
def readtextfile():
# C:\\Users\\ss\\Desktop\\文本相似度\\gan.TXT
# C:\\Users\\ss\\Desktop\\文本相似度\\kan.TXT
    paper = input("请输入论文文件名：")
    copypaper = input("请输入抄袭论文文件名：")
    try:
        papertext =open(paper,'r',encoding='UTF-8')
        copypapertext = open(copypaper,'r',encoding='UTF-8')
    except IOError as e:
        print("file open error:",e)
    else:
        for eachLine in papertext:
            print(eachLine,end='')
        print('')
        papertext.close()
        for eachLine in copypapertext:
            print(eachLine, end='')
        copypapertext.close()

