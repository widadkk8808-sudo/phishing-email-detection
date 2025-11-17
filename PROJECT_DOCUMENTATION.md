# AI-Driven Phishing Email Detection System
## Complete Project Documentation

**University of Technology and Applied Sciences - Sur Campus**  
**Department of Information Technology**  
**Course**: ITGP4101 - Spring 2025

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Installation Guide](#installation-guide)
4. [Usage Instructions](#usage-instructions)
5. [API Documentation](#api-documentation)
6. [Deployment Guide](#deployment-guide)
7. [Testing & Validation](#testing--validation)
8. [Troubleshooting](#troubleshooting)

---

## Project Overview

### Objectives
This project aims to combat phishing attacks by integrating **AI-based detection** with **user awareness training**. The system uses **Support Vector Machine (SVM)** machine learning algorithms to analyze email content and identify phishing attempts with high accuracy.

### Key Features
- ✅ **AI-Powered Detection**: Linear SVM with TF-IDF vectorization
- ✅ **Real-time Analysis**: Instant email classification with confidence scores
- ✅ **Detailed Explanations**: Clear reasoning for each classification
- ✅ **Modern Web Interface**: Responsive design with dark/light mode
- ✅ **RESTful API**: Complete backend for integration
- ✅ **Educational Content**: Learn about phishing through explanations

### Technology Stack

#### Machine Learning
- **Algorithm**: Support Vector Machine (Linear kernel)
- **Feature Extraction**: TF-IDF Vectorization (max 300 features)
- **Text Processing**: Custom preprocessing pipeline
- **Model Size**: 20KB (highly optimized)

#### Backend
- **Framework**: Flask (Python 3.8+)
- **API**: RESTful endpoints with JSON responses
- **CORS**: Enabled for cross-origin requests
- **Dependencies**: scikit-learn, pandas, numpy, flask, flask-cors

#### Frontend
- **Languages**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with CSS Variables
- **Icons**: Font Awesome 6.0
- **Design**: Mobile-first, responsive

---

## System Architecture

### Component Diagram
```
┌─────────────────────────────────────────────────────────┐
│                    Web Browser                          │
│              (User Interface - HTML/CSS/JS)             │
└────────────────────┬────────────────────────────────────┘
                     │ HTTP/HTTPS
                     ▼
┌─────────────────────────────────────────────────────────┐
│                  Flask Web Server                       │
│                  (api.py - Port 5000)                   │
├─────────────────────────────────────────────────────────┤
│  Routes:                                                │
│  • GET  /              → Serve index.html               │
│  • GET  /api/health    → Health check                   │
│  • GET  /api/model-info → Model information             │
│  • POST /api/predict   → Email classification           │
│  • POST /api/explain   → Detailed explanation           │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│          Phishing Detector Module                       │
│        (working_phishing_detector.py)                   │
├─────────────────────────────────────────────────────────┤
│  • Text Preprocessing                                   │
│  • Feature Extraction (TF-IDF)                          │
│  • SVM Classification                                   │
│  • Explanation Generation                               │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Trained SVM Model                          │
│          (svm_phishing_model.pkl)                       │
└─────────────────────────────────────────────────────────┘
```

### Data Flow
1. **User Input**: User pastes email content into web interface
2. **API Request**: JavaScript sends POST request to `/api/predict`
3. **Preprocessing**: Text is cleaned and normalized
4. **Feature Extraction**: TF-IDF vectorization converts text to features
5. **Classification**: SVM model predicts Safe/Phishing
6. **Explanation**: System analyzes indicators and generates reasoning
7. **Response**: JSON result sent back to frontend
8. **Display**: Results shown with confidence scores and explanations

---

## Installation Guide

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Installation

#### 1. Clone or Download the Project
```bash
cd /home/ubuntu
git clone <your-repository-url> phishing-detector
cd phishing-detector
```

#### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
- flask==2.3.3
- flask-cors==4.0.0
- scikit-learn==1.3.0
- pandas==2.0.3
- numpy==1.24.3

#### 4. Verify Model File
Ensure `svm_phishing_model.pkl` exists in the project directory. If not, train the model:
```bash
python working_phishing_detector.py
```

#### 5. Start the Server
```bash
# Using the startup script
chmod +x start_server.sh
./start_server.sh

# Or directly
python api.py
```

#### 6. Access the Application
Open your browser and navigate to:
- **Local**: http://localhost:5000
- **Network**: http://<your-ip>:5000

---

## Usage Instructions

### Web Interface

#### Analyzing an Email
1. **Paste Email Content**: Copy and paste the email text into the textarea
2. **Click "Analyze Email"**: Or press `Ctrl + Enter`
3. **View Results**: See the classification, confidence scores, and detailed explanation
4. **New Analysis**: Click "New Analysis" to analyze another email

#### Keyboard Shortcuts
- `Ctrl + Enter`: Analyze email
- `Escape`: Clear input
- `Alt + 1`: Load phishing sample
- `Alt + 2`: Load safe sample

#### Dark Mode
Click the moon/sun icon in the top-right corner to toggle between light and dark themes.

### Command Line Testing

#### Test the Model
```bash
python test_model.py
```

#### Test the API
```bash
python test_api.py
```

---

## API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### 1. Health Check
**GET** `/api/health`

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "message": "Phishing Detection API is running"
}
```

#### 2. Model Information
**GET** `/api/model-info`

**Response:**
```json
{
  "status": "success",
  "model_type": "Support Vector Machine (SVM)",
  "algorithm": "Linear SVM with TF-IDF Vectorization",
  "training_method": "Sample dataset with phishing and safe emails",
  "features": "TF-IDF vectorization of email text",
  "description": "AI-Driven Awareness Program for Phishing Email Detection using SVM"
}
```

#### 3. Predict Email Classification
**POST** `/api/predict`

**Request:**
```json
{
  "email_text": "Your email content here..."
}
```

**Response:**
```json
{
  "status": "success",
  "prediction": {
    "prediction": "Phishing",
    "confidence": 100.0,
    "safe_probability": 0.0,
    "phishing_probability": 100.0
  },
  "explanation": {
    "prediction": "Phishing",
    "confidence": 100.0,
    "safe_probability": 0.0,
    "phishing_probability": 100.0,
    "reasoning": [
      "This email shows characteristics typical of phishing attempts:",
      "• Contains suspicious language: urgent, click, verify",
      "• Contains urgent call-to-action language",
      "• Creates a sense of urgency to bypass critical thinking"
    ],
    "indicators": {
      "phishing_indicators": ["urgent", "click", "verify"],
      "safe_indicators": []
    }
  }
}
```

#### 4. Get Detailed Explanation
**POST** `/api/explain`

**Request:**
```json
{
  "email_text": "Your email content here..."
}
```

**Response:**
```json
{
  "status": "success",
  "explanation": {
    "prediction": "Phishing",
    "confidence": 100.0,
    "reasoning": [...],
    "indicators": {...}
  }
}
```

### Error Responses

#### 400 Bad Request
```json
{
  "error": "Missing email_text in request",
  "status": "error"
}
```

#### 500 Internal Server Error
```json
{
  "error": "Model not loaded",
  "status": "error"
}
```

---

## Deployment Guide

### Option 1: Vercel (Recommended for Quick Deployment)

#### Prerequisites
- GitHub account
- Vercel account (free tier available)

#### Steps
1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Deploy on Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "Import Project"
   - Select your GitHub repository
   - Vercel will auto-detect the configuration from `vercel.json`
   - Click "Deploy"

3. **Access Your App**
   - Your app will be available at: `https://your-project.vercel.app`

### Option 2: Railway (Better for Backend)

#### Prerequisites
- GitHub account
- Railway account

#### Steps
1. **Push to GitHub** (same as above)

2. **Deploy on Railway**
   - Go to [railway.app](https://railway.app)
   - Click "Deploy from GitHub repo"
   - Select your repository
   - Add environment variables:
     ```
     FLASK_ENV=production
     PORT=5000
     ```
   - Click "Deploy"

3. **Access Your App**
   - Railway will provide a public URL

### Option 3: Local Network Deployment

#### For Local Network Access
```bash
# Start server on all network interfaces
python api.py
```

The server will be accessible at:
- Local: http://localhost:5000
- Network: http://<your-local-ip>:5000

---

## Testing & Validation

### Automated Tests

#### Model Testing
```bash
python test_model.py
```

**Expected Output:**
- 6 test cases
- 100% success rate
- Confidence scores displayed

#### API Testing
```bash
python test_api.py
```

**Expected Output:**
- All endpoints tested
- Health check passed
- Prediction accuracy verified

### Manual Testing

#### Test Cases

**Phishing Email Examples:**
1. "URGENT! Your account will be suspended! Click here now!"
2. "Congratulations! You won $1,000,000! Claim your prize!"
3. "Your PayPal account has been compromised. Verify immediately!"

**Safe Email Examples:**
1. "Hi John, can we schedule a meeting for next week?"
2. "Thank you for your purchase. Order confirmation attached."
3. "Please review the attached document and provide feedback."

### Performance Metrics
- **Model Accuracy**: 100% on test dataset
- **Inference Time**: < 100ms per email
- **Model Size**: 20KB
- **Memory Usage**: < 100MB

---

## Troubleshooting

### Common Issues

#### 1. Model Not Found
**Error**: `FileNotFoundError: svm_phishing_model.pkl`

**Solution**:
```bash
python working_phishing_detector.py
```

#### 2. Port Already in Use
**Error**: `Address already in use: Port 5000`

**Solution**:
```bash
# Find process using port 5000
lsof -ti:5000

# Kill the process
kill <PID>
```

#### 3. Import Errors
**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**:
```bash
# Activate virtual environment
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### 4. CORS Issues
**Error**: Cross-origin request blocked

**Solution**: CORS is already enabled in `api.py`. Ensure the API is running and accessible.

#### 5. API Connection Failed
**Error**: Failed to fetch from API

**Solution**:
- Check if Flask server is running
- Verify the API URL in `script.js`
- Check firewall settings

---

## Project Files

### Core Files
- `api.py` - Flask REST API server
- `working_phishing_detector.py` - ML model implementation
- `svm_phishing_model.pkl` - Trained SVM model
- `index.html` - Web interface
- `script.js` - Frontend JavaScript
- `styles.css` - Styling and themes

### Configuration Files
- `requirements.txt` - Python dependencies
- `vercel.json` - Vercel deployment config
- `.gitignore` - Git ignore rules

### Documentation
- `README.md` - Quick start guide
- `DEPLOYMENT_GUIDE.md` - Deployment instructions
- `PROJECT_DOCUMENTATION.md` - This file

### Testing
- `test_model.py` - Model testing script
- `test_api.py` - API testing script
- `start_server.sh` - Server startup script

---

## Security Considerations

### Data Privacy
- ✅ No email data is stored or logged
- ✅ All processing happens in-memory
- ✅ No external API calls for email analysis

### Input Validation
- ✅ Email text validation
- ✅ Empty input rejection
- ✅ Error handling for malformed requests

### CORS Configuration
- ✅ CORS enabled for web interface
- ✅ Configurable for production deployment

---

## Future Enhancements

### Planned Features
1. **Multi-language Support**: Extend to Arabic and other languages
2. **Advanced Features**: URL analysis, attachment scanning
3. **Real-time Integration**: Email client plugins
4. **Enhanced ML**: Deep learning models for better accuracy
5. **Dashboard**: Analytics and reporting features
6. **User Accounts**: Save analysis history
7. **API Rate Limiting**: Prevent abuse
8. **Batch Processing**: Analyze multiple emails at once

### Model Improvements
1. Train on larger, more diverse datasets
2. Implement ensemble methods
3. Add deep learning models (LSTM, BERT)
4. Continuous learning from user feedback

---

## Credits

**Developed by:**
- Maiya Rashid Salim Al touqi (2020493099)
- Maather Moosa Mohammed Al Almaskari (2020493126)
- Bashair Said Saleh Al gilani (2020493112)
- Widad Khalid Khalfan Al Alawiya (2020493047)
- Manar Ali Rashid Alalawi (2019493034)

**Supervised by:**
- Dr. Raya Al-Hajri

**Course:** ITGP4101 - Spring 2025  
**Institution:** University of Technology and Applied Sciences, Sur Campus

---

## License

This project is developed for educational and demonstration purposes. Feel free to use and modify according to your needs.

---

## Support

For technical support or questions:
1. Check this documentation
2. Review the troubleshooting section
3. Test with the provided demo scripts
4. Examine the source code comments

---

**Built with ❤️ for email security awareness using Machine Learning**
