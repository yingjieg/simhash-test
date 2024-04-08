import jieba
from simhash import Simhash

# 定义文本相似度阈值
threshold = 10

# 分词函数
def cut_text(text):
    return [word for word in jieba.cut(text) if len(word) > 1]

# 计算Simhash值
def get_simhash(text):
    words = cut_text(text)
    return Simhash(words)

# 判断两篇新闻是否相似
def is_similar(news1, news2):
    simhash1 = get_simhash(news1)
    simhash2 = get_simhash(news2)
    print(simhash1.value)
    print(simhash2.value)
    distance = simhash1.distance(simhash2)
    if distance < threshold:
        return True
    else:
        return False

# 两篇相似新闻示例
news1 = "今天天气很好"
news2 = "今天有很好的天气"

if is_similar(news1, news2):
    print("这两篇新闻相似")
else:
    print("这两篇新闻不相似")

