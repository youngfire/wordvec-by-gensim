# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import jieba
import logging
import sys
import jieba.analyse
import codecs
import re
# Chinese extraction
def Chinese_word_extraction(content_raw):
	chinese_pattern = ur"([\u4e00-\u9fa5]+)"
	chi_pattern = re.compile(chinese_pattern)
	re_data = chi_pattern.findall(content_raw)
	content_clean  = ' '.join(re_data)
	return content_clean

from hanziconv import HanziConv

# Traditional 2 Simplified
def tra2sim(content):
	content = HanziConv.toSimplified(content)
	return content


def text_transformation(load_path,save_path):
	with codecs.open(load_path, 'rb', 'utf-8') as f1:
		with codecs.open(save_path, 'w', 'utf-8') as f2:
			for line in f1:
				line = line.strip('\n')
				line = tra2sim(line)
				line = Chinese_word_extraction(line)
				f2.write(line+'\n')
if __name__ == '__main__':
	reload(sys)
	sys.setdefaultencoding("utf-8")
	text_transformation('wiki_texts.txt', 'wiki_simply.txt')
	# a = tra2sim()
	# a = Chinese_word_extraction(a)
	# print a
