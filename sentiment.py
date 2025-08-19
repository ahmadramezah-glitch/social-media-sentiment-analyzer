import re
import arabic_reshaper
from bidi.algorithm import get_display
import emoji
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob


# Arabic & English Sentiment Words
ARABIC_POSITIVE_WORDS = {
    'ممتاز', 'رائع', 'جميل', 'عظيم', 'مذهل', 'مفيد', 'جيد', 'حلو', 'لذيذ', 'مريح',
    'سعيد', 'فرحان', 'مبسوط', 'متحمس', 'مشجع', 'ممتازة', 'رائعة', 'جميلة', 'عظيمة',
    'مذهلة', 'مفيدة', 'جيدة', 'حلوة', 'لذيذة', 'مريحة', 'سعيدة', 'فرحانة', 'مبسوطة',
    'متحمسة', 'مشجعة', 'أفضل', 'أحسن', 'أجمل', 'أروع', 'أمتع', 'ألذ', 'أحلى',
    'سريع', 'سريعة', 'أسرع', 'أسرع', 'بيناسب', 'مناسب', 'مناسبة', 'أفضل', 'أحسن',
    'ممتاز', 'رائع', 'جميل', 'عظيم', 'مذهل', 'مفيد', 'جيد', 'حلو', 'لذيذ', 'مريح',
    'excellent', 'amazing', 'great', 'good', 'wonderful', 'fantastic', 'awesome',
    'beautiful', 'nice', 'perfect', 'love', 'like', 'enjoy', 'happy', 'excited',
    'brilliant', 'outstanding', 'superb', 'magnificent', 'splendid', 'marvelous',
    'delightful', 'pleasing', 'satisfying', 'enjoyable', 'pleasurable', 'grateful',
    'thankful', 'blessed', 'fortunate', 'lucky', 'successful', 'winning', 'victorious',
    'fast', 'fastest', 'quick', 'quickest', 'speedy', 'rapid', 'swift', 'efficient',
    'convenient', 'suitable', 'appropriate', 'ideal', 'perfect', 'best', 'optimal',
    'affordable', 'cheap', 'inexpensive', 'reasonable', 'value', 'deal', 'offer',
    'service', 'broadband', 'wifi', 'internet', 'connection', 'available', 'ready'
}

ARABIC_NEGATIVE_WORDS = {
    'سيء', 'رديء', 'مزعج', 'مؤلم', 'مخيب', 'سيئة', 'رديئة', 'مزعجة', 'مؤلمة',
    'مخيبة', 'أسوأ', 'أردأ', 'أمزعج', 'أمؤلم', 'أمخيب', 'مكروه', 'مبغوض', 'مقرف',
    'مقزز', 'مثير للاشمئزاز', 'مخجل', 'مخز', 'مخيب للأمل', 'محبط', 'محبطة',
    'bad', 'terrible', 'awful', 'horrible', 'disgusting', 'hate', 'dislike',
    'annoying', 'frustrating', 'disappointing', 'sad', 'angry', 'upset', 'dreadful',
    'atrocious', 'appalling', 'revolting', 'repulsive', 'nauseating', 'sickening',
    'offensive', 'insulting', 'humiliating', 'embarrassing', 'shameful', 'disgraceful',
    'unpleasant', 'uncomfortable', 'painful', 'hurtful', 'harmful', 'damaging',
    'destructive', 'ruinous', 'catastrophic', 'devastating', 'crushing', 'overwhelming'
}

# Emoji sentiment score dictionary
EMOJI_SENTIMENT = {
    # Very Positive
    '😍': 1.0, '🥰': 1.0, '❤️': 1.0, '💖': 1.0, '💕': 1.0, '💗': 1.0, '💓': 1.0,
    '🤩': 0.9, '😊': 0.9, '😁': 0.9, '😄': 0.9, '🙌': 0.9, '👏': 0.9, '🎉': 0.9,
    
    # Positive
    '😊': 0.8, '😂': 0.8, '😎': 0.8, '👍': 0.8, '😃': 0.8, '😆': 0.8, '😉': 0.8,
    '😋': 0.8, '😌': 0.8, '😇': 0.8, '🤗': 0.8, '🤔': 0.6, '🤓': 0.7, '😏': 0.5,
    
    # Neutral
    '😐': 0.0, '😑': 0.0, '😶': 0.0, '🤐': 0.0, '😯': 0.0, '😦': 0.0, '😧': 0.0,
    '😮': 0.0, '😲': 0.0, '😴': 0.0, '🤤': 0.0, '😪': 0.0, '😵': 0.0, '🤢': 0.0,
    
    # Negative
    '😢': -0.6, '😞': -0.6, '😔': -0.6, '😩': -0.6, '😤': -0.6, '😣': -0.6,
    '😖': -0.6, '😫': -0.6, '😓': -0.6, '😥': -0.6, '😰': -0.6, '😨': -0.6,
    
    # Very Negative
    '😡': -0.9, '😠': -0.9, '😤': -0.9, '😭': -0.9, '👎': -0.9, '💔': -1.0,
    '😈': -0.8, '👿': -0.8, '😱': -0.8, '😨': -0.8, '😰': -0.8, '😥': -0.8,
    
    # Additional positive emojis
    '✨': 0.8, '🌟': 0.8, '💫': 0.8, '⭐': 0.8, '🔥': 0.8, '💯': 0.9, '💪': 0.8,
    '🏆': 0.9, '🎯': 0.8, '🎊': 0.8, '🎈': 0.7, '🎁': 0.8, '🎂': 0.7, '🍰': 0.7,
    
    # Additional negative emojis
    '💩': -0.8, '👻': -0.3, '☠️': -0.9, '💀': -0.8, '👹': -0.8, '👺': -0.8,
    '😈': -0.8, '👿': -0.8, '🤡': -0.5, '👽': -0.3, '🤖': -0.2, '👾': -0.2
}

# Initialize sentiment analyzers
vader_analyzer = None
try:
    # Try to initialize VADER analyzer without downloading
    vader_analyzer = SentimentIntensityAnalyzer()
    print("NLTK sentiment analyzer loaded successfully!")
except Exception as e:
    print(f"Error loading NLTK: {e}")
    vader_analyzer = None

# Initialize sentiment analyzer
sentiment_analyzer = None

# Simple sentiment analysis using keyword matching
def advanced_sentiment_analysis(text):
    """Advanced sentiment analysis using NLTK VADER and TextBlob for comprehensive word understanding"""
    if not text:
        return "neutral", 0.0
    
    # Clean the text
    cleaned_text = clean_text(text)
    if not cleaned_text:
        return "neutral", 0.0
    
    # Initialize scores
    vader_score = 0.0
    textblob_score = 0.0
    emoji_score = 0.0
    emoji_count = 0
    keyword_score = 0.0
    
    # Analyze emojis first
    for emoji_char, score in EMOJI_SENTIMENT.items():
        if emoji_char in text:
            emoji_score += score
            emoji_count += 1
    
    # Calculate average emoji sentiment if emojis found
    if emoji_count > 0:
        emoji_score = emoji_score / emoji_count
    
    # Analyze keywords for Arabic and English
    text_lower = text.lower()
    positive_count = 0
    negative_count = 0
    
    # Check for positive keywords
    for word in ARABIC_POSITIVE_WORDS:
        if word.lower() in text_lower:
            positive_count += 1
    
    # Check for negative keywords
    for word in ARABIC_NEGATIVE_WORDS:
        if word.lower() in text_lower:
            negative_count += 1
    
    # Calculate keyword score
    if positive_count > 0 or negative_count > 0:
        keyword_score = (positive_count - negative_count) / max(positive_count + negative_count, 1)
        keyword_score = max(-0.9, min(0.9, keyword_score))
    
    # Use NLTK VADER for English text analysis
    if vader_analyzer:
        try:
            vader_scores = vader_analyzer.polarity_scores(cleaned_text)
            vader_score = vader_scores['compound']  # Compound score ranges from -1 to 1
        except Exception as e:
            print(f"VADER analysis error: {e}")
            vader_score = 0.0
    
    # Use TextBlob for additional analysis
    try:
        blob = TextBlob(cleaned_text)
        textblob_score = blob.sentiment.polarity  # Ranges from -1 to 1
    except Exception as e:
        print(f"TextBlob analysis error: {e}")
        textblob_score = 0.0
    
    # Combine scores with weights
    # VADER: 30%, TextBlob: 25%, Emojis: 25%, Keywords: 20%
    combined_score = (vader_score * 0.3) + (textblob_score * 0.25) + (emoji_score * 0.25) + (keyword_score * 0.2)
    
    # Context-aware adjustments for promotional content
    text_lower = text.lower()
    
    # Check for promotional indicators (positive boost)
    promotional_indicators = [
        'fastest', 'best', 'perfect', 'ideal', 'optimal', 'excellent', 'amazing',
        'great', 'wonderful', 'fantastic', 'awesome', 'brilliant', 'outstanding',
        'superb', 'magnificent', 'splendid', 'marvelous', 'delightful', 'pleasing',
        'satisfying', 'enjoyable', 'pleasurable', 'grateful', 'thankful', 'blessed',
        'fortunate', 'lucky', 'successful', 'winning', 'victorious', 'fast', 'quick',
        'speedy', 'rapid', 'swift', 'efficient', 'convenient', 'suitable', 'appropriate',
        'affordable', 'cheap', 'inexpensive', 'reasonable', 'value', 'deal', 'offer',
        'service', 'broadband', 'wifi', 'internet', 'connection', 'available', 'ready',
        'سريع', 'سريعة', 'أسرع', 'بيناسب', 'مناسب', 'مناسبة', 'أفضل', 'أحسن', 'ممتاز',
        'رائع', 'جميل', 'عظيم', 'مذهل', 'مفيد', 'جيد', 'حلو', 'لذيذ', 'مريح'
    ]
    
    promotional_count = sum(1 for word in promotional_indicators if word in text_lower)
    if promotional_count > 0:
        # Boost positive sentiment for promotional content
        combined_score += (promotional_count * 0.1)
        combined_score = min(0.9, combined_score)  # Cap at 0.9
    
    # Determine sentiment and polarity
    if combined_score > 0.05:  # Lowered threshold for positive
        sentiment = "positive"
        polarity = min(0.9, combined_score)
    elif combined_score < -0.05:  # Lowered threshold for negative
        sentiment = "negative"
        polarity = max(-0.9, combined_score)
    else:
        sentiment = "neutral"
        polarity = 0.0
    
    return sentiment, polarity

def simple_sentiment_analysis(text):
    """Fallback sentiment analysis using keyword matching and emoji analysis"""
    if not text:
        return "neutral", 0.0
    
    text_lower = text.lower()
    
    # Positive keywords
    positive_words = ['good', 'great', 'amazing', 'excellent', 'wonderful', 'fantastic', 'love', 'like', 'awesome', 'perfect', 'best', 'beautiful', 'nice', 'happy', 'joy', 'excited', 'wow', 'ممتاز', 'رائع', 'جميل', 'عظيم', 'مذهل']
    
    # Negative keywords  
    negative_words = ['bad', 'terrible', 'awful', 'hate', 'dislike', 'worst', 'horrible', 'disappointing', 'sad', 'angry', 'frustrated', 'upset', 'سيء', 'مخيب', 'مزعج', 'محبط']
    
    # Count keyword matches
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)
    
    # Analyze emojis
    emoji_score = 0.0
    emoji_count = 0
    
    for emoji_char, score in EMOJI_SENTIMENT.items():
        if emoji_char in text:
            emoji_score += score
            emoji_count += 1
    
    # Calculate average emoji sentiment if emojis found
    if emoji_count > 0:
        emoji_score = emoji_score / emoji_count
        # Convert emoji score to count (positive emojis add to positive count, negative to negative)
        if emoji_score > 0:
            positive_count += abs(emoji_score) * 2  # Weight emojis more heavily
        elif emoji_score < 0:
            negative_count += abs(emoji_score) * 2
    
    # Calculate sentiment
    if positive_count > negative_count:
        sentiment = "positive"
        polarity = min(0.9, positive_count / 8)  # Adjusted for emoji influence
    elif negative_count > positive_count:
        sentiment = "negative" 
        polarity = max(-0.9, -negative_count / 8)
    else:
        sentiment = "neutral"
        polarity = 0.0
    
    return sentiment, polarity

def clean_text(text):
    """Clean and normalize text for sentiment analysis"""
    if not text:
        return ""
    
    # Convert to string if not already
    text = str(text)
    
    # Handle Arabic text
    text = arabic_reshaper.reshape(text)
    text = get_display(text)
    
    # Keep emojis for sentiment analysis (don't demojize)
    # text = emoji.demojize(text)  # Commented out to preserve emojis
    
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    
    # Remove hashtags but keep the text
    text = re.sub(r'#(\w+)', r'\1', text)
    
    # Remove mentions
    text = re.sub(r'@(\w+)', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def analyze_sentiment(text):
    """Analyze sentiment using advanced analysis and return sentiment and polarity score"""
    try:
        # Clean the text
        cleaned_text = clean_text(text)
        
        if not cleaned_text:
            return "neutral", 0.0
        
        # Try advanced analysis first (NLTK + TextBlob + Emojis)
        if vader_analyzer:
            sentiment, polarity = advanced_sentiment_analysis(text)
        else:
            # Fallback to simple analysis
            sentiment, polarity = simple_sentiment_analysis(cleaned_text)
        
        return sentiment, polarity
        
    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        return "neutral", 0.0

def get_sentiment_confidence(text):
    """Get sentiment confidence score for visualization"""
    try:
        cleaned_text = clean_text(text)
        if not cleaned_text:
            return 0.0
        
        # Use the same analysis method as analyze_sentiment
        if vader_analyzer:
            sentiment, polarity = advanced_sentiment_analysis(text)
        else:
            sentiment, polarity = simple_sentiment_analysis(cleaned_text)
        
        return abs(polarity)
        
    except Exception as e:
        print(f"Error getting sentiment confidence: {e}")
        return 0.0

def get_sentiment_color(sentiment, confidence=1.0):
    """Get color for sentiment visualization"""
    if sentiment == "positive":
        return f"rgba(34, 197, 94, {confidence})"  # Green
    elif sentiment == "negative":
        return f"rgba(239, 68, 68, {confidence})"  # Red
    else:
        return f"rgba(156, 163, 175, {confidence})"  # Gray

def get_sentiment_bar_width(polarity):
    """Convert polarity to bar width percentage"""
    # Convert polarity (-1 to 1) to percentage (0 to 100)
    return abs(polarity) * 100
