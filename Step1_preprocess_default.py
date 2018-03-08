#encoding="utf8"
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import re
#import nltk
#nltk.download()
import simplejson as json
#import pickle
import emoji
#from emoji.unicode_codes import UNICODE_EMOJI
#import numpy as np

def rm_html_tags(str):
    html_prog = re.compile(r'<[^>]+>',re.S)
    return html_prog.sub('', str)

def rm_html_escape_characters(str):
    pattern_str = r'&quot;|&amp;|&lt;|&gt;|&nbsp;|&#34;|&#38;|&#60;|&#62;|&#160;|&#20284;|&#30524;|&#26684|&#43;|&#20540|&#23612;'
    escape_characters_prog = re.compile(pattern_str, re.S)
    return escape_characters_prog.sub('', str)

def rm_at_user(str):
    return re.sub(r'@[a-zA-Z_0-9]*', '', str)

def rm_url(str):
    return re.sub(r'http[s]?:[/+]?[a-zA-Z0-9_\.\/]*', '', str)

def rm_repeat_chars(str):
    return re.sub(r'(.)(\1){2,}', r'\1\1', str)

def rm_hashtag_symbol(str):
    return re.sub(r'#', '', str)

def rm_time(str):
    return re.sub(r'[0-9][0-9]:[0-9][0-9]', '', str)


# process word to remove line break
def rm_linebreak(str1):
    final_str = ""
    for word in str1.split():
        final_str += " "
        final_str += str(word)
    return final_str
    

def pre_process(str):
    # do not change the preprocessing order only if you know what you're doing 
    str = str.lower()
    str = rm_url(str)        
    str = rm_at_user(str)        
    str = rm_repeat_chars(str) 
    str = rm_hashtag_symbol(str)       
    str = rm_time(str) 
    str = rm_linebreak(str)
        
    return str
                            


if __name__ == "__main__":
    data_dir = './data'  ##Setting your own file path here.

    x_filename = 'tweets.txt'
    y_filename = 'labels.txt'


    ##load and process samples
    print('start loading and process samples...')
    words_stat = {} # record statistics of the df and tf for each word; Form: {word:[tf, df, tweet index]}
    tweets = []
    cnt = 0
    with open(os.path.join(data_dir, x_filename), encoding='utf-8') as f:
        for i, line in enumerate(f):
            tweet_obj = json.loads(line.strip(), encoding='utf-8')
            content = tweet_obj['text'].replace("\n"," ")
            postprocess_tweet = pre_process(content)
            tweets.append( postprocess_tweet )


    ###Re-process samples, filter low frequency words...
    fout = open(os.path.join(data_dir, 'tweets_processed.txt'), 'w', encoding='utf-8')
    for tweet in tweets:
        fout.write('%s\n' %tweet)
    fout.close()

    print("Preprocessing is completed")
    
    