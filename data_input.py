# -*- coding: utf-8 -*-
import logging
import sys
import io

from gensim.corpora import WikiCorpus



def data_read_xmlbz2(zhwiki_file, save_path = "wiki_texts.txt"):

	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	wiki_corpus = WikiCorpus(zhwiki_file, dictionary={})
	texts_num = 0

	with io.open("wiki_texts.txt",'w',encoding='utf-8') as output:
	    for text in wiki_corpus.get_texts():
	        output.write(b' '.join(text).decode('utf-8') + '\n')
	        texts_num += 1
	        if texts_num % 10000 == 0:
	            logging.info("已处理 %d 篇文章" % texts_num)

if __name__ == "__main__":
	reload(sys)
	sys.setdefaultencoding("utf-8")
	zhwiki_file = 'zhwiki-latest-pages-articles.xml.bz2'
	data_read_xmlbz2(zhwiki_file)