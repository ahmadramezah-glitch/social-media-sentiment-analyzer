from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Role-based permissions
    can_view_dashboard = db.Column(db.Boolean, default=True)
    can_view_graphs = db.Column(db.Boolean, default=True)
    can_search_hashtags = db.Column(db.Boolean, default=True)
    can_view_filtered_results = db.Column(db.Boolean, default=True)
    can_view_all_posts = db.Column(db.Boolean, default=True)
    can_manage_users = db.Column(db.Boolean, default=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def has_permission(self, permission):
        """Check if user has a specific permission"""
        if self.is_admin:
            return True
        return getattr(self, permission, False)
    
    def get_role_name(self):
        """Get human-readable role name"""
        if self.is_admin:
            return "Admin"
        elif self.can_manage_users:
            return "Manager"
        elif self.can_view_all_posts and self.can_search_hashtags:
            return "Analyst"
        elif self.can_view_graphs and self.can_view_filtered_results:
            return "Viewer"
        else:
            return "Basic User"
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'is_admin': self.is_admin,
            'is_active': self.is_active,
            'role': self.get_role_name(),
            'permissions': {
                'can_view_dashboard': self.can_view_dashboard,
                'can_view_graphs': self.can_view_graphs,
                'can_search_hashtags': self.can_search_hashtags,
                'can_view_filtered_results': self.can_view_filtered_results,
                'can_view_all_posts': self.can_view_all_posts,
                'can_manage_users': self.can_manage_users
            },
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.String(100), unique=True, nullable=False)  # Changed from insta_post_id
    caption = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String(20), nullable=False)
    polarity = db.Column(db.Float, nullable=False)
    hashtag = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Source tracking (Instagram, Twitter, or TikTok)
    source = db.Column(db.String(20), default='instagram')
    
    # Additional Instagram post information
    media_url = db.Column(db.String(500), nullable=True)
    permalink = db.Column(db.String(500), nullable=True)
    like_count = db.Column(db.Integer, default=0)
    comments_count = db.Column(db.Integer, default=0)
    
    # TikTok specific fields
    video_url = db.Column(db.String(500), nullable=True)
    video_transcript = db.Column(db.Text, nullable=True)
    video_duration = db.Column(db.Integer, default=0)  # in seconds
    detected_language = db.Column(db.String(10), nullable=True)  # Language code (e.g., 'en', 'ar', 'fr')
    
    # Twitter specific fields
    tweet_text = db.Column(db.Text, nullable=True)
    author_username = db.Column(db.String(100), nullable=True)
    retweet_count = db.Column(db.Integer, default=0)
    reply_count = db.Column(db.Integer, default=0)
    
    # Overall sentiment including comments
    overall_sentiment = db.Column(db.String(20), nullable=True)
    overall_polarity = db.Column(db.Float, nullable=True)
    
    def __repr__(self):
        return f'<Post {self.post_id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'post_id': self.post_id,
            'caption': self.caption,
            'sentiment': self.sentiment,
            'polarity': self.polarity,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'source': self.source,
            'media_url': self.media_url,
            'permalink': self.permalink,
            'like_count': self.like_count,
            'comments_count': self.comments_count
        }
    
    def get_overall_sentiment(self):
        """Calculate overall sentiment including comments if available"""
        if self.overall_sentiment:
            return self.overall_sentiment
        return self.sentiment
    
    def get_overall_polarity(self):
        """Get overall polarity including comments if available"""
        if self.overall_polarity is not None:
            return self.overall_polarity
        return self.polarity


class Comment(db.Model):
    """Model for storing comments on posts"""
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    comment_text = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String(20), nullable=False)
    polarity = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    post = db.relationship('Post', backref=db.backref('comments', lazy=True))
    
    def __repr__(self):
        return f'<Comment {self.id} on Post {self.post_id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'post_id': self.post_id,
            'comment_text': self.comment_text,
            'sentiment': self.sentiment,
            'polarity': self.polarity,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }