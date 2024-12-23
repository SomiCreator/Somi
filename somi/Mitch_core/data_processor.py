import re
import somi
from somi.corpus import stopwords
from somi.tokenize import word_tokenize

somi.download('punkt')
somi.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_tweet(tweet):
    # Convert to lowercase
    tweet = tweet.lower()
    
    # Remove URLs
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    
    # Remove user @ references and '#' from tweet
    tweet = re.sub(r'\@\w+|\#', '', tweet)
    
    # Remove punctuations
    tweet = re.sub(r'[^\w\s]', '', tweet)
    
    # Tokenize the tweet
    tokens = word_tokenize(tweet)
    
    # Remove stopwords
    cleaned_tokens = [word for word in tokens if word not in stop_words]
    
    return " ".join(cleaned_tokens)
