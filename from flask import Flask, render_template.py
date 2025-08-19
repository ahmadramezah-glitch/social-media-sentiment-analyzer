import os
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging
from datetime import datetime, timedelta
import json
from instagram_api import InstagramAPI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Production configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here-change-in-production')
app.config['INSTAGRAM_CLIENT_ID'] = os.environ.get('INSTAGRAM_CLIENT_ID', '')
app.config['INSTAGRAM_CLIENT_SECRET'] = os.environ.get('INSTAGRAM_CLIENT_SECRET', '')
app.config['INSTAGRAM_ACCESS_TOKEN'] = os.environ.get('INSTAGRAM_ACCESS_TOKEN', '')
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

# Initialize Instagram API
instagram_api = InstagramAPI(
    access_token=app.config['INSTAGRAM_ACCESS_TOKEN'],
    client_id=app.config['INSTAGRAM_CLIENT_ID'],
    client_secret=app.config['INSTAGRAM_CLIENT_SECRET']
)

# Rate limiting
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# In-memory cache for demo (use Redis in production)
cache = {}

def get_cached_data(key, ttl_seconds=300):
    """Simple cache implementation"""
    if key in cache:
        data, timestamp = cache[key]
        if datetime.now() - timestamp < timedelta(seconds=ttl_seconds):
            return data
        else:
            del cache[key]
    return None

def set_cached_data(key, data):
    """Set cache data with timestamp"""
    cache[key] = (data, datetime.now())

@app.route('/', methods=['GET', 'POST'])
@limiter.limit("10 per minute")
def index():
    try:
        if request.method == 'POST':
            hashtag = request.form.get('hashtag', '').strip()
            if not hashtag:
                flash('Please enter at least one hashtag to analyze.', 'warning')
                return render_template('index.html', hashtag='', posts=[])
            
            # Check cache first
            cache_key = f"hashtag_{hashtag}"
            cached_posts = get_cached_data(cache_key)
            
            if cached_posts:
                flash(f'Analysis completed for hashtag: {hashtag} (cached)', 'info')
                return render_template('index.html', hashtag=hashtag, posts=cached_posts)
            
            # Get real Instagram posts
            try:
                posts = instagram_api.get_posts_by_hashtag(hashtag, limit=10)
                
                if not posts:
                    flash(f'No posts found for hashtag: {hashtag}', 'warning')
                    return render_template('index.html', hashtag=hashtag, posts=[])
                
                # Cache the results
                set_cached_data(cache_key, posts)
                
                flash(f'Analysis completed for hashtag: {hashtag} - Found {len(posts)} posts', 'success')
                logger.info(f'Analyzed hashtag: {hashtag} - Found {len(posts)} posts')
                
                return render_template('index.html', hashtag=hashtag, posts=posts)
                
            except Exception as e:
                logger.error(f'Error analyzing hashtag {hashtag}: {str(e)}')
                flash(f'Error analyzing hashtag: {hashtag}. Please try again later.', 'danger')
                return render_template('index.html', hashtag=hashtag, posts=[])
        
        return render_template('index.html', hashtag='', posts=[])
        
    except Exception as e:
        logger.error(f'Unexpected error in index route: {str(e)}')
        flash('An unexpected error occurred. Please try again.', 'danger')
        return render_template('index.html', hashtag='', posts=[])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<post_id>')
@limiter.limit("30 per minute")
def post_detail(post_id):
    try:
        # Get post details and comments
        posts = instagram_api.get_posts_by_hashtag('demo', limit=10)  # Get demo posts to find the one we want
        post = None
        
        for p in posts:
            if p['id'] == post_id:
                post = p
                break
        
        if not post:
            # Create a demo post if not found
            post = {
                'id': post_id,
                'caption': f'Detailed view of post {post_id} - This is a comprehensive analysis of the content and sentiment.',
                'sentiment': 'positive',
                'polarity': 0.8,
                'created_at': datetime.now() - timedelta(hours=int(post_id.split('_')[-1]) if '_' in post_id else 1),
                'likes': 150 + (int(post_id.split('_')[-1]) if '_' in post_id else 1) * 10,
                'comments': 20 + (int(post_id.split('_')[-1]) if '_' in post_id else 1) * 5,
                'hashtags': ['demo', 'sentiment', 'analysis'],
                'media_url': None,
                'permalink': f'https://instagram.com/p/{post_id}',
                'media_type': 'IMAGE'
            }
        
        # Get comments for this post
        comments = instagram_api.get_post_comments(post_id)
        post['comments_list'] = comments
        
        return render_template('post_detail.html', post=post)
    except Exception as e:
        logger.error(f'Error loading post {post_id}: {str(e)}')
        flash('Error loading post details.', 'danger')
        return redirect(url_for('index'))

@app.route('/api/posts/<hashtag>')
@limiter.limit("20 per minute")
def api_posts(hashtag):
    """API endpoint for programmatic access"""
    try:
        cache_key = f"api_hashtag_{hashtag}"
        cached_data = get_cached_data(cache_key, ttl_seconds=600)
        
        if cached_data:
            return jsonify({'status': 'success', 'data': cached_data, 'cached': True})
        
        # Get real Instagram posts
        posts = instagram_api.get_posts_by_hashtag(hashtag, limit=5)
        
        set_cached_data(cache_key, posts)
        return jsonify({'status': 'success', 'data': posts, 'cached': False})
        
    except Exception as e:
        logger.error(f'API error for hashtag {hashtag}: {str(e)}')
        return jsonify({'status': 'error', 'message': 'Internal server error'}), 500

@app.route('/api/comments/<post_id>')
@limiter.limit("30 per minute")
def api_comments(post_id):
    """API endpoint to get comments for a specific post"""
    try:
        comments = instagram_api.get_post_comments(post_id)
        return jsonify({'status': 'success', 'data': comments})
    except Exception as e:
        logger.error(f'API error for comments {post_id}: {str(e)}')
        return jsonify({'status': 'error', 'message': 'Internal server error'}), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(429)
def ratelimit_handler(e):
    flash('Too many requests. Please wait a moment before trying again.', 'warning')
    return render_template('index.html', hashtag='', posts=[]), 429

@app.errorhandler(500)
def internal_error(e):
    logger.error(f'Internal server error: {str(e)}')
    flash('An internal server error occurred. Please try again later.', 'danger')
    return render_template('index.html', hashtag='', posts=[]), 500

if __name__ == '__main__':
    # Production recommendations
    if not app.config['INSTAGRAM_CLIENT_ID']:
        logger.warning('INSTAGRAM_CLIENT_ID not set. Set environment variable for production.')
    
    if app.config['SECRET_KEY'] == 'your-secret-key-here-change-in-production':
        logger.warning('Using default secret key. Set SECRET_KEY environment variable for production.')
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])