# Configuration Example File
# Copy this file to config.py and fill in your actual API keys and configuration

# Flask Configuration
SECRET_KEY = 'your-secret-key-here'
DEBUG = True

# Database Configuration
DATABASE_URI = 'sqlite:///social_media_analyzer.db'

# API Configuration
TWITTER_BEARER_TOKEN = 'your-twitter-bearer-token-here'
INSTAGRAM_ACCESS_TOKEN = 'your-instagram-access-token-here'
TIKTOK_ACCESS_TOKEN = 'your-tiktok-access-token-here'

# Twitter API Configuration
TWITTER_API_CONFIG = {
    'bearer_token': 'your-twitter-bearer-token-here',
    'wait_on_rate_limit': True,
    'max_results': 100
}

# Instagram API Configuration
INSTAGRAM_API_CONFIG = {
    'access_token': 'your-instagram-access-token-here',
    'api_version': 'v18.0'
}

# TikTok API Configuration
TIKTOK_API_CONFIG = {
    'access_token': 'your-tiktok-access-token-here',
    'api_version': 'v1.3'
}

# Sentiment Analysis Configuration
SENTIMENT_CONFIG = {
    'use_demo_data': True,  # Set to False for production
    'confidence_threshold': 0.6
}

# Demo Data Configuration (for testing)
DEMO_DATA_CONFIG = {
    'enabled': True,
    'max_tweets': 20,
    'max_comments': 5,
    'languages': ['en', 'ar']  # English and Arabic
}

# Application Settings
APP_CONFIG = {
    'name': 'Social Media Sentiment Analyzer',
    'version': '1.3.0',
    'description': 'A comprehensive sentiment analysis tool for social media platforms',
    'author': 'Your Name',
    'contact': 'your.email@example.com'
}

# Security Configuration
SECURITY_CONFIG = {
    'session_timeout': 3600,  # 1 hour in seconds
    'max_login_attempts': 5,
    'password_min_length': 8
}

# Export Configuration
EXPORT_CONFIG = {
    'max_records_per_export': 10000,
    'supported_formats': ['excel', 'pdf'],
    'include_charts': True
}

# Logging Configuration
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': 'app.log'
}

# Cache Configuration
CACHE_CONFIG = {
    'enabled': True,
    'timeout': 300,  # 5 minutes
    'max_size': 1000
}

# Rate Limiting
RATE_LIMIT_CONFIG = {
    'enabled': True,
    'requests_per_minute': 60,
    'burst_size': 10
}

# Demo Twitter Data Structure (Example)
DEMO_TWITTER_DATA = {
    "example_hashtag": [
        {
            "id": "demo_example_1",
            "text": "This is an example tweet for demonstration purposes. #example #demo",
            "name": "Example User",
            "username": "example_user",
            "created_at": "2024-01-15T10:00:00Z",
            "like_count": 100,
            "retweet_count": 50,
            "reply_count": 25,
            "quote_count": 10,
            "sentiment": "positive",
            "source": "twitter",
            "permalink": "https://twitter.com/example_user/status/demo_example_1",
            "comments_count": 3
        }
        # Add more demo tweets as needed
    ]
}

# Demo Instagram Data Structure (Example)
DEMO_INSTAGRAM_DATA = {
    "example_hashtag": [
        {
            "id": "demo_instagram_1",
            "caption": "This is an example Instagram post for demonstration. #example #instagram",
            "username": "example_instagram_user",
            "created_at": "2024-01-15T10:00:00Z",
            "like_count": 150,
            "comment_count": 30,
            "sentiment": "positive",
            "source": "instagram",
            "media_url": "https://example.com/media/demo_instagram_1.jpg"
        }
        # Add more demo posts as needed
    ]
}

# Demo TikTok Data Structure (Example)
DEMO_TIKTOK_DATA = {
    "example_hashtag": [
        {
            "id": "demo_tiktok_1",
            "description": "This is an example TikTok video for demonstration. #example #tiktok",
            "username": "example_tiktok_user",
            "created_at": "2024-01-15T10:00:00Z",
            "like_count": 200,
            "comment_count": 40,
            "share_count": 20,
            "sentiment": "positive",
            "source": "tiktok",
            "video_url": "https://example.com/video/demo_tiktok_1.mp4"
        }
        # Add more demo videos as needed
    ]
}

# User Roles and Permissions
USER_ROLES = {
    'admin': {
        'permissions': ['can_view_all', 'can_edit_users', 'can_export_data', 'can_view_database'],
        'description': 'Full access to all features'
    },
    'advisor': {
        'permissions': ['can_view_filtered_results', 'can_export_data', 'can_view_database'],
        'description': 'Access to view and export data'
    },
    'user': {
        'permissions': ['can_view_basic'],
        'description': 'Basic access to view results'
    }
}

# Default User Configuration
DEFAULT_USERS = [
    {
        'username': 'admin',
        'password': 'admin123',  # Change this in production!
        'role': 'admin',
        'email': 'admin@example.com'
    },
    {
        'username': 'advisor',
        'password': 'advisor123',  # Change this in production!
        'role': 'advisor',
        'email': 'advisor@example.com'
    }
]

# Feature Flags
FEATURES = {
    'twitter_analysis': True,
    'instagram_analysis': True,
    'tiktok_analysis': True,
    'sentiment_analysis': True,
    'data_export': True,
    'user_management': True,
    'platform_filtering': True,
    'demo_data': True
}

# Performance Configuration
PERFORMANCE_CONFIG = {
    'max_concurrent_requests': 10,
    'request_timeout': 30,
    'cache_enabled': True,
    'compression_enabled': True
}

# Error Handling
ERROR_CONFIG = {
    'log_errors': True,
    'show_detailed_errors': False,  # Set to False in production
    'custom_error_pages': True
}

# Backup Configuration
BACKUP_CONFIG = {
    'enabled': True,
    'frequency': 'daily',
    'retention_days': 30,
    'include_database': True,
    'include_logs': True
}

# Monitoring Configuration
MONITORING_CONFIG = {
    'enabled': True,
    'health_check_interval': 300,  # 5 minutes
    'performance_metrics': True,
    'error_tracking': True
}

# Development vs Production
ENVIRONMENT = 'development'  # Change to 'production' when deploying

if ENVIRONMENT == 'production':
    DEBUG = False
    SECURITY_CONFIG['session_timeout'] = 1800  # 30 minutes
    ERROR_CONFIG['show_detailed_errors'] = False
    FEATURES['demo_data'] = False
    LOGGING_CONFIG['level'] = 'WARNING'
else:
    DEBUG = True
    FEATURES['demo_data'] = True
    LOGGING_CONFIG['level'] = 'DEBUG'
