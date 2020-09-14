# 题目：论文查重

> 描述如下：

- 设计一个论文查重算法，给出一个原文文件和一个在这份原文上经过了增删改的抄袭版论文的文件，在答案文件中输出其重- 复率。

- 原文示例：今天是星期天，天气晴，今天晚上我要去看电影。
- 抄袭版示例：今天是周天，天气晴朗，我晚上要去看电影。
- 要求输入输出采用文件输入输出，规范如下：

- 从命令行参数给出：论文原文的文件的绝对路径。
- 从命令行参数给出：抄袭版论文的文件的绝对路径。
- 从命令行参数给出：输出的答案文件的绝对路径。
- 我们提供一份样例，可以在群文件里下载，使用方法是：orig.txt是原文，其他orig_add.txt等均为抄袭版论文。



|PSP2.1|Personal Software Process Stages|预估耗时（分钟）|实际耗时（分钟）|
|--|--|--|--|
|Planning|计划|60|--|
|Estimate|估计这个任务需要多少时间|1200|
|Development|开发|
|Analysis|需求分析 (包括学习新技术)|500|
|Design Spec|生成设计文档|120
|Design Review| 设计复审|
|Coding Standard|代码规范 (为目前的开发制定合适的规范)|
|Design|具体设计|
|Coding|具体编码|
|Code Review|代码复审|
|Test|测试（自我测试，修改代码，提交修改）|
|Reporting|报告|
|Test Repor|测试报告|
|Size Measurement|计算工作量|
|Postmortem & Process Improvement Plan|事后总结, 并提出过程改进计划|
|--|合计|

> 9.10
- 学习python的jieba库 
> 9.12
- 写了文件读取与输出

- 学习[gensim](https://gensim.apachecn.org/#/blog/Introduction/README)

> 9.13
- [gensim使用方法以及例子](https://blog.csdn.net/u014595019/article/details/52218249/?biz_id=102&utm_term=corpora.Dictionary.save&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-9-52218249&spm=1018.2118.3001.4187)
- [Python+gensim-文本相似度分析](https://blog.csdn.net/Yellow_python/article/details/81021142?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160000659919724835847152%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=160000659919724835847152&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v28-2-81021142.pc_first_rank_v2_rank_v28&utm_term=similarities.SparseMatrixSimil&spm=1018.2118.3001.4187)