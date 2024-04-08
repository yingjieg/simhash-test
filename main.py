import jieba
from simhash import Simhash

# 中文句子
chinese_sentence = "今天天气真好，我们一起去公园玩吧。"

# 使用jieba进行分词
seg_list = jieba.lcut(chinese_sentence, cut_all=False)

# 将分词结果拼接成字符串
seg_str = " ".join(seg_list)

# 计算Simhash值
simhash = Simhash(seg_str)

print("Simhash value for the Chinese sentence:")
print(simhash.value)

