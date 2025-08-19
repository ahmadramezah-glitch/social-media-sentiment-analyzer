#!/usr/bin/env python3
"""
TikTok API Setup Test Script
This script helps you test your TikTok API configuration and get OAuth setup instructions.
"""

from tiktok_api import TikTokAPI
from config import TIKTOK_CLIENT_KEY, TIKTOK_CLIENT_SECRET, TIKTOK_ACCESS_TOKEN

def test_tiktok_setup():
    print("TikTok API Setup Test")
    print("=" * 50)
    
    # Test API initialization
    try:
        api = TikTokAPI()
        print(f"✓ TikTok API initialized successfully")
        print(f"✓ Client Key: {api.client_key}")
        print(f"✓ Client Secret: {api.client_secret[:8]}...{api.client_secret[-8:]}")
        print(f"✓ Base URL: {api.base_url}")
        print(f"✓ Access Token: {'✓ Set' if api.access_token else '✗ Not set'}")
        
    except Exception as e:
        print(f"✗ Error initializing TikTok API: {e}")
        return
    
    print("\n" + "=" * 50)
    print("CURRENT STATUS:")
    
    if api.access_token:
        print("✓ Access token is configured")
        print("✓ Ready to make real TikTok API calls")
        
        # Test a simple API call
        print("\nTesting API call...")
        try:
            videos = api.search_hashtag("test")
            print(f"✓ API call successful, found {len(videos)} videos")
        except Exception as e:
            print(f"✗ API call failed: {e}")
            
    else:
        print("✗ Access token is NOT configured")
        print("✗ Will fall back to mock data")
        
        # Show OAuth setup instructions
        print("\n" + "=" * 50)
        print("OAUTH SETUP REQUIRED:")
        oauth_info = api.setup_oauth_flow()
        
        print(f"\nYour OAuth Authorization URL:")
        print(f"{oauth_info['auth_url']}")
        
        print(f"\nTo complete setup:")
        print(f"1. Visit the authorization URL above")
        print(f"2. Authorize your app")
        print(f"3. Copy the authorization code from the redirect")
        print(f"4. Exchange it for an access token")
        print(f"5. Update TIKTOK_ACCESS_TOKEN in config.py")
    
    print("\n" + "=" * 50)
    print("TEST COMPLETE")

if __name__ == "__main__":
    test_tiktok_setup()
