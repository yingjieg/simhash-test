import jieba
from simhash import Simhash

# 多个中文句子，包括一些相似的句子
chinese_sentences = [
    "今天天气真好，我们一起去公园玩吧。",
    "今天的天气非常好，我们一起去公园散步吧。",
    "明天下雨，最好带把伞。",
    "明天可能会下雨，最好带把雨伞。",
    "春天来了，花开满园。",
    "春风拂面，百花盛开。",
    "学习使人进步，勤奋是成功之母。",
    "学无止境，勤能补拙。"
]

# 计算每个句子的Simhash值
for sentence in chinese_sentences:
    seg_list = jieba.lcut(sentence, cut_all=False)
    seg_str = " ".join(seg_list)
    simhash = Simhash(seg_str)
    
    print(f"Simhash value for the sentence '{sentence}':")
    print(simhash.value)
    print()

