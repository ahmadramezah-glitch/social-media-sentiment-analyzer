# TikTok API Setup Guide

## Current Status ✅
- **Client Key**: `aw3fjyb3brmee44j` ✅
- **Client Secret**: `KCZvutQtBvj7BLRLQW1qkCfSVX8C4Hmg` ✅
- **Base URL**: `https://open.tiktokapis.com/v2` ✅
- **Access Token**: ❌ **NOT SET** (This is what you need to get)

## What You Have vs. What You Need

### ✅ What You Already Have:
1. **TikTok Developer Account** - You're registered as a developer
2. **App Created** - Your app exists with the credentials above
3. **Client Credentials** - Your app's ID and secret are configured

### ❌ What You Still Need:
1. **Access Token** - This is the key to actually using the API
2. **OAuth 2.0 Setup** - The process to get user permission

## Step-by-Step Setup Instructions

### Step 1: Complete OAuth 2.0 Setup in TikTok Developer Console

1. Go to [TikTok Developer Console](https://developers.tiktok.com/)
2. Sign in with your account
3. Find your app (the one with client key `aw3fjyb3brmee44j`)
4. Go to **App Management** → **OAuth 2.0**
5. Set up your redirect URI: `http://localhost:5000/tiktok-callback`
6. Request these permissions:
   - `user.info.basic` - Basic user information
   - `video.list` - Access to video data
   - `hashtag.search` - Search hashtags

### Step 2: Get User Authorization

1. **Visit this authorization URL** (replace with your actual app):
   ```
   https://www.tiktok.com/v2/auth/authorize?
   client_key=aw3fjyb3brmee44j&
   scope=user.info.basic,video.list,hashtag.search&
   response_type=code&
   redirect_uri=http://localhost:5000/tiktok-callback
   ```

2. **Authorize your app** when prompted
3. **Copy the authorization code** from the redirect URL

### Step 3: Exchange Code for Access Token

1. **Make a POST request** to get your access token:
   ```bash
   curl -X POST "https://open.tiktokapis.com/v2/oauth/token/" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "client_key=aw3fjyb3brmee44j" \
     -d "client_secret=KCZvutQtBvj7BLRLQW1qkCfSVX8C4Hmg" \
     -d "code=YOUR_AUTHORIZATION_CODE" \
     -d "grant_type=authorization_code" \
     -d "redirect_uri=http://localhost:5000/tiktok-callback"
   ```

2. **Save the access token** from the response

### Step 4: Update Your Configuration

1. **Edit `config.py`**:
   ```python
   # Change this line:
   TIKTOK_ACCESS_TOKEN = None
   
   # To this:
   TIKTOK_ACCESS_TOKEN = "YOUR_ACTUAL_ACCESS_TOKEN_HERE"
   ```

2. **Restart your Flask app**

## Testing Your Setup

Run this command to test if everything is working:
```bash
python test_tiktok_setup.py
```

## What Happens After Setup

### ✅ With Access Token:
- **Real TikTok data** - Actual videos, hashtags, and user content
- **Video downloads** - Real TikTok videos saved locally
- **Speech-to-text** - Actual audio transcription from videos
- **Real-time analysis** - Live data from TikTok platform

### ❌ Without Access Token (Current State):
- **Mock data** - Example/placeholder content
- **Placeholder files** - Text files instead of real videos
- **Simulated analysis** - Not real TikTok content

## Troubleshooting

### Common Issues:
1. **"Invalid client"** - Check your client key/secret
2. **"Invalid redirect URI"** - Make sure redirect URI matches exactly
3. **"Insufficient permissions"** - Request more permissions in developer console
4. **"Token expired"** - Access tokens expire, you'll need to refresh them

### Getting Help:
- [TikTok Developer Documentation](https://developers.tiktok.com/doc)
- [TikTok API Reference](https://developers.tiktok.com/doc/tiktok-api-v2)
- [OAuth 2.0 Guide](https://developers.tiktok.com/doc/oauth-2-0)

## Next Steps

1. **Complete OAuth setup** in TikTok Developer Console
2. **Get your access token** using the authorization flow
3. **Update config.py** with the real token
4. **Test the setup** with `python test_tiktok_setup.py`
5. **Restart your Flask app** to use real TikTok data

## Security Notes

- **Never commit** your client secret or access token to version control
- **Keep credentials secure** - they give access to TikTok data
- **Rotate tokens** periodically for security
- **Monitor API usage** to stay within rate limits

---

**Need help?** The setup script will guide you through each step and show you exactly what's missing.
