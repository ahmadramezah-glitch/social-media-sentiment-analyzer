# Contributing to Social Media Sentiment Analyzer

Thank you for your interest in contributing to the Social Media Sentiment Analyzer project! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Bug Reports**: Report bugs and issues you encounter
- **Feature Requests**: Suggest new features or improvements
- **Code Contributions**: Submit pull requests with code changes
- **Documentation**: Improve or add documentation
- **Testing**: Help test the application and report issues
- **Translation**: Help translate the application to other languages

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic knowledge of Flask and Python

### Setting Up Development Environment

1. **Fork the repository**
   - Go to the main repository on GitHub
   - Click the "Fork" button to create your own copy

2. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/social-media-sentiment-analyzer.git
   cd social-media-sentiment-analyzer
   ```

3. **Set up the upstream remote**
   ```bash
   git remote add upstream https://github.com/original-owner/social-media-sentiment-analyzer.git
   ```

4. **Create a virtual environment**
   ```bash
   python -m venv .venv
   
   # Activate on Windows
   .venv\Scripts\activate
   
   # Activate on macOS/Linux
   source .venv/bin/activate
   ```

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Set up configuration**
   ```bash
   cp config.example.py config.py
   # Edit config.py with your API keys and settings
   ```

## 📝 Development Workflow

### 1. Create a Feature Branch

Always work on a separate branch for your changes:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/your-bug-fix
```

### 2. Make Your Changes

- Write clean, readable code
- Follow the existing code style and conventions
- Add comments for complex logic
- Update documentation if needed

### 3. Test Your Changes

Before submitting, ensure your changes work correctly:

```bash
# Run the application
python app.py

# Test the specific functionality you changed
# Check that existing features still work
```

### 4. Commit Your Changes

Use clear, descriptive commit messages:

```bash
git add .
git commit -m "Add new feature: platform filtering in database viewer

- Added platform filter dropdown to database viewer
- Updated export functionality to support platform filtering
- Added platform-specific statistics display"
```

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then go to GitHub and create a pull request.

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Code follows the project's style guidelines
- [ ] All tests pass (if applicable)
- [ ] Documentation is updated
- [ ] No sensitive information is included
- [ ] Changes are tested locally

### Pull Request Template

Use the provided template when creating pull requests. Include:

- **Description**: What the PR does and why
- **Type of Change**: Bug fix, feature, documentation, etc.
- **Testing**: How you tested the changes
- **Screenshots**: If UI changes are involved
- **Related Issues**: Link to any related issues

### Code Review Process

1. **Initial Review**: Maintainers will review your PR
2. **Feedback**: Address any feedback or requested changes
3. **Approval**: Once approved, your PR will be merged
4. **Deployment**: Changes will be deployed to staging/production

## 🎨 Code Style Guidelines

### Python Code

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Keep functions small and focused
- Add type hints where appropriate
- Use docstrings for functions and classes

### HTML/CSS/JavaScript

- Use consistent indentation (2 or 4 spaces)
- Follow Bootstrap conventions
- Use semantic HTML elements
- Keep CSS organized and commented
- Use meaningful class names

### Database

- Use descriptive table and column names
- Add appropriate indexes
- Follow SQL naming conventions
- Document complex queries

## 🧪 Testing Guidelines

### Manual Testing

- Test all affected functionality
- Test edge cases and error conditions
- Test on different browsers (if applicable)
- Test with different user roles and permissions

### Automated Testing

- Write unit tests for new functions
- Update existing tests if needed
- Ensure test coverage doesn't decrease
- Run the full test suite before submitting

## 📚 Documentation

### Code Documentation

- Add docstrings to new functions and classes
- Update existing docstrings if you modify functions
- Add inline comments for complex logic
- Keep README and other docs up to date

### API Documentation

- Document new API endpoints
- Update API documentation for changes
- Include examples and error responses
- Document authentication requirements

## 🔒 Security Considerations

### Sensitive Information

- Never commit API keys or secrets
- Use environment variables for sensitive data
- Check that no credentials are in code or logs
- Follow security best practices

### Input Validation

- Validate all user inputs
- Sanitize data before processing
- Use parameterized queries for database operations
- Implement proper access controls

## 🚨 Reporting Issues

### Bug Reports

When reporting bugs, include:

- **Description**: Clear description of the problem
- **Steps to Reproduce**: Detailed steps to recreate the issue
- **Expected vs Actual Behavior**: What should happen vs what happens
- **Environment**: OS, browser, Python version, etc.
- **Screenshots/Logs**: Visual evidence or error logs
- **Additional Context**: Any relevant information

### Feature Requests

For feature requests, include:

- **Problem Statement**: What problem the feature would solve
- **Proposed Solution**: How you envision the feature working
- **Use Cases**: Examples of when the feature would be useful
- **Priority**: How important the feature is to you
- **Mockups**: If you have design ideas

## 🌟 Recognition

Contributors will be recognized in:

- Project README
- Release notes
- Contributor hall of fame
- GitHub contributors list

## 📞 Getting Help

If you need help or have questions:

- **Issues**: Use GitHub issues for questions and discussions
- **Discussions**: Use GitHub Discussions for general topics
- **Documentation**: Check the project documentation first
- **Community**: Reach out to other contributors

## 📋 Contributor Checklist

Before contributing, ensure you have:

- [ ] Read and understood this guide
- [ ] Set up your development environment
- [ ] Familiarized yourself with the codebase
- [ ] Understood the project's goals and scope
- [ ] Agreed to the project's license and code of conduct

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project (MIT License).

---

Thank you for contributing to the Social Media Sentiment Analyzer project! 🎉

Your contributions help make this tool better for everyone in the community.
