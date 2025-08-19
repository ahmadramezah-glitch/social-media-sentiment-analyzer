#!/usr/bin/env python3
"""
Test script to verify logout functionality
"""

import requests
from config import FACEBOOK_ACCESS_TOKEN, FACEBOOK_PAGE_ID

def test_logout():
    """Test the logout functionality"""
    base_url = "http://localhost:5000"
    
    print("Testing logout functionality...")
    
    # Test 1: Check if login page is accessible
    try:
        response = requests.get(f"{base_url}/login")
        if response.status_code == 200:
            print("✅ Login page is accessible")
        else:
            print(f"❌ Login page returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error accessing login page: {e}")
    
    # Test 2: Check if dashboard requires authentication
    try:
        response = requests.get(f"{base_url}/dashboard")
        if response.status_code == 302:  # Redirect to login
            print("✅ Dashboard properly redirects unauthenticated users to login")
        else:
            print(f"❌ Dashboard returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error accessing dashboard: {e}")
    
    # Test 3: Check if logout route exists
    try:
        response = requests.get(f"{base_url}/logout")
        if response.status_code == 302:  # Redirect to login
            print("✅ Logout route exists and redirects to login")
        else:
            print(f"❌ Logout route returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error accessing logout route: {e}")
    
    print("\nLogout functionality test completed!")

if __name__ == "__main__":
    test_logout() 