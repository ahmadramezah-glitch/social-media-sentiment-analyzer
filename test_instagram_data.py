#!/usr/bin/env python3
"""
Test script to verify Instagram data fetching with new token
"""

from instagram_api import get_hashtag_id, fetch_recent_posts
from config import INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_USER_ID

def test_instagram_data_fetching():
    """Test Instagram data fetching functionality"""
    print("🔍 Testing Instagram Data Fetching...")
    
    # Test 1: Get hashtag ID
    print("\n1️⃣ Getting hashtag ID for 'mtc'...")
    hashtag_id = get_hashtag_id('mtc', INSTAGRAM_USER_ID, INSTAGRAM_ACCESS_TOKEN)
    
    if hashtag_id:
        print(f"✅ Hashtag ID found: {hashtag_id}")
        
        # Test 2: Fetch posts
        print("\n2️⃣ Fetching posts for hashtag 'mtc'...")
        posts = fetch_recent_posts(hashtag_id, INSTAGRAM_USER_ID, INSTAGRAM_ACCESS_TOKEN)
        
        if posts:
            print(f"✅ Successfully fetched {len(posts)} posts!")
            print("\n📊 Sample posts:")
            for i, post in enumerate(posts[:3]):  # Show first 3 posts
                caption = post.get('caption', 'No caption')[:100]
                timestamp = post.get('timestamp', 'No timestamp')
                likes = post.get('like_count', 0)
                comments = post.get('comments_count', 0)
                print(f"   Post {i+1}: {caption}...")
                print(f"      📅 {timestamp} | ❤️ {likes} | 💬 {comments}")
        else:
            print("❌ No posts fetched")
    else:
        print("❌ Could not get hashtag ID")

if __name__ == "__main__":
    test_instagram_data_fetching() 