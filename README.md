# Social Media Sentiment Analyzer

A comprehensive Flask-based web application for analyzing sentiment across multiple social media platforms including Instagram, Twitter, and TikTok. This project provides real-time sentiment analysis, data visualization, and comprehensive reporting capabilities.

## 🚀 Features

### Core Functionality
- **Multi-Platform Support**: Instagram, Twitter, and TikTok integration
- **Real-time Sentiment Analysis**: Advanced NLP-based sentiment analysis using NLTK
- **Comprehensive Dashboard**: Interactive charts and statistics
- **Data Export**: Excel and PDF export capabilities
- **User Management**: Role-based access control system
- **Database Viewer**: Advanced filtering and search capabilities

### Twitter Analysis
- Hashtag-based search functionality
- Tweet sentiment analysis
- Comment analysis and sentiment scoring
- Demo data support for testing
- Real-time processing with up to 20+ tweets

### Instagram Analysis
- Post sentiment analysis
- Media content processing
- User engagement metrics
- Historical data tracking

### TikTok Analysis
- Video content sentiment analysis
- Trend analysis
- User interaction metrics

### Advanced Features
- **Platform Filtering**: Filter data by social media platform
- **Hashtag Filtering**: Search and filter by specific hashtags
- **Sentiment Distribution**: Visual representation of positive, negative, and neutral content
- **Time-based Analytics**: Monthly sentiment trends and patterns
- **Export Functionality**: Comprehensive data export in multiple formats

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLAlchemy with SQLite
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Sentiment Analysis**: NLTK (Natural Language Toolkit)
- **Data Visualization**: Chart.js
- **Icons**: Font Awesome
- **Export**: openpyxl (Excel), reportlab (PDF)

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/social-media-sentiment-analyzer.git
   cd social-media-sentiment-analyzer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   Create a `.env` file in the root directory with your API keys:
   ```env
   FLASK_SECRET_KEY=your-secret-key-here
   TWITTER_BEARER_TOKEN=your-twitter-api-token
   INSTAGRAM_ACCESS_TOKEN=your-instagram-access-token
   TIKTOK_ACCESS_TOKEN=your-tiktok-access-token
   ```

## 🔧 Configuration

### API Setup
1. **Twitter API**: Follow the setup guide in `TWITTER_API_SETUP_GUIDE.md`
2. **Instagram API**: Follow the setup guide in the Instagram API documentation
3. **TikTok API**: Follow the setup guide in `TIKTOK_API_SETUP_GUIDE.md`

### Database Setup
The application uses SQLite by default. For production, consider using PostgreSQL or MySQL.

## 🚀 Running the Application

1. **Start the Flask application**
   ```bash
   python app.py
   ```

2. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

3. **Default login credentials**
   - Username: `admin`
   - Password: `admin123`

## 📊 Usage

### Dashboard Overview
- View overall statistics and sentiment distribution
- Access platform-specific analytics
- Monitor recent activity

### Twitter Search
1. Navigate to the Twitter search page
2. Enter a hashtag (e.g., "mtc", "digital", "innovation")
3. Click "Search Twitter"
4. View results with sentiment analysis
5. Click on individual tweets for detailed analysis

### Database Viewer
1. Access the database viewer (admin only)
2. Filter by hashtag and/or platform
3. Export filtered data to Excel or PDF
4. View comprehensive statistics

### User Management
- Create new users with specific permissions
- Manage user roles and access levels
- Monitor user activity

## 🔒 Security Features

- **Session Management**: Secure session handling with configurable timeouts
- **Role-based Access Control**: Different permission levels for users
- **Input Validation**: Comprehensive input sanitization and validation
- **CSRF Protection**: Built-in CSRF protection for forms

## 📁 Project Structure

```
social-media-sentiment-analyzer/
├── app.py                 # Main Flask application
├── models.py             # Database models
├── config.py             # Configuration and demo data
├── twitter_api.py        # Twitter API integration
├── instagram_api.py      # Instagram API integration
├── tiktok_api.py         # TikTok API integration
├── sentiment.py          # Sentiment analysis functions
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
│   ├── base.html
│   ├── dashboard_overview.html
│   ├── twitter_search.html
│   ├── twitter_results.html
│   ├── database_viewer.html
│   └── ...
├── static/               # Static files (CSS, JS, images)
└── instance/             # Instance-specific files (database, config)
```

## 🧪 Testing

The application includes comprehensive demo data for testing purposes:

- **Demo Hashtags**: mtc, digital, innovation, tech, lebanon, touchlebanon
- **Mixed Content**: Arabic and English content
- **Sentiment Variety**: Positive, negative, and neutral examples
- **Realistic Data**: Simulated social media posts with engagement metrics

## 📈 Data Export

### Supported Formats
- **Excel (.xlsx)**: Comprehensive data export with multiple sheets
- **PDF**: Formatted reports with charts and statistics

### Export Features
- Filter by hashtag and platform
- Include all post details and sentiment scores
- Customizable date ranges
- Professional formatting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **NLTK**: Natural language processing capabilities
- **Flask**: Web framework
- **Bootstrap**: Frontend framework
- **Font Awesome**: Icon library
- **Chart.js**: Data visualization

## 📞 Support

For support and questions:
- Create an issue in the GitHub repository
- Contact the development team
- Check the documentation in the `/docs` folder

## 🔄 Version History

- **v1.0.0**: Initial release with basic functionality
- **v1.1.0**: Added platform filtering and enhanced export features
- **v1.2.0**: Improved sentiment analysis and demo data
- **v1.3.0**: Enhanced UI/UX and performance optimizations

---

**Note**: This application is designed for educational and research purposes. Please ensure compliance with social media platform terms of service and data privacy regulations when using in production environments.
