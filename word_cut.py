# -*- coding: utf-8 -*-

import jieba
import logging
import sys
import jieba.analyse
import codecs
def text_tokneize(load_path, save_path):

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # jieba custom setting.
    jieba.load_userdict("user_dict.txt")
    # jieba.set_dictionary('jieba_dict/dict.txt.big')
    # jieba.analyse.set_stop_words("../extra_dict/stop_words.txt")
    # load stopwords set
    stopwordset = set()
    with codecs.open('user_stopwords.txt','rb','utf-8') as sw:
        for line in sw:
            stopwordset.add(line.strip('\n'))
    print "stop words number is %d" %(len(stopwordset))

    texts_num = 0
    with codecs.open(save_path,'w','utf-8') as f_out:
        with open(load_path,'r') as content :
            for line in content:
                line = line.strip('\n')
                words = jieba.cut(line, cut_all=False)
                for word in words:
                    if word not in stopwordset:
                        f_out.write(word +' ')
                texts_num += 1
                if texts_num % 10000 == 0:
                    logging.info("已完成前 %d 行的断词" % texts_num)
    
    
if __name__ == '__main__':

    reload(sys)
    sys.text_tokneize("utf-8")
    main()











