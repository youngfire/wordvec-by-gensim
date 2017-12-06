# -*- coding: utf-8 -*-

from gensim.models import word2vec
import logging
import sys
def model_training(seg_file, model_path):
	
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	sentences = word2vec.Text8Corpus(seg_file)
    # exit()
    # size:這表示的是訓練出的詞向量會有幾維
    # alpha:機器學習中的學習率，這東西會逐漸收斂到 min_alpha
	# sg:這個不是三言兩語能說完的，sg=1表示採用skip-gram,sg=0 表示採用cbow
	# window:滑窗大小
	# workers:线程数
	# min_count:若這個詞出現的次數小於min_count，那他就不會被視為訓練對象
	model = word2vec.Word2Vec(sentences, size=250)

	# Save our model.
	model.save(model_save)

def model_load(model_path):
	# To load a model.
	model = word2vec.Word2Vec.load(model_path)
	return model
	
if __name__ == "__main__":

	reload(sys)
	sys.setdefaultencoding("utf-8")

	
	model_training()




	model = model_load()
	q_list = u'总统'
	res = model.most_similar(u'张扬帆',topn = 100)
	for r in res:
		print r[0]

	print '*'*40
	res = model.similarity(u'总统',u'国王')
	print res
	res = model.similarity(u'总统',u'努力')
	print res
	print '*'*40