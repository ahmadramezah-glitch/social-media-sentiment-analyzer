#!/usr/bin/env python3
"""
Test Flask app Instagram search functionality
"""

from app import app, db
from models import Post
from instagram_api import get_hashtag_id, fetch_recent_posts
from sentiment import analyze_sentiment
from config import INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_USER_ID
from datetime import datetime

def test_flask_instagram_search():
    """Test Instagram search functionality in Flask app context"""
    with app.app_context():
        print("🔍 Testing Flask Instagram Search Functionality...")
        
        # Test 1: Check if database is empty
        posts_before = Post.query.count()
        print(f"Posts in database before search: {posts_before}")
        
        # Test 2: Simulate Instagram search (like the dashboard route does)
        print("\n2️⃣ Simulating Instagram search for hashtag 'mtc'...")
        
        hashtag = 'mtc'
        
        # Get hashtag ID
        hashtag_id = get_hashtag_id(hashtag, INSTAGRAM_USER_ID, INSTAGRAM_ACCESS_TOKEN)
        
        if hashtag_id:
            print(f"✅ Hashtag ID found: {hashtag_id}")
            
            # Fetch posts
            instagram_posts = fetch_recent_posts(hashtag_id, INSTAGRAM_USER_ID, INSTAGRAM_ACCESS_TOKEN)
            
            if instagram_posts:
                print(f"✅ Fetched {len(instagram_posts)} posts from Instagram API")
                
                # Process posts (like the dashboard route does)
                total_posts_analyzed = 0
                for post in instagram_posts[:10]:  # Process first 10 posts
                    caption = post.get('caption', '')
                    post_id = post.get('id')
                    
                    if caption and post_id:
                        # Analyze sentiment
                        sentiment, polarity = analyze_sentiment(caption)
                        
                        # Check if post already exists
                        existing = Post.query.filter_by(post_id=post_id).first()
                        if not existing:
                            # Create new post
                            new_post = Post(
                                post_id=post_id,
                                caption=caption,
                                sentiment=sentiment,
                                polarity=polarity,
                                hashtag=hashtag,
                                created_at=datetime.now(),
                                source='instagram',
                                media_url=post.get('media_url', ''),
                                permalink=post.get('permalink', ''),
                                like_count=post.get('like_count', 0),
                                comments_count=post.get('comments_count', 0)
                            )
                            
                            db.session.add(new_post)
                            total_posts_analyzed += 1
                
                # Commit to database
                db.session.commit()
                
                print(f"✅ Successfully analyzed and saved {total_posts_analyzed} new posts!")
                
                # Check final count
                posts_after = Post.query.count()
                print(f"Posts in database after search: {posts_after}")
                
                # Show sample posts
                print("\n📊 Sample saved posts:")
                sample_posts = Post.query.order_by(Post.id.desc()).limit(3).all()
                for post in sample_posts:
                    print(f"   - {post.hashtag}: {post.caption[:50]}... ({post.sentiment})")
                
            else:
                print("❌ No posts fetched from Instagram API")
        else:
            print("❌ Could not get hashtag ID")

if __name__ == "__main__":
    test_flask_instagram_search() 