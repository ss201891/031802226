#导入所需的模块
from gensim import corpora,models,similarities
import jieba
from collections import defaultdict

#打开并读取文件
f1 = "C:\\Users\\ss\\Desktop\\文本相似度\\sim_0.8\\orig.txt"
f2 = "C:\\Users\\ss\\Desktop\\文本相似度\\cn_stopwords.txt"
#停用词库与原文进入tfidf训练

content1 = open(f1,encoding='UTF-8').read()
content2 = open(f2,encoding='UTF-8').read()

#对文档进行分词
data1 = jieba.cut(content1)
data2 = jieba.cut(content2)

#整理文档格式，格式为："词语1 词语2 ... 词语n "(词语之间用空格分隔)
str1 = ""
for item in data1:
    str1+=item+" "
#print(str1)
str2 = ""
for item in data2:
    str2+=item+" "
#print(str2)

#split默认分隔符为空格
str_all = [str1,str2]
text = [[word for word in str3.split()]
        for str3 in str_all]

#计算词语频率
frequency = defaultdict(int)
for i in text:
    for token in i:
        frequency[token]+=1
#过滤词频为3的
'''
texts=[[word for word in text if frequency[token]>3]
 for text in texts]
'''
#通过语料库建立词典
dictionary = corpora.Dictionary(text)
# dictionary.save("D:/reptile/file/dict1.txt")

#加载要对比的文档
f3 = "C:\\Users\\ss\\Desktop\\文本相似度\\sim_0.8\\orig_0.8_dis_1.txt"
content3 = open(f3,encoding='UTF-8').read()
data3 = jieba.cut(content3)

str3 = ""
for item in data3:
    str3+=item+" "
new_data = str3

#doc2bow将文件变成一个稀疏矩阵
new_vec = dictionary.doc2bow(new_data.split())

#对字典进行docbow处理，得到新的语料库
corpus = [dictionary.doc2bow(j) for j in text]

#将corpus语料库持久化到磁盘中，词句可以删除
#corpora.MmCorpus.serialize("D:/reptile/file/New_Yuliaoku.mm",corpus)

#将新的语料库通过TfidfModel处理，得到tfidf
tfidf = models.TfidfModel(corpus)
print("tfidf :",tfidf)
#求特征数
featureNum = len(dictionary.token2id.keys())

#SparseMatrixSimilarity 稀疏矩阵相似度
index = similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=featureNum)
print("index: ",index)
#得到结果
sim = index[tfidf[new_vec]]

#打印结果
print(sim[0])