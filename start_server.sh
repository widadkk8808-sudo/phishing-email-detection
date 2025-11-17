#!/bin/bash

# AI-Driven Phishing Email Detection System
# Server Startup Script

echo "=========================================="
echo "Phishing Detection System - Starting..."
echo "=========================================="

# Navigate to project directory
cd /home/ubuntu/phishing-detector

# Activate virtual environment
source venv/bin/activate

# Check if model exists
if [ ! -f "svm_phishing_model.pkl" ]; then
    echo "Model file not found. Training model..."
    python working_phishing_detector.py
fi

# Start Flask API server
echo ""
echo "Starting Flask API server on http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo ""

python api.py
