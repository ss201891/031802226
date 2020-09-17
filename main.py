# 导入所需的模块
import sys
import os
import jieba.analyse
# 用于分词和 tfidf
import numpy as np


# 读取文件模块
def read_text(origin_file, copy_file):
    # 原文本和抄袭文本
    if not os.path.exists(origin_file):
        raise ValueError('链接错误')
    if not os.path.exists(copy_file):
        raise ValueError('链接错误')
    fo1 = open(origin_file, encoding='UTF-8')
    fo2 = open(copy_file, encoding='UTF-8')
    origin_text = fo1.read()
    copy_text = fo2.read()
    fo1.close()
    fo2.close()
    return [origin_text, copy_text]


# 利用jieba.analyse.extract_tags将文本分割完并且得出tfidf值
def get_cult_tfidf(content):
    text_tfidfs = {}
    for word, tfidf in jieba.analyse.extract_tags(content, topK=0, withWeight=True):
        text_tfidfs[word] = tfidf
    if len(text_tfidfs) == 0:
        raise ValueError("无效文本")
    return text_tfidfs


# 将两个文本的分词对齐 如{‘第一’：1，“第二”；2，“第三”：3}
# {“第二”；2，“第三”：3，“第四”；4}
# 对齐为{‘第一’：1，“第二”；2，“第三”：3，“第四”；0}和{第一’：0，“第二”；2，“第三”：3，“第四”；4}
# 并且获得两个字典的权重列表vec_a和vac_b
def completion(content1, content2):
    zero = 0
    origin_word_list = []
    copy_word_list = []
    origin_array = {}
    copy_array = {}
    words_list = []
    for item in content1:
        origin_word_list.append(item)
    for item in content2:
        copy_word_list.append(item)
    words_list = origin_word_list + copy_word_list
    for word in words_list:
        if word not in origin_word_list:
            origin_array[word] = zero
            copy_array[word] = content2[word]
        elif word not in copy_word_list:
            origin_array[word] = content1[word]
            copy_array[word] = zero
        else:
            origin_array[word] = content1[word]
            copy_array[word] = content2[word]
    vec_a = [origin_array[item] for item in origin_array]
    vec_b = [copy_array[item] for item in copy_array]
    return [vec_a, vec_b]


# 计算余弦相似度
def cosine_similarity(vec_a, vec_b):
    num = np.dot(vec_a, vec_b)
    denom = np.linalg.norm(vec_a) * np.linalg.norm(vec_b)
    cos = num / denom  # 余弦值
    return cos


# 把答案写入文件
def write_into_text(cos, path):
    fo = open(path, 'w', encoding='UTF-8')
    fo.write(str(round(cos, 2)))
    fo.close()


# 调用各个函数求得答案
def get_similar(origin_file, copy_file):
    [origin_text, copy_text] = read_text(origin_file, copy_file)
    origin_tfidf = get_cult_tfidf(origin_text)
    copy_tfidf = get_cult_tfidf(copy_text)
    # print(origin_tfidf, copy_tfidf)
    [vec_a, vec_b] = completion(origin_tfidf, copy_tfidf)
    cos = cosine_similarity(vec_a, vec_b)
    return cos


if __name__ == '__main__':
    if len(sys.argv) < 4:
        raise ValueError('参数缺失')
    origin_file = sys.argv[1]
    copy_file = sys.argv[2]
    cos = get_similar(origin_file, copy_file)
    if cos > 0.99:
        cos = 1
    path = sys.argv[3]
    write_into_text(cos, path)
