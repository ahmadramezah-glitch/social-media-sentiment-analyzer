# GitHub Setup Guide

This guide will walk you through setting up your Social Media Sentiment Analyzer project on GitHub.

## 🚀 Step 1: Create a GitHub Repository

1. **Go to GitHub.com** and sign in to your account
2. **Click the "+" icon** in the top right corner
3. **Select "New repository"**
4. **Fill in the repository details:**
   - **Repository name**: `social-media-sentiment-analyzer`
   - **Description**: `A comprehensive Flask-based web application for analyzing sentiment across multiple social media platforms`
   - **Visibility**: Choose Public or Private (Public recommended for open source)
   - **Initialize with**: Check "Add a README file" (we'll replace it)
   - **Add .gitignore**: Choose Python
   - **Choose a license**: MIT License
5. **Click "Create repository"**

## 🔧 Step 2: Clone the Repository Locally

1. **Open your terminal/command prompt**
2. **Navigate to your project directory** (if not already there):
   ```bash
   cd C:\Users\ahmad\Desktop\mtc
   ```
3. **Clone the repository** (replace `yourusername` with your actual GitHub username):
   ```bash
   git clone https://github.com/yourusername/social-media-sentiment-analyzer.git
   ```
4. **Navigate into the cloned directory**:
   ```bash
   cd social-media-sentiment-analyzer
   ```

## 📁 Step 3: Copy Your Project Files

1. **Copy all your project files** from the current directory to the cloned repository:
   ```bash
   # Copy all files except .git and .venv
   xcopy /E /I /H /Y "C:\Users\ahmad\Desktop\mtc\*" "." /EXCLUDE:exclude.txt
   ```

2. **Create an exclude.txt file** with these contents:
   ```
   .git
   .venv
   __pycache__
   instance
   ```

## 🔒 Step 3: Update .gitignore for Sensitive Data

Since your project contains sensitive configuration files, let's update the .gitignore:

1. **Edit the .gitignore file** to ensure sensitive files are excluded:
   ```bash
   # Add these lines to .gitignore if not already present
   config.py
   .env
   instance/
   *.db
   *.sqlite
   *.sqlite3
   ```

2. **Create a config.example.py file** for reference:
   ```python
   # Copy your config.py and remove sensitive data
   # Keep the structure but replace actual API keys with placeholders
   ```

## 📝 Step 4: Initial Git Setup

1. **Initialize git** (if not already done):
   ```bash
   git init
   ```

2. **Add your remote origin**:
   ```bash
   git remote add origin https://github.com/yourusername/social-media-sentiment-analyzer.git
   ```

3. **Add all files**:
   ```bash
   git add .
   ```

4. **Make your first commit**:
   ```bash
   git commit -m "Initial commit: Social Media Sentiment Analyzer"
   ```

5. **Push to GitHub**:
   ```bash
   git push -u origin main
   ```

## 🔐 Step 5: Handle Sensitive Configuration

Since your project contains sensitive API keys and configuration, you have two options:

### Option A: Use Environment Variables (Recommended)

1. **Create a `.env` file** (this will be ignored by git):
   ```env
   FLASK_SECRET_KEY=your-actual-secret-key
   TWITTER_BEARER_TOKEN=your-actual-twitter-token
   INSTAGRAM_ACCESS_TOKEN=your-actual-instagram-token
   TIKTOK_ACCESS_TOKEN=your-actual-tiktok-token
   ```

2. **Create a `config.example.py`** file with placeholder values:
   ```python
   # This file shows the structure without sensitive data
   # Users should copy this and fill in their own API keys
   ```

### Option B: Use GitHub Secrets (For Production)

1. **Go to your repository settings**
2. **Click on "Secrets and variables" → "Actions"**
3. **Add your secrets**:
   - `FLASK_SECRET_KEY`
   - `TWITTER_BEARER_TOKEN`
   - `INSTAGRAM_ACCESS_TOKEN`
   - `TIKTOK_ACCESS_TOKEN`

## 🚀 Step 6: Create GitHub Actions (Optional)

Create a `.github/workflows/ci.yml` file for automated testing:

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        python -m pytest
```

## 📚 Step 7: Update Documentation

1. **Update the README.md** with your actual GitHub username
2. **Add screenshots** of your application (optional but recommended)
3. **Create a CONTRIBUTING.md** file if you want others to contribute
4. **Add issue templates** for bug reports and feature requests

## 🔄 Step 8: Regular Updates

For future updates:

1. **Make your changes**
2. **Add files**:
   ```bash
   git add .
   ```
3. **Commit changes**:
   ```bash
   git commit -m "Description of your changes"
   ```
4. **Push to GitHub**:
   ```bash
   git push origin main
   ```

## 🌟 Step 9: Make Your Repository Stand Out

1. **Add topics** to your repository (click on "About" section)
   - `flask`
   - `sentiment-analysis`
   - `social-media`
   - `python`
   - `nlp`
   - `data-analysis`

2. **Create a good description** in the About section

3. **Add a website** if you deploy it (optional)

4. **Enable GitHub Pages** for documentation (optional)

## 🚨 Important Security Notes

- **Never commit API keys** or sensitive configuration
- **Use environment variables** for sensitive data
- **Regularly update dependencies** to fix security vulnerabilities
- **Review code** before pushing to ensure no secrets are exposed

## 🆘 Troubleshooting

### Common Issues:

1. **"Permission denied"**: Check your GitHub authentication
2. **"Repository not found"**: Verify the repository URL and your username
3. **"Large file" errors**: Check if you're trying to commit large files or virtual environments

### Solutions:

1. **Use GitHub CLI** for easier authentication:
   ```bash
   gh auth login
   ```

2. **Use SSH instead of HTTPS**:
   ```bash
   git remote set-url origin git@github.com:yourusername/social-media-sentiment-analyzer.git
   ```

3. **Check file sizes** before committing:
   ```bash
   git status
   ```

## 🎉 Congratulations!

Your Social Media Sentiment Analyzer is now on GitHub! 

- **Repository**: `https://github.com/yourusername/social-media-sentiment-analyzer`
- **Issues**: Use the Issues tab for bug reports and feature requests
- **Discussions**: Enable Discussions for community engagement
- **Wiki**: Create a Wiki for detailed documentation

## 📞 Need Help?

- **GitHub Help**: https://help.github.com/
- **Git Documentation**: https://git-scm.com/doc
- **Flask Documentation**: https://flask.palletsprojects.com/

---

**Remember**: Keep your API keys secure and never share them publicly!
