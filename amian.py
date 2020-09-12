import numpy as np
import jieba
#读取停用词
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='gbk').readlines()]
    return stopwords

# 加载停用词
stopwords = stopwordslist("停用词.txt")

def cosine_similarity(sentence1: str, sentence2: str) -> float:
    """
    :param sentence1: s
    :param sentence2:
    :return: 两句文本的相识度
    """
    seg1 = [word for word in jieba.cut(sentence1) if word not in stopwords]
    seg2 = [word for word in jieba.cut(sentence2) if word not in stopwords]
    word_list = list(set([word for word in seg1 + seg2]))#建立词库
    word_count_vec_1 = []
    word_count_vec_2 = []
    for word in word_list:
        word_count_vec_1.append(seg1.count(word))#文本1统计在词典里出现词的次数
        word_count_vec_2.append(seg2.count(word))#文本2统计在词典里出现词的次数

    vec_1 = np.array(word_count_vec_1)
    vec_2 = np.array(word_count_vec_2)
    #余弦公式

    num = vec_1.dot(vec_2.T)
    denom = np.linalg.norm(vec_1) * np.linalg.norm(vec_2)
    cos = num / denom
    sim = 0.5 + 0.5 * cos

    return sim


str1="重庆是一个好地方"
str2="重庆好吃的在哪里"
str3= "重庆是好地方"
sim1=cosine_similarity(str1,str2)
sim2=cosine_similarity(str1,str3)
print("sim1 ：",sim1)
print("sim2:",sim2)