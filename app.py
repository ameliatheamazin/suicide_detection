from json import load
from flask import Flask, render_template, request,url_for, redirect
import pandas as pd
import numpy as np
import re
import string 
import pickle
import joblib
import nltk
import sklearn
from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import contractions
from sklearn import feature_extraction, model_selection
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.ensemble import RandomForestClassifier

app=Flask(__name__)
all_tweets=[]

#Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.ejs'), 404

#Main Page
@app.route("/") 
def home_page():
    risk_values = [tweet.get('risk_level') for tweet in all_tweets]
    risk_totals=get_risk_totals()
    return render_template('index.ejs',all_tweets=all_tweets, risk_values=risk_values,risk_totals=risk_totals)

@app.route('/',methods = ['POST', 'GET'])
def predict():
    result=-1
    all_tweets=[]
    all_features=pd.DataFrame()
    model=pickle.load(open('model-final.pkl','rb'))
    #nltk.download('omw-1.4')
    if request.method=='POST':
        data=request.form['tweet']
        
        ##preprocessing steps
        cleaned_data=clean(data)
        if (len(cleaned_data) == 0 or cleaned_data.isspace()):
            result=[0]
        else:
            cleaned_token=word_lemmatizer(cleaned_data)
            cleaned_text=combine_clean_text(cleaned_token)
            tagged=pos_tag_features(cleaned_token)
            tagged=np.reshape(tagged, (1, 35))
            all_features = pd.DataFrame(tagged,columns=["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS", "MD", 
                        "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$","RB", "RBR", "RBS", "RP", "TO", "UH",
                        "VB", "VBD", "VBG","VBN", "VBP","VBZ", "WDT", "WP", "WP$","WRB"])
            all_features.to_csv('f1.csv')           
            all_features['sentiment']=extract_sentiment(cleaned_text)    
            # print(all_features['sentiment'])    
            # tf_idf = tfidf.transform([cleaned_text]).toarray()
            tf_idf_df=extract_tf_idf(cleaned_text)

            #final feature set
            all_features=all_features.merge(tf_idf_df,left_index=True,right_index=True)
            # print(all_features)
            #model prediction
            result = model.predict(all_features.values)
        print(result)
        
        #prepare data to be passed back
        all_tweets=store_tweet(data,result)
        tweetID=all_tweets[-1]['id']
        risk_values = [tweet.get('risk_level') for tweet in all_tweets]
        risk_totals=get_risk_totals()
        # print(all_tweets)
        return render_template('index.ejs',result=result,all_tweets=all_tweets,showResultModal=True,tweetID=tweetID, risk_values=risk_values,risk_totals=risk_totals)
        
    return render_template('index.ejs')

@app.route('/<int:id>',methods = ['PUT','GET'])
def set_action(id):
    if request.method=='GET':
        print(request.args.get('action'))
        action=request.args.get('action')
        global all_tweets
        #print(len(all_tweets))
        all_tweets[id-1]['action']=int(action)
        # print(all_tweets)
        risk_values = [tweet.get('risk_level') for tweet in all_tweets]
        risk_totals=get_risk_totals()
    return render_template('index.ejs',all_tweets=all_tweets,showInfoModal=True,tweetID=id, risk_values=risk_values,risk_totals=risk_totals)

def get_risk_totals():
     global all_tweets
     risk_totals=[]
     risk_totals.append(sum(tweet.get('risk_level')==0 for tweet in all_tweets))
     risk_totals.append(sum(tweet.get('risk_level')==1 for tweet in all_tweets))
     risk_totals.append(sum(tweet.get('risk_level')==2 for tweet in all_tweets))
     return risk_totals

def store_tweet(tweet, result):
    global all_tweets
    tweet_data={
        "id": len(all_tweets)+1,
        "content":tweet,
        "author":"helensmith",
        "date_time":"2022-07-08 18:37:12",
        "location":"-105.109815, 39.614151",
        "risk_level":result[0],
        "action":-1 
    }
   
    all_tweets.append(tweet_data)
    return all_tweets
    
#Data preprocessing- Removal of redundant words and characters
def clean(tweet): 
    #convert to lowercase
    tweet = tweet.lower() #Convert strings in the Series/Index to lowercase.       
    
    #remove username tag
    tweet = re.sub('@[\w]+','',tweet)
    
    #remove all apecial characters
    tweet = re.sub(r"â€™", "'", tweet)
    tweet = re.sub(r"ðŸ™„", "", tweet)
    tweet = re.sub(r"ðŸ˜‚", "", tweet)
    tweet = re.sub(r"ðŸ¤­", "", tweet)
    tweet = re.sub(r"amp;", "", tweet)
    tweet = re.sub(r"ðŸ‘ðŸ» ", "", tweet)
    tweet = re.sub(r"¦", "", tweet)
    tweet = re.sub(r"â€", "", tweet)
    tweet = re.sub(r"ðŸ‘ŽðŸ½", "", tweet)
    tweet = re.sub(r"@ ", "", tweet)
    tweet = re.sub(r"ðŸ‘¿", "", tweet)
    tweet = re.sub(r"ðŸ˜¶â€ðŸŒ«ï¸", "", tweet)
    tweet = re.sub(r"ðŸ˜”", "", tweet)
    tweet = re.sub(r"ðŸ‘¿", "", tweet)
    tweet = re.sub(r"ðŸ˜ƒ", "", tweet)
    tweet = re.sub(r"â€œ", "", tweet)
    tweet = re.sub(r"ðŸ˜", "", tweet)
    tweet = re.sub(r"ðŸ˜­â¤", "", tweet)
    tweet = re.sub(r"ðŸ˜¢ðŸ’”", "", tweet)
    tweet = re.sub(r"ðŸ’°", "", tweet)
    tweet = re.sub(r"ðŸ’–", "", tweet)
    tweet = re.sub(r"â€”", "", tweet)
    tweet = re.sub(r"ðŸ¤ª", "", tweet)
    tweet = re.sub(r"ðŸŽµ", "", tweet)
    tweet = re.sub(r"ðŸ™ðŸ¼", "", tweet)
    tweet = re.sub(r"ðŸ˜«", "", tweet)
    tweet = re.sub(r"â€”", "", tweet)
    tweet = re.sub(r"ðŸ¤ª", "", tweet)
    tweet = re.sub(r"ðŸŽµ", "", tweet)
    tweet = re.sub(r"ðŸ™ðŸ¼", "", tweet)
    tweet = re.sub(r"ðŸ˜«", "", tweet)
    tweet = re.sub(r"ðŸ’¯ âœŒï¸", "", tweet)
    tweet = re.sub(r"ðŸ¥¹", "", tweet)
    tweet = re.sub(r"ðŸ˜¢", "", tweet)
    tweet = re.sub(r"â˜¹ï¸", "", tweet)
    tweet = re.sub(r"â€ðŸ˜", "", tweet)
    tweet = re.sub(r"ðŸ’€", "", tweet)
    tweet = re.sub(r"ðŸš¨ðŸ’¥BQQQQMðŸ’¥ðŸš¨ @ : ", "", tweet)
    tweet = re.sub(r"ÙÙ‚Ù†", "", tweet)
    tweet = re.sub(r"Ã°Å¸ËœÂ¶ÂÃ°Å¸Å’Â«Ã¯Â¸Â", "", tweet)
    tweet = re.sub(r"Å“", "", tweet)
    tweet = re.sub(r"Â", "", tweet)
    tweet = re.sub(r"Â", "", tweet)
    tweet = re.sub(r"Ã°Å¸â€™â€¢Ã°Å¸â„¢ÂÃ°Å¸ÂÂ½ ", "", tweet)
    tweet = re.sub(r"Ã°Å¸ËœÂ", "", tweet)
    tweet = re.sub(r"Ã°Å¸â„¢Â", "", tweet)
    tweet = re.sub(r"tÃƒÂ´", "", tweet)
    tweet = re.sub(r"Ã°Å¸Â¤Â£Ã°Å¸Â«Â¤ ", "", tweet)
    tweet = re.sub(r"Ã°Å¸ËœÂ­ ", "", tweet)
    tweet = re.sub(r"Ã°Å¸Å’Â", "", tweet)
    tweet = re.sub(r"ðŸ", "", tweet)
    tweet = re.sub(r"ðÿ‘\x8dðÿ\x8f»", "", tweet)
    tweet = re.sub(r"â€", "", tweet)
    
    #remove all contractions
    tweet = contractions.fix(tweet)
    
    #remove url links
    tweet = re.sub(r'https?:\\', '', tweet)
    tweet = re.sub(r'www.', '', tweet)
    
    #remove words with punctuations and special characters
    tweet = re.sub('[%s]' % re.escape(string.punctuation), ' ', tweet)
        
    # remove unnecessary ... and ..
    tweet = tweet.replace('...', '')
    if '...' not in tweet:
        tweet = tweet.replace('..', '')   
    
    #remove numbers
    tweet = re.sub(r"\d+", "",tweet)
    
    #remove whitespace
    tweet=re.sub("\s\s+" , " ", tweet)
    
    return tweet  

def word_lemmatizer(text):
    text=word_tokenize(text) #tokenize the text first
    lem_text = [WordNetLemmatizer().lemmatize(i,'v') for i in text] #lemmatize with emphasis on verbs
    return lem_text

#detokenize the lemmatized output
def combine_clean_text(text):
    combine_text = TreebankWordDetokenizer().detokenize(text)
    return combine_text

#pos tagging
def pos_tag_features(tweet: str):
    pos_tags = ["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS", "MD", 
                "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$","RB", "RBR", "RBS", "RP", "TO", "UH",
                "VB", "VBD", "VBG","VBN", "VBP","VBZ", "WDT", "WP", "WP$","WRB"]
    
    tags = pos_tag(tweet)
    tag_list= list()
    
    for tag in pos_tags:
        tag_list.append(len([i[0] for i in tags if i[1] == tag]))
    
    return tag_list

#Extract Sentiment Score
def extract_sentiment(full_text):
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(full_text) #for each sentence in training set, compute the polarity score
    score=score['compound'] #score derived from normalizing the degree of positives, negatives and neural in the sentence

    return score

def extract_tf_idf(cleaned_text):
    tfidf=pickle.load(open('tfidf-final.pkl','rb'))
    tf_idf = tfidf.transform([cleaned_text]).toarray()
    tf_idf_df=pd.DataFrame(tf_idf,columns=tfidf.get_feature_names_out())
    return tf_idf_df

if __name__=="__main__":
    app.run(debug=True) 