#!/usr/bin/env python3
"""
Clear demo data to test with real Instagram data
"""

from app import app, db
from models import Post

def clear_demo_data():
    """Clear all demo posts from database"""
    with app.app_context():
        print("🧹 Clearing demo data...")
        
        # Count posts before deletion
        total_before = Post.query.count()
        print(f"Posts before deletion: {total_before}")
        
        # Delete all posts
        Post.query.delete()
        db.session.commit()
        
        # Count posts after deletion
        total_after = Post.query.count()
        print(f"Posts after deletion: {total_after}")
        
        print("✅ Demo data cleared successfully!")
        print("🎯 Ready to test with real Instagram data!")

if __name__ == "__main__":
    clear_demo_data() 