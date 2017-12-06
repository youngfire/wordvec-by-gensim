# -*- coding: utf-8 -*-

from gensim.models import word2vec
import logging
import sys

import data_input
import data_transform
import word_cut
import wv_train


if __name__ == '__main__':
	print 'RUNNING'
	# download wiki text from 
	# https://dumps.wikimedia.org/zhwiki/

	# user dictionary and stop words texts are from
	# https://github.com/dongxiexidian/Chinese

	# unziped wiki text from xml.bz2, saving path "wiki_texts.txt"
	zhwiki_file = 'zhwiki-latest-pages-articles.xml.bz2'
	data_input.data_read_xmlbz2(zhwiki_file, "wiki_texts.txt")

	# transform from complex Chinese to simply Chinese,
	# keep Chinese words and delete other words
	# load data from 'wiki_texts.txt' and save to 'wiki_simply.txt'
	data_transform.text_transformation('wiki_texts.txt', 'wiki_simply.txt')

	# tokenize text and save to "wiki_seg.txt"
	# user dictionary words file: "user_dict.txt"
	# user stop words file: 'user_stopwords.txt'

	word_cut.text_tokneize('wiki_simply.txt', 'wiki_seg.txt')


	# load tokenized file from "wiki_seg.txt"
	# save model to "med250.model.bin"
	wv_train.model_training("wiki_seg.txt","med250.model.bin")

	# load model

	# model = wv_train.model_load("med250.model.bin")

	# do some little tests

	# q_list = u'总统'
	# res = model.most_similar(u'张扬帆',topn = 100)
	# for r in res:
	# 	print r[0]

	# print '*'*40
	# res = model.similarity(u'总统',u'国王')
	# print res
	# res = model.similarity(u'总统',u'努力')
	# print res
	# print '*'*40