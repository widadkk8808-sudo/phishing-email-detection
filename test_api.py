#!/usr/bin/env python3
"""
Test script for the Phishing Detection API
"""

import requests
import json

API_URL = "http://localhost:5000"

def test_api():
    """Test all API endpoints"""
    
    print("="*70)
    print("PHISHING DETECTION API - TEST SUITE")
    print("="*70)
    
    # Test 1: Health Check
    print("\n1. Testing Health Check Endpoint...")
    try:
        response = requests.get(f"{API_URL}/api/health")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✓ Status: {data['status']}")
            print(f"   ✓ Model Loaded: {data['model_loaded']}")
        else:
            print(f"   ✗ Failed with status code: {response.status_code}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 2: Model Info
    print("\n2. Testing Model Info Endpoint...")
    try:
        response = requests.get(f"{API_URL}/api/model-info")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✓ Model Type: {data['model_type']}")
            print(f"   ✓ Algorithm: {data['algorithm']}")
        else:
            print(f"   ✗ Failed with status code: {response.status_code}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 3: Predict Phishing Email
    print("\n3. Testing Prediction - Phishing Email...")
    phishing_email = "URGENT! Your account will be suspended! Click here now to verify!"
    try:
        response = requests.post(
            f"{API_URL}/api/predict",
            json={"email_text": phishing_email},
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            data = response.json()
            pred = data['prediction']
            exp = data['explanation']
            print(f"   ✓ Prediction: {pred['prediction']}")
            print(f"   ✓ Confidence: {pred['confidence']:.1f}%")
            print(f"   ✓ Safe Probability: {pred['safe_probability']:.1f}%")
            print(f"   ✓ Phishing Probability: {pred['phishing_probability']:.1f}%")
            print(f"   ✓ Reasoning: {len(exp['reasoning'])} points")
        else:
            print(f"   ✗ Failed with status code: {response.status_code}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 4: Predict Safe Email
    print("\n4. Testing Prediction - Safe Email...")
    safe_email = "Hi John, can we schedule a meeting for next week to discuss the project?"
    try:
        response = requests.post(
            f"{API_URL}/api/predict",
            json={"email_text": safe_email},
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            data = response.json()
            pred = data['prediction']
            exp = data['explanation']
            print(f"   ✓ Prediction: {pred['prediction']}")
            print(f"   ✓ Confidence: {pred['confidence']:.1f}%")
            print(f"   ✓ Safe Probability: {pred['safe_probability']:.1f}%")
            print(f"   ✓ Phishing Probability: {pred['phishing_probability']:.1f}%")
            print(f"   ✓ Reasoning: {len(exp['reasoning'])} points")
        else:
            print(f"   ✗ Failed with status code: {response.status_code}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 5: Explain Endpoint
    print("\n5. Testing Explain Endpoint...")
    try:
        response = requests.post(
            f"{API_URL}/api/explain",
            json={"email_text": phishing_email},
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            data = response.json()
            exp = data['explanation']
            print(f"   ✓ Prediction: {exp['prediction']}")
            print(f"   ✓ Reasoning Points: {len(exp['reasoning'])}")
            print("   ✓ Sample Reasoning:")
            for reason in exp['reasoning'][:2]:
                print(f"      - {reason}")
        else:
            print(f"   ✗ Failed with status code: {response.status_code}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 6: Error Handling - Empty Email
    print("\n6. Testing Error Handling - Empty Email...")
    try:
        response = requests.post(
            f"{API_URL}/api/predict",
            json={"email_text": ""},
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 400:
            print(f"   ✓ Correctly rejected empty email (400 Bad Request)")
        else:
            print(f"   ✗ Unexpected status code: {response.status_code}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    print("\n" + "="*70)
    print("API TESTING COMPLETED")
    print("="*70)

if __name__ == "__main__":
    test_api()
