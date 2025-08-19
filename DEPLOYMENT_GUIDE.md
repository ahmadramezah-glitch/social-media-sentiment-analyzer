# Deployment Guide

This guide covers deploying your Social Media Sentiment Analyzer to various platforms.

## 🚀 Local Development

### Prerequisites
- Python 3.8+
- pip
- Virtual environment

### Setup
```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (macOS/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp config.example.py config.py
# Edit config.py with your API keys

# Run the application
python app.py
```

## ☁️ Cloud Deployment Options

### 1. Heroku

#### Prerequisites
- Heroku account
- Heroku CLI installed

#### Deployment Steps
```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Set environment variables
heroku config:set FLASK_SECRET_KEY=your-secret-key
heroku config:set TWITTER_BEARER_TOKEN=your-twitter-token
heroku config:set INSTAGRAM_ACCESS_TOKEN=your-instagram-token
heroku config:set TIKTOK_ACCESS_TOKEN=your-tiktok-token

# Deploy
git push heroku main

# Open the app
heroku open
```

#### Heroku Files Required
Create `Procfile`:
```
web: gunicorn app:app
```

Update `requirements.txt` to include:
```
gunicorn==20.1.0
```

### 2. Python Anywhere

#### Steps
1. Create account at [PythonAnywhere.com](https://www.pythonanywhere.com)
2. Upload your project files
3. Set up virtual environment
4. Install requirements
5. Configure WSGI file
6. Set environment variables

### 3. DigitalOcean App Platform

#### Steps
1. Create DigitalOcean account
2. Connect your GitHub repository
3. Configure build settings
4. Set environment variables
5. Deploy

### 4. AWS Elastic Beanstalk

#### Prerequisites
- AWS account
- AWS CLI configured

#### Deployment Steps
```bash
# Install EB CLI
pip install awsebcli

# Initialize EB application
eb init

# Create environment
eb create production

# Deploy
eb deploy
```

## 🐳 Docker Deployment

### Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

### Build and Run
```bash
# Build image
docker build -t sentiment-analyzer .

# Run container
docker run -p 5000:5000 sentiment-analyzer
```

### Docker Compose
Create `docker-compose.yml`:
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_SECRET_KEY=your-secret-key
      - TWITTER_BEARER_TOKEN=your-twitter-token
    volumes:
      - ./instance:/app/instance
```

## 🔒 Production Security Checklist

### Environment Variables
- [ ] Set `FLASK_SECRET_KEY` to a strong, random value
- [ ] Configure all API tokens
- [ ] Set `DEBUG=False`
- [ ] Set `ENVIRONMENT=production`

### Database
- [ ] Use production database (PostgreSQL/MySQL)
- [ ] Set up database backups
- [ ] Configure connection pooling

### Security Headers
- [ ] Enable HTTPS
- [ ] Set security headers
- [ ] Configure CORS properly
- [ ] Enable rate limiting

### Monitoring
- [ ] Set up logging
- [ ] Configure error tracking
- [ ] Set up health checks
- [ ] Monitor performance

## 📊 Performance Optimization

### Database
- [ ] Add database indexes
- [ ] Optimize queries
- [ ] Use connection pooling
- [ ] Implement caching

### Application
- [ ] Enable gunicorn workers
- [ ] Configure static file serving
- [ ] Implement caching layers
- [ ] Use CDN for static assets

### Scaling
- [ ] Load balancing
- [ ] Horizontal scaling
- [ ] Auto-scaling policies
- [ ] Database sharding (if needed)

## 🔧 Environment-Specific Configurations

### Development
```python
DEBUG = True
ENVIRONMENT = 'development'
FEATURES['demo_data'] = True
```

### Staging
```python
DEBUG = False
ENVIRONMENT = 'staging'
FEATURES['demo_data'] = False
```

### Production
```python
DEBUG = False
ENVIRONMENT = 'production'
FEATURES['demo_data'] = False
SECURITY_CONFIG['session_timeout'] = 1800
```

## 📝 Deployment Checklist

### Pre-Deployment
- [ ] Test all functionality locally
- [ ] Update requirements.txt
- [ ] Set environment variables
- [ ] Configure database
- [ ] Test database connections

### Deployment
- [ ] Deploy to staging (if applicable)
- [ ] Run smoke tests
- [ ] Deploy to production
- [ ] Verify deployment
- [ ] Monitor logs

### Post-Deployment
- [ ] Verify all features work
- [ ] Check performance metrics
- [ ] Monitor error rates
- [ ] Set up alerts
- [ ] Document deployment

## 🆘 Troubleshooting

### Common Issues

#### Database Connection Errors
- Check database credentials
- Verify network connectivity
- Check firewall settings

#### API Key Issues
- Verify API keys are set
- Check API rate limits
- Verify API permissions

#### Performance Issues
- Check database queries
- Monitor resource usage
- Review caching configuration

### Debug Commands
```bash
# Check logs
heroku logs --tail

# Check environment variables
heroku config

# Restart application
heroku restart

# Check database
heroku pg:psql
```

## 📚 Additional Resources

- [Flask Deployment Guide](https://flask.palletsprojects.com/en/2.3.x/deploying/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Heroku Python Guide](https://devcenter.heroku.com/categories/python)
- [Docker Python Guide](https://docs.docker.com/language/python/)

---

**Remember**: Always test in staging before deploying to production!
