import os
import pandas as pd

os.chdir(r'stanfordSentimentTreebank')

## Loading reviews
sents = pd.read_csv('datasetSentences.txt',sep = "\t")

alltog = '.'.join(sents.sentence.str.lower().to_list())

sent_chars = set(alltog)

## Loading Phrases
phrs = pd.read_csv('dictionary.txt', sep = "|", header = None, names= ['phrase', 'phrase id'] )
phrstog = '.'.join(phrs.phrase.str.lower().to_list())
phrs_chars = set(phrstog)

replacements = {        '-LRB-' : '(',
        '-RRB-' : ')',
        '\xa0' : ' ',
        '\xc2' : '',
        '\xc3\x83\xc2\xa0' : 'a',
        'à' : 'a',
        'Â' : '',
        'â' : 'a',
        'ã' : 'a',
        'Ã¡' : 'a',
        'Ã¢' : 'a',
        'Ã£' : 'a',
        'Ã¦' : 'ae',
        'Ã§' : 'c',
        'Ã¨' : 'e',
        'Ã©' : 'e',
        'Ã­' : 'i',
        'Ã¯' : 'i',
        'Ã±' : 'n',
        'Ã³' : 'o',
        'Ã´' : 'o',
        'Ã¶' : 'o',
        'Ã»' : 'u',
        'Ã¼' : 'u',
        'æ' : 'ae',
        'ç' : 'c',
        'è' : 'e',
        'é' : 'e',
        'í' : 'i',
        'ï' : 'i',
        'ñ' : 'n',
        'ó' : 'o',
        'ô' : 'o',
        'ö' : 'o',
        'û' : 'u',
        'ü' : 'u'}


for char_ in replacements.keys():
    sents.sentence = sents.sentence.str.replace(char_,replacements[char_])
    phrs.phrase = phrs.phrase.str.replace(char_,replacements[char_])
    
sents.sentence = sents.sentence.str.lower()
phrs.phrase = phrs.phrase.str.lower()

sents = pd.merge(sents, phrs, left_on = 'sentence', right_on = 'phrase', how = 'left')
sents = sents[~sents['phrase id'].isna()]
sents.drop_duplicates(subset = ['sentence_index'], keep = 'first', inplace = True)
## Target Values
sentiments = pd.read_csv('sentiment_labels.txt', sep = "|")
sents = pd.merge(sents, sentiments, how = 'left', left_on = 'phrase id', right_on = 'phrase ids')

## Train/Test Splits
splts = pd.read_csv('datasetSplit.txt')
sents = pd.merge(sents, splts, on = 'sentence_index', how = 'left')

sents = sents[['sentence','sentiment values', 'splitset_label']]

sents['label5'] = pd.cut(sents['sentiment values'], bins = 5)
sents['label25'] = pd.cut(sents['sentiment values'], bins = 25)

from translate import Translator
german = Translator(from_lang="English",to_lang="german")
english = Translator(from_lang="german",to_lang="English")
# german.translate("Good Morning!")
# english.translate('Guten Morgen')
#
# sents['German'] = sents['sentence'].apply(lambda x:german.translate(x))
# sents['augmented_english'] = sents['German'].apply(lambda x:english.translate(x))

for i in sents.index:
        print(i)
        sents.loc[i, 'german'] = german.translate(sents.loc[i,'sentiment values'])
        sents.loc[i, 'augmented_english'] = german.translate(sents.loc[i, 'german'])