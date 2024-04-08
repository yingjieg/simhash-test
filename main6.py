from sklearn.feature_extraction.text import TfidfVectorizer
import jieba
import re
from simhash import Simhash, SimhashIndex

news = """
在当今数字化时代，人们越来越依赖互联网获取信息、沟通交流。社交媒体平台如今已经成为人们日常生活中不可或缺的一部分，无论是工作还是娱乐。通过社交媒体，人们可以迅速了解世界各地发生的事件，分享自己的生活点滴，与朋友家人保持联系。然而，随之而来的是信息泛滥和隐私泄露等问题，这需要我们更加谨慎地使用这些平台，保护个人隐私和信息安全。
"""

news2 = """
在当前数字化时代，互联网已经深刻改变了人们的生活方式和社会交往模式。社交媒体作为信息传播和交流的重要平台，已经成为人们日常生活中不可或缺的一部分。通过社交媒体，人们可以方便地获取各种信息、与他人分享生活点滴、保持社交联系。然而，随着社交媒体的普及，信息安全和隐私保护等问题也日益突出，我们必须更加重视个人信息的保护，避免隐私泄露和数据滥用的风险。
"""

pattern = re.compile(r"[^\u4e00-\u9fa5a-zA-Z0-9]+")

# 示例文本
corpus = [
    # news,
    # news2,
    "今天天气很好",
    "今天是好天气",
    "今天天气不错",
    "今天天气好",
    "好天气",
    "今天好天气",
]

# 中文分词
def chinese_word_cut(text):
    output = ""
    seg_list =  jieba.lcut(text, cut_all=False)
    for word in seg_list:
        word = pattern.sub("", word)
        if word != "":
            output = output + " " + word

    # print(output)
    return output

# 对文本进行分词处理
corpus_cut = list(map(chinese_word_cut, corpus))

# 计算 TF-IDF 权重
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus_cut)


index = SimhashIndex([], k=3)


for i in range(len(corpus)):
     # 获取非零特征和权重
    features = X[i].nonzero()[1]
    weights = X[i].data

    # 构建特征和权重的元组列表
    feature_weight_pairs = [(str(f), w) for f, w in zip(features, weights)]
    # print(feature_weight_pairs)

    # 生成 SimHash 值
    simhash = Simhash(feature_weight_pairs)
    # simhash = Simhash(corpus_cut[i])

    #groups = [simhash.value >> shift & 0xFFFF for shift in [48, 32, 16, 0]]
    #binary_groups = [format(group, '016b') for group in groups]

    #data_set = set()

    #for group in groups:
    #    bin_data = format(group, '016b')
    #    print(bin_data)
    #    if bin_data in data_set:
    #        print("Found")
    #    else:
    #        data_set.add(bin_data)

    similar_docs = index.get_near_dups(simhash)

    if len(similar_docs) > 0:
        print(i, end=" similar ")
        print(similar_docs);
    else:
        index.add(i, simhash)



