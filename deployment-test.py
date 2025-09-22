#!/usr/bin/env python3
"""
Deployment Test Script for FastAPI Blog API
Run this script to verify your application is ready for Vercel deployment
"""

import os
import sys
from pathlib import Path

def check_environment():
    """Check if all required environment variables are set"""
    print("🔍 Checking environment variables...")

    required_vars = ['MONGODB_URL', 'SECRET_KEY', 'ENVIRONMENT']
    missing_vars = []

    for var in required_vars:
        value = os.getenv(var)
        if value:
            print(f"✅ {var}: {value[:20]}...")
        else:
            print(f"❌ {var}: Not set")
            missing_vars.append(var)

    return len(missing_vars) == 0, missing_vars

def check_dependencies():
    """Check if all required dependencies are installed"""
    print("\n🔍 Checking dependencies...")

    try:
        import fastapi
        import uvicorn
        import motor
        import beanie
        import passlib
        import python_jose
        print("✅ All core dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        return False

def check_app_structure():
    """Check if the application structure is correct"""
    print("\n🔍 Checking application structure...")

    required_files = [
        'app/main.py',
        'app/blog/database.py',
        'app/blog/models.py',
        'vercel.json',
        'requirements.txt'
    ]

    missing_files = []
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path}")
            missing_files.append(file_path)

    return len(missing_files) == 0, missing_files

def test_app_import():
    """Test if the application can be imported without errors"""
    print("\n🔍 Testing application import...")

    try:
        # Add the current directory to Python path
        sys.path.insert(0, str(Path.cwd()))

        from app.main import app
        print("✅ Application imported successfully")
        print(f"   App title: {app.title}")
        print(f"   Routes: {len(app.routes)}")

        # Test health endpoint
        from fastapi.testclient import TestClient
        client = TestClient(app)

        response = client.get('/health')
        print(f"   Health endpoint: {response.status_code}")

        response = client.get('/')
        print(f"   Root endpoint: {response.status_code}")

        return True
    except Exception as e:
        print(f"❌ Application import failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 FastAPI Blog API - Deployment Readiness Test")
    print("=" * 50)

    tests = [
        ("Environment Variables", check_environment),
        ("Dependencies", check_dependencies),
        ("Application Structure", check_app_structure),
        ("Application Import", test_app_import)
    ]

    results = []
    for test_name, test_func in tests:
        print(f"\n🧪 Running {test_name} test...")
        try:
            result = test_func()
            if isinstance(result, tuple):
                passed, details = result
                results.append((test_name, passed, details))
            else:
                results.append((test_name, result, None))
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
            results.append((test_name, False, str(e)))

    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)

    all_passed = True
    for test_name, passed, details in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} {test_name}")

        if not passed and details:
            if isinstance(details, list):
                for detail in details:
                    print(f"     - {detail}")
            else:
                print(f"     - {details}")

        if not passed:
            all_passed = False

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 ALL TESTS PASSED! Your application is ready for deployment.")
        print("\nNext steps:")
        print("1. Set environment variables in Vercel dashboard")
        print("2. Push your code to GitHub")
        print("3. Deploy on Vercel")
        print("4. Test the /health endpoint on your deployed app")
    else:
        print("⚠️  Some tests failed. Please fix the issues above before deploying.")
        print("\nFor help, check the troubleshooting section in README.md")

    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
