#!/bin/bash

# GitHub Publishing Script
# AI-Driven Phishing Email Detection System

echo "=========================================="
echo "GitHub Publishing Script"
echo "=========================================="
echo ""

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is not installed."
    echo "Please install it from: https://cli.github.com/"
    exit 1
fi

# Check if user is logged in
if ! gh auth status &> /dev/null; then
    echo "🔐 You need to login to GitHub first."
    echo "Run: gh auth login"
    echo ""
    read -p "Press Enter to login now, or Ctrl+C to cancel..."
    gh auth login
fi

echo ""
echo "Creating GitHub repository..."
echo ""

# Create repository
gh repo create phishing-email-detection \
    --public \
    --description "AI-Driven Awareness Program for Phishing Email Detection using SVM - Graduation Project" \
    --source=. \
    --remote=origin \
    --push

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✅ SUCCESS! Repository created and pushed!"
    echo "=========================================="
    echo ""
    echo "📍 Your repository is now live at:"
    gh repo view --web
    echo ""
    echo "🚀 Next steps:"
    echo "1. Visit your repository on GitHub"
    echo "2. Go to Vercel.com and import your repository"
    echo "3. Deploy with one click!"
    echo ""
else
    echo ""
    echo "❌ Failed to create repository."
    echo "You can create it manually:"
    echo "1. Go to: https://github.com/new"
    echo "2. Name: phishing-email-detection"
    echo "3. Make it public"
    echo "4. Don't initialize with README"
    echo "5. Run these commands:"
    echo ""
    echo "   git remote add origin https://github.com/YOUR-USERNAME/phishing-email-detection.git"
    echo "   git push -u origin main"
    echo ""
fi
