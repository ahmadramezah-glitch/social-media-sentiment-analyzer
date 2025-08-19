#!/usr/bin/env python3
"""
Demo data generator for testing the sentiment analysis application
"""

from app import app, db
from models import Post, User
from sentiment import analyze_sentiment
from datetime import datetime, timedelta
import random

def generate_demo_data():
    """Generate demo posts for testing"""
    with app.app_context():
        print("🎯 Generating demo data...")
        
        # Sample hashtags and captions
        hashtags = ['mtc', 'tech', 'ai', 'programming', 'innovation']
        
        sample_captions = [
            "Amazing new technology! This is incredible! 🚀 #innovation",
            "Great day at the conference, learned so much! 😊",
            "Working on some exciting new features today! 💻",
            "This project is turning out really well! 👍",
            "Love working with this team! Such great collaboration! ❤️",
            "New breakthrough in our research! 🎉",
            "Customer feedback has been overwhelmingly positive! 🌟",
            "Team meeting went fantastic today! 🎯",
            "Product launch was a huge success! 🚀",
            "Innovation never stops! Always pushing boundaries! 💪",
            "This is really frustrating, nothing is working 😤",
            "Terrible experience with the service today 😞",
            "Why is this so complicated? 😫",
            "Not happy with the results at all 😠",
            "This is a complete disaster! 😡",
            "Neutral observation about the current situation 📊",
            "Just checking the status of things 🔍",
            "Regular update on the project 📈",
            "Standard procedure being followed 📋",
            "Normal day at the office 🏢"
        ]
        
        # Generate posts for the last 3 months
        total_posts = 0
        for i in range(50):  # Generate 50 demo posts
            # Random date within last 3 months
            days_ago = random.randint(0, 90)
            created_at = datetime.now() - timedelta(days=days_ago)
            
            # Random hashtag
            hashtag = random.choice(hashtags)
            
            # Random caption
            caption = random.choice(sample_captions)
            
            # Analyze sentiment
            sentiment, polarity = analyze_sentiment(caption)
            
            # Create post
            post = Post(
                post_id=f"demo_{i}_{hashtag}",
                caption=caption,
                sentiment=sentiment,
                polarity=polarity,
                hashtag=hashtag,
                created_at=created_at,
                source='instagram',
                media_url='',
                permalink='',
                like_count=random.randint(0, 100),
                comments_count=random.randint(0, 20)
            )
            
            db.session.add(post)
            total_posts += 1
        
        # Generate some Facebook posts too
        facebook_captions = [
            "Great community engagement today! 👥",
            "Exciting news to share with everyone! 📢",
            "Thank you for all the support! 🙏",
            "New features coming soon! Stay tuned! 🔔",
            "Amazing feedback from our users! 🌟"
        ]
        
        for i in range(20):  # Generate 20 Facebook posts
            days_ago = random.randint(0, 60)
            created_at = datetime.now() - timedelta(days=days_ago)
            
            caption = random.choice(facebook_captions)
            sentiment, polarity = analyze_sentiment(caption)
            
            post = Post(
                post_id=f"fb_demo_{i}",
                caption=caption,
                sentiment=sentiment,
                polarity=polarity,
                hashtag='facebook',
                created_at=created_at,
                source='facebook',
                media_url='',
                permalink='',
                like_count=random.randint(0, 50),
                comments_count=random.randint(0, 10)
            )
            
            db.session.add(post)
            total_posts += 1
        
        # Commit all posts
        db.session.commit()
        
        print(f"✅ Generated {total_posts} demo posts!")
        print("📊 Demo data includes:")
        print(f"   - Instagram posts: {50} posts")
        print(f"   - Facebook posts: {20} posts")
        print(f"   - Hashtags: {', '.join(hashtags)}")
        print(f"   - Date range: Last 3 months")
        
        return total_posts

if __name__ == "__main__":
    generate_demo_data() 