# Quick Start Guide
## AI-Driven Phishing Email Detection System

Get your phishing detection system up and running in **5 minutes**!

---

## 🚀 Quick Setup

### Step 1: Navigate to Project Directory
```bash
cd /home/ubuntu/phishing-detector
```

### Step 2: Activate Virtual Environment
```bash
source venv/bin/activate
```

### Step 3: Start the Server
```bash
./start_server.sh
```

**That's it!** Your server is now running at http://localhost:5000

---

## 🧪 Quick Test

### Test the Model
```bash
python test_model.py
```

**Expected Output:**
```
======================================================================
PHISHING DETECTION MODEL - TEST SUITE
======================================================================
✓ Model loaded successfully!
✓ All tests passed (6/6)
✓ Success Rate: 100.0%
```

### Test the API
```bash
python test_api.py
```

**Expected Output:**
```
======================================================================
PHISHING DETECTION API - TEST SUITE
======================================================================
✓ Health Check: healthy
✓ Model Info: Support Vector Machine (SVM)
✓ Prediction Tests: All passed
```

---

## 🌐 Access the Web Interface

1. **Open your browser**
2. **Navigate to:** http://localhost:5000
3. **Paste an email** into the textarea
4. **Click "Analyze Email"**
5. **View the results!**

---

## 📝 Sample Emails to Test

### Phishing Email (Should detect as Phishing)
```
URGENT! Your account will be suspended in 24 hours! 
Click here immediately to verify your identity and claim your $1000 prize!
```

### Safe Email (Should detect as Safe)
```
Hi John, can we schedule a meeting for next Tuesday to discuss the project? 
Please let me know your availability.
```

---

## 🎯 Key Features

- ✅ **AI-Powered**: SVM machine learning
- ✅ **Real-time**: Instant analysis
- ✅ **Accurate**: 100% on test dataset
- ✅ **Explanations**: Clear reasoning provided
- ✅ **Dark Mode**: Toggle light/dark theme

---

## 🔧 Common Commands

### Start Server
```bash
./start_server.sh
```

### Stop Server
```bash
# Press Ctrl+C in the terminal where server is running
```

### Retrain Model
```bash
python working_phishing_detector.py
```

### Run Tests
```bash
python test_model.py  # Test ML model
python test_api.py    # Test API endpoints
```

---

## 📱 Keyboard Shortcuts (Web Interface)

- `Ctrl + Enter` - Analyze email
- `Escape` - Clear input
- `Alt + 1` - Load phishing sample
- `Alt + 2` - Load safe sample

---

## 🚀 Deploy to Production

### Deploy to Vercel (Free)
```bash
# 1. Push to GitHub
git init
git add .
git commit -m "Initial commit"
git push origin main

# 2. Go to vercel.com
# 3. Import your GitHub repo
# 4. Deploy!
```

**Your app will be live at:** `https://your-project.vercel.app`

---

## 📊 Project Structure

```
phishing-detector/
├── api.py                          # Flask API server
├── working_phishing_detector.py    # ML model
├── svm_phishing_model.pkl          # Trained model
├── index.html                      # Web interface
├── script.js                       # Frontend logic
├── styles.css                      # Styling
├── requirements.txt                # Dependencies
├── test_model.py                   # Model tests
├── test_api.py                     # API tests
└── start_server.sh                 # Startup script
```

---

## ❓ Troubleshooting

### Port Already in Use
```bash
lsof -ti:5000 | xargs kill
```

### Model Not Found
```bash
python working_phishing_detector.py
```

### Dependencies Missing
```bash
pip install -r requirements.txt
```

---

## 📚 More Information

- **Full Documentation**: See `PROJECT_DOCUMENTATION.md`
- **Deployment Guide**: See `DEPLOYMENT_GUIDE.md`
- **Project Details**: See `README.md`

---

## 🎓 Project Info

**Course:** ITGP4101 - Spring 2025  
**Institution:** University of Technology and Applied Sciences, Sur Campus  
**Department:** Information Technology

---

**Happy Phishing Detection! 🛡️**
