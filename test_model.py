#!/usr/bin/env python3
"""
Test script for the phishing detection model
"""

import sys
import pickle
from working_phishing_detector import detector

def test_model():
    """Test the phishing detection model with sample emails"""
    
    print("="*70)
    print("PHISHING DETECTION MODEL - TEST SUITE")
    print("="*70)
    
    # Load the model
    print("\n1. Loading trained model...")
    try:
        with open('svm_phishing_model.pkl', 'rb') as f:
            detector.pipeline = pickle.load(f)
        detector.is_trained = True
        print("   ✓ Model loaded successfully!")
    except Exception as e:
        print(f"   ✗ Error loading model: {e}")
        return False
    
    # Test emails
    test_cases = [
        {
            'email': "Congratulations! You won $1,000,000! Click here immediately to claim your prize!",
            'expected': 'Phishing',
            'description': 'Obvious phishing with money and urgency'
        },
        {
            'email': "URGENT: Your account will be suspended unless you verify your identity now!",
            'expected': 'Phishing',
            'description': 'Account threat with urgency'
        },
        {
            'email': "Hi John, can we schedule a meeting for next Tuesday to discuss the project?",
            'expected': 'Safe',
            'description': 'Normal business communication'
        },
        {
            'email': "Thank you for your purchase. Your order #12345 has been confirmed and will ship soon.",
            'expected': 'Safe',
            'description': 'Legitimate order confirmation'
        },
        {
            'email': "FREE iPhone! You're the lucky winner! Click now to claim your free phone!",
            'expected': 'Phishing',
            'description': 'Free offer scam'
        },
        {
            'email': "Please find attached the quarterly report for your review. Let me know if you have any questions.",
            'expected': 'Safe',
            'description': 'Professional document sharing'
        }
    ]
    
    print("\n2. Running test cases...")
    print("-"*70)
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test['description']}")
        print(f"Email: {test['email'][:60]}...")
        
        try:
            result = detector.predict_email(test['email'])
            prediction = result['prediction']
            confidence = result['confidence']
            
            # Check if prediction matches expected
            if prediction == test['expected']:
                print(f"✓ PASSED - Predicted: {prediction} (Confidence: {confidence:.1f}%)")
                passed += 1
            else:
                print(f"✗ FAILED - Expected: {test['expected']}, Got: {prediction} (Confidence: {confidence:.1f}%)")
                failed += 1
            
            # Show detailed explanation
            explanation = detector.generate_detailed_explanation(test['email'])
            print("  Reasoning:")
            for reason in explanation['reasoning'][:3]:  # Show first 3 reasons
                print(f"    • {reason}")
                
        except Exception as e:
            print(f"✗ ERROR: {e}")
            failed += 1
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Total Tests: {len(test_cases)}")
    print(f"Passed: {passed} ✓")
    print(f"Failed: {failed} ✗")
    print(f"Success Rate: {(passed/len(test_cases)*100):.1f}%")
    print("="*70)
    
    return failed == 0

if __name__ == "__main__":
    success = test_model()
    sys.exit(0 if success else 1)
