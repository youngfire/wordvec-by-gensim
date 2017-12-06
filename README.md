	# 本程序参考https://github.com/zake7749/word2vec-tutorial
	# 环境python2.7
	# download wiki text from 
	# https://dumps.wikimedia.org/zhwiki/

	# user dictionary and stop words texts are from
	# https://github.com/dongxiexidian/Chinese
	

	#主要步骤：
	
	# 1 解压文件
	# unziped wiki text from xml.bz2, saving path "wiki_texts.txt"
	zhwiki_file = 'zhwiki-latest-pages-articles.xml.bz2'
	data_input.data_read_xmlbz2(zhwiki_file, "wiki_texts.txt")

	# 2 繁体转换为简体中文 删除非中文词句
	# transform from complex Chinese to simply Chinese,
	# keep Chinese words and delete other words
	# load data from 'wiki_texts.txt' and save to 'wiki_simply.txt'
	data_transform.text_transformation('wiki_texts.txt', 'wiki_simply.txt')

	# 3 中文分词
	# tokenize text and save to "wiki_seg.txt"
	# user dictionary words file: "user_dict.txt"
	# user stop words file: 'user_stopwords.txt'
	word_cut.text_tokneize('wiki_simply.txt', 'wiki_seg.txt')
	
	# 4 模型训练
	# load tokenized file from "wiki_seg.txt"
	# save model to "med250.model.bin"
	wv_train.model_training("wiki_seg.txt","med250.model.bin")

	# 5 模型读取
	# load model
	# model = wv_train.model_load("med250.model.bin")

	# do some little tests
	# 输出距离某个词向量最近的top 100词向量
	# res = model.most_similar(u'总统',topn = 100)
	# 输出两个词向量的相似性
	# res = model.similarity(u'总统',u'努力')
