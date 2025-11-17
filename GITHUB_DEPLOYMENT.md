# GitHub Deployment Guide
## AI-Driven Phishing Email Detection System

Complete guide to deploy your project on GitHub and make it publicly accessible.

---

## 📋 Prerequisites

1. **GitHub Account**: Create one at [github.com](https://github.com)
2. **Git Installed**: Check with `git --version`
3. **Project Files**: All files in `/home/ubuntu/phishing-detector/`

---

## 🚀 Step-by-Step Deployment

### Step 1: Initialize Git Repository

```bash
cd /home/ubuntu/phishing-detector

# Initialize git repository
git init

# Configure git (replace with your info)
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Step 2: Create .gitignore File

The `.gitignore` file is already created. Verify it contains:

```bash
cat .gitignore
```

**Should include:**
- `venv/` - Virtual environment
- `__pycache__/` - Python cache
- `*.log` - Log files
- `*.csv` - Large datasets

### Step 3: Add Files to Git

```bash
# Add all files
git add .

# Check what will be committed
git status

# Commit the files
git commit -m "Initial commit: AI-Driven Phishing Email Detection System"
```

### Step 4: Create GitHub Repository

1. **Go to GitHub**: [github.com/new](https://github.com/new)
2. **Repository Name**: `phishing-email-detection`
3. **Description**: "AI-Driven Awareness Program for Phishing Email Detection using SVM"
4. **Visibility**: Choose Public or Private
5. **DO NOT** initialize with README (we already have one)
6. **Click**: "Create repository"

### Step 5: Connect Local Repository to GitHub

GitHub will show you commands. Use these:

```bash
# Add remote repository
git remote add origin https://github.com/YOUR-USERNAME/phishing-email-detection.git

# Verify remote
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main
```

**Enter your GitHub credentials when prompted.**

---

## 🌐 Deploy to Vercel (Free Hosting)

### Option A: Deploy via Vercel Dashboard

1. **Go to Vercel**: [vercel.com](https://vercel.com)
2. **Sign up/Login**: Use your GitHub account
3. **Import Project**: Click "Add New..." → "Project"
4. **Select Repository**: Choose `phishing-email-detection`
5. **Configure**:
   - Framework Preset: Other
   - Root Directory: `./`
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
6. **Deploy**: Click "Deploy"

**Your app will be live at:** `https://phishing-email-detection.vercel.app`

### Option B: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
cd /home/ubuntu/phishing-detector
vercel

# Follow the prompts:
# - Set up and deploy? Yes
# - Which scope? Your account
# - Link to existing project? No
# - Project name? phishing-email-detection
# - Directory? ./
# - Override settings? No

# Deploy to production
vercel --prod
```

---

## 🚂 Deploy to Railway (Alternative)

### Step 1: Create Railway Account
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub

### Step 2: Deploy from GitHub
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose `phishing-email-detection`
4. Railway will auto-detect Python and deploy

### Step 3: Configure Environment Variables
1. Go to your project settings
2. Add variables:
   ```
   FLASK_ENV=production
   PORT=5000
   ```

### Step 4: Access Your App
Railway will provide a public URL: `https://your-app.railway.app`

---

## 📦 Files to Include in GitHub

### Essential Files (Must Include)
- ✅ `api.py` - Flask API server
- ✅ `working_phishing_detector.py` - ML model
- ✅ `svm_phishing_model.pkl` - Trained model (20KB)
- ✅ `index.html` - Web interface
- ✅ `script.js` - Frontend JavaScript
- ✅ `styles.css` - Styling
- ✅ `requirements.txt` - Python dependencies
- ✅ `vercel.json` - Vercel configuration
- ✅ `README.md` - Project documentation
- ✅ `DEPLOYMENT_GUIDE.md` - Deployment instructions
- ✅ `.gitignore` - Git ignore rules

### Optional Files (Helpful)
- ✅ `test_model.py` - Model testing
- ✅ `test_api.py` - API testing
- ✅ `start_server.sh` - Server startup script
- ✅ `PROJECT_DOCUMENTATION.md` - Full documentation
- ✅ `QUICK_START.md` - Quick start guide

### Files to EXCLUDE (in .gitignore)
- ❌ `venv/` - Virtual environment (large)
- ❌ `__pycache__/` - Python cache
- ❌ `*.log` - Log files
- ❌ `*.csv` - Large datasets
- ❌ `server.log` - Server logs

---

## 🔧 Update Deployment Configuration

### For Vercel

The `vercel.json` file is already configured:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "api.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api.py"
    }
  ]
}
```

### For Railway

Create `railway.json` (optional):

```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python api.py",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

---

## 📝 Update README for GitHub

Make sure your `README.md` includes:

1. **Project Title and Description**
2. **Live Demo Link** (after deployment)
3. **Features**
4. **Technology Stack**
5. **Installation Instructions**
6. **Usage Guide**
7. **API Documentation**
8. **Screenshots** (optional)
9. **Credits**
10. **License**

---

## 🖼️ Add Screenshots (Optional)

### Capture Screenshots

1. **Homepage**: Main interface
2. **Analysis Result**: Phishing detection
3. **Dark Mode**: Theme toggle
4. **API Response**: JSON output

### Add to GitHub

```bash
# Create screenshots directory
mkdir screenshots

# Add screenshots
git add screenshots/
git commit -m "Add screenshots"
git push
```

### Reference in README

```markdown
## Screenshots

### Main Interface
![Main Interface](screenshots/homepage.png)

### Phishing Detection
![Detection Result](screenshots/detection.png)
```

---

## 🔄 Update Your Repository

### After Making Changes

```bash
# Check status
git status

# Add changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push to GitHub
git push
```

### Vercel Auto-Deploy
Vercel automatically deploys when you push to GitHub!

---

## 🌟 Make Your Repository Stand Out

### Add Badges to README

```markdown
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
```

### Add Topics to GitHub Repository

1. Go to your repository on GitHub
2. Click "About" (gear icon)
3. Add topics:
   - `machine-learning`
   - `phishing-detection`
   - `svm`
   - `flask`
   - `cybersecurity`
   - `email-security`
   - `python`
   - `ai`

### Create a Good README Structure

```markdown
# Project Title
Brief description

## 🌟 Features
- Feature 1
- Feature 2

## 🚀 Live Demo
[View Live Demo](https://your-app.vercel.app)

## 📸 Screenshots
[Add screenshots]

## 🛠️ Technology Stack
[List technologies]

## 📦 Installation
[Installation steps]

## 🎯 Usage
[Usage instructions]

## 📚 API Documentation
[API docs]

## 🤝 Contributing
[Contribution guidelines]

## 📝 License
[License info]

## 👥 Authors
[Your team]
```

---

## 🔐 Security Best Practices

### 1. Never Commit Sensitive Data
- ❌ API keys
- ❌ Passwords
- ❌ Database credentials
- ❌ Private keys

### 2. Use Environment Variables
For sensitive data, use environment variables:

```python
import os
API_KEY = os.environ.get('API_KEY')
```

### 3. Review .gitignore
Ensure all sensitive files are excluded.

---

## 📊 Monitor Your Deployment

### Vercel Dashboard
- View deployment logs
- Monitor performance
- Check analytics
- Configure domains

### Railway Dashboard
- View logs
- Monitor resource usage
- Configure environment variables
- Set up custom domains

---

## 🎓 Project Presentation

### For Your Graduation Project

1. **GitHub Repository**: Share the link
2. **Live Demo**: Show the deployed app
3. **Documentation**: Reference README and docs
4. **Code Quality**: Clean, well-commented code
5. **Testing**: Show test results
6. **Performance**: Display metrics

### Repository URL Format
```
https://github.com/YOUR-USERNAME/phishing-email-detection
```

### Live Demo URL Format
```
https://phishing-email-detection.vercel.app
```

---

## ✅ Deployment Checklist

Before submitting your project:

- [ ] All code pushed to GitHub
- [ ] README.md is complete and informative
- [ ] .gitignore excludes unnecessary files
- [ ] requirements.txt is up to date
- [ ] Model file (svm_phishing_model.pkl) is included
- [ ] Deployed to Vercel or Railway
- [ ] Live demo is working
- [ ] API endpoints are accessible
- [ ] Web interface loads correctly
- [ ] Tests are passing
- [ ] Documentation is complete
- [ ] License is added
- [ ] Credits are included

---

## 🆘 Troubleshooting

### Git Push Rejected
```bash
# Pull latest changes first
git pull origin main --rebase

# Then push
git push origin main
```

### Large File Error
```bash
# Remove large files from git
git rm --cached large_file.csv
git commit -m "Remove large file"
git push
```

### Vercel Build Failed
- Check `vercel.json` configuration
- Verify `requirements.txt` is correct
- Check build logs in Vercel dashboard

### Railway Deployment Failed
- Check Python version compatibility
- Verify environment variables
- Review deployment logs

---

## 📞 Support

### Resources
- **GitHub Docs**: [docs.github.com](https://docs.github.com)
- **Vercel Docs**: [vercel.com/docs](https://vercel.com/docs)
- **Railway Docs**: [docs.railway.app](https://docs.railway.app)

### Community
- **GitHub Discussions**: Enable in your repository
- **Stack Overflow**: Tag questions with relevant tags
- **Discord/Slack**: Join developer communities

---

## 🎉 Congratulations!

Your AI-Driven Phishing Email Detection System is now:
- ✅ Version controlled with Git
- ✅ Hosted on GitHub
- ✅ Deployed to the cloud
- ✅ Publicly accessible
- ✅ Ready for presentation!

**Share your project:**
- Repository: `https://github.com/YOUR-USERNAME/phishing-email-detection`
- Live Demo: `https://your-app.vercel.app`

---

**Good luck with your graduation project! 🎓**
