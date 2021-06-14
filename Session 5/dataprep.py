import pandas as pd
import os
os.chdir(r'/mnt/567ABBD17ABBABDD/Learning/TSAI/END_2_Assignments/Session 5/stanfordSentimentTreebank')

sents = pd.read_csv(r'datasetSentences.txt', sep = '\t')
p_dct = pd.read_csv(r'dictionary.txt',sep = '|', header = None, names=['phrase','phrase ids'])
slbls = pd.read_csv(r'sentiment_labels.txt', sep = "|")
dsplt = pd.read_csv(r'datasetSplit.txt', sep = ",")