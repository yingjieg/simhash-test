from sklearn.feature_extraction.text import TfidfVectorizer
import jieba
from simhash import Simhash

news = """
本文转自【外交部网站】；2024年3月18日，外交部大使王克俭访问卡塔尔，会见卡外交部国务大臣胡莱菲，就中卡关系、加沙冲突等交换意见。王克俭表示，今年是中卡建立战略伙伴关系10周年。中方愿与卡方共同努力，落实好两国元首重要共识，推动中卡关系不断发展。当前加沙冲突持续延宕，人道局势极其严峻。中方愿继续同卡在内的地区国家加强沟通协调，推动全面停火止战，落实人道救援，推动巴勒斯坦问题早日得到全面、公正、持久解决。胡莱菲表示，卡方高度重视发展对华关系，愿同中方不断深化各领域友好合作。卡方赞赏中方在巴勒斯坦问题上的客观公正立场和所作努力，期待中方发挥更大作用。
"""

news2 = """
□ 证券日报记者 何文英 刘 钊
数据显示，我国是世界上老年人口规模最大的国家，目前60岁以上人口已近3亿人，预计到2035年，我国60岁以上人口将突破4亿人。今年的《政府工作报告》提出，实施积极应对人口老龄化国家战略。在此背景下，如何发展养老生态，让老年人老有所养、老有所享、老有所乐，正待多方协力破题。
政策支持发展
在当前多元化的适老产品供给中，银发经济已从过去的零星散发逐步向产业归集过渡，但如何更好地满足适老需求，促进银发经济高质量发展，仍需从顶层设计上予以支持。
今年的《政府工作报告》提出，加强老年用品和服务供给，大力发展银发经济。此前，国务院办公厅印发了我国首个以“银发经济”命名的政策文件——《关于发展银发经济增进老年人福祉的意见》。《意见》提出加快银发经济规模化、标准化、集群化、品牌化发展，培育高精尖产品和高品质服务模式。此外，相关部门也加大了对老年用品政策的倾斜力度。去年，工业和信息化部印发《促进数字技术适老化高质量发展工作方案》，提出大力培育智慧健康养老产业。
中国老龄产业协会科技委主任王永春表示：“这些政策从老年群体需求出发，在供需两端提出了具体的实施意见，相信随着政策的落实和推进，未来由政府牵头搭建、社会资本参与的银发经济产业结构将进一步完善。”
老年人能不能吃上饭、吃好饭是子女最牵挂的事。在长沙市望城区雷锋社区食堂，记者看到许多老人前来用餐。老人们你一言我一语地告诉记者，这里的菜肴无论是口味还是营养搭配都十分讲究，仅需12元就能在家门口享用四菜一汤的丰盛餐食。
据了解，雷锋社区是湖南发展集团养老产业有限公司签约的社区之一。截至目前，该公司已在长沙市签约社区居家养老服务站78家，开办运营75家，助餐服务达到17万余人次。
除了基本的养老需求，一些高品质、多样化的适老产品也越来越受到银发族的青睐。二月末的长沙春寒料峭，泰康之家湘园内享受养老服务的老人正在围炉煮茶。泰康之家养老规划师李玉婵向记者介绍：“目前全国泰康之家已有约1.2万老人在享受高品质养老服务。”
记者在可孚医疗旗下的健耳听力验配中心看到，一名听觉退化的老人正在验配师的帮助下挑选适合自己的助听器，当清晰低噪的声音传至老人耳中时，欣喜的笑容在他的脸上绽放。
可孚医疗投资者关系经理罗晓旭介绍：“随着人们健康意识和健康消费意愿的持续提升，老年人对医疗器械的需求缺口正逐步扩大，近年来公司听力业务发展迅速，旗下健耳听力收入规模从2021年不到7000万元增长至2022年的1.2亿元，2023年也保持了较快的增速。”
不同于传统的适老产品，山东青鸟软通信息技术股份有限公司则是将数字科技与养老运营服务融合，实现养老产业的创新突破。公司总经理张登国表示：“公司以全域智慧康养平台、青鸟颐居养老机构、社区居家养老服务等为依托，连接政府、企业、老人和社会各行业优质资源，建设养老服务生态圈。截至2023年11月，公司运营智慧养老平台78个、运营居家社区养老中心站398个、家庭养老床位建设及运营3.6万余张。”
堵点有待疏通
银发经济作为由人口结构转型引领的新型经济产业，市场空间巨大。据《中国老龄产业发展报告》预测，从2020年到2050年，中国老年人口的消费潜力将从约4.3万亿元增加到约40.6万亿元。发展空间广阔，但问题仍存。
湖南发展集团养老产业有限公司总经理徐志刚认为，当前养老体系的产业结构需要调整。“养老产业现在仍过多依赖政府资源和行政督办，还未形成成熟的产业体系，建议从政策、资金、产业协同等方面发力，促使养老产业形成规模化和产业化集群。”
深耕养老产业的青岛国君医疗股份有限公司董事长赵明强认为：“养老体系专业人才匮乏限制了银发经济的可持续发展，适老化改造面临着技术门槛高、专业人才缺乏等难题，目前市场上从事适老化改造的技术人员数量较少，技术水平参差不齐，难以满足市场需求。”
老年群体的消费理念也影响着相关产业。北京市丰台区老年大学教育工作室主任马格军表示：“目前受众对老年教育知识付费的积极性仍不高，要形成可持续发展的老年教育体系，不能仅依靠政府投入与公益扶持，还需在产业结构以及消费理念上有所转变。”
老年人在金融产品方面的需求也不容忽视。保障银发族的钱袋子安全，实现其金融资产的稳健增值，是促进银发经济高质量发展的重要前提。相较于以往老年群体多购买定期存款、记账式国债等产品进行理财，当下老年人对多元化金融产品的需求正在增长。
某国有大行省级分行养老金业务部工作人员向记者介绍，其所在的银行目前构建了养老金金融、养老服务金融、养老产业金融三大板块的业务体系，在基本养老保险、年金管理、个人养老金、长辈客群服务、养老产业金融等领域深耕已久。业内专家表示，养老金融产品要提高产品质量，主打大类资产配置，资管机构需要加强核心投研能力、交易纪律、人才梯队等核心内容的建设，以出色的产品配置和管理能力护航养老金融产品的保值增值。
“目前我国养老产业仍处于单点作战的状态，要疏通银发经济中的堵点，需各方共建完整的生态闭环。”北京社科院副研究员王鹏建议，市场层面，应推出更符合老年人身体结构和精神需求的产品和服务，提高其适用性；政府层面，应加强产品和服务的质量监管，推动安全性能升级，确保老年人使用无忧。同时，还应通过加强宣传教育来提高老年人对适老产品的认知度和接受度。
关注多元需求
当前我国银发经济正处于发展的初级阶段，产业要实现从有到优的转型，不仅需要提升物质层面的保障水平，也需要对老年群体的精神需求给予更多关注。
目前，越来越多的社会力量正积极探索如何进一步满足银发族多元化的精神需求。在丰台区老年大学，针对老年群体的AI应用公开课颇受欢迎。“当下社会发展日新月异，老年大学也应当与时俱进，以满足老年群体对新知识的渴求。”马格军说道。
中央财经大学数字经济融合创新发展中心主任陈端表示，对银发族需求深度挖掘并在供给侧推动精准服务和供给优化，是当前提振内需的重要抓手。在政策护航、产业发力、社会参与多管齐下推动银发经济高质量发展的基础上，还需借助数字化手段和高科技工具赋能，把分散、潜在的长尾需求更好地转化为银发经济的市场潜力。
"""

# 示例文本
corpus = [
    #news,
    #news2,
    "今天天气很好",
    "今天是好天气",
    "好天气",

]

# 中文分词
def chinese_word_cut(text):
    words = [word for word in jieba.cut(text) if len(word) > 1]
    return " ".join(words)

# 对文本进行分词处理
corpus_cut = list(map(chinese_word_cut, corpus))

# 计算 TF-IDF 权重
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus_cut)


# 生成 SimHash 值
simhash_values = []
for i in range(len(corpus)):
    simhash = Simhash(corpus_cut[i])
    groups = [simhash.value >> shift & 0xFFFF for shift in [48, 32, 16, 0]]
    binary_groups = [format(group, '016b') for group in groups]
    print(binary_groups)

    simhash_values.append(simhash.value)

# 输出 SimHash 值
for i, value in enumerate(simhash_values):
    print("Document {}: SimHash Value - {}".format(i + 1, value))

