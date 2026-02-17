"""
Quick setup and test script for Kira Health Assistant.
Run this to verify your environment is set up correctly.
"""

import sys
import subprocess


def check_python_version():
    """Check if Python version is compatible."""
    print("Checking Python version...")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required.")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    return True


def install_requirements():
    """Install required packages."""
    print("\nInstalling requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements.")
        return False


def check_imports():
    """Check if critical packages can be imported."""
    print("\nChecking critical packages...")
    packages = {
        "torch": "PyTorch",
        "transformers": "Transformers",
        "datasets": "Datasets",
        "peft": "PEFT (LoRA)",
        "gradio": "Gradio",
        "evaluate": "Evaluate"
    }
    
    all_good = True
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"✅ {name}")
        except ImportError:
            print(f"❌ {name} - not found")
            all_good = False
    
    return all_good


def check_gpu():
    """Check if GPU is available."""
    print("\nChecking GPU availability...")
    try:
        import torch
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1e9
            print(f"✅ GPU available: {gpu_name}")
            print(f"   Memory: {gpu_memory:.2f} GB")
            return True
        else:
            print("⚠️  No GPU detected. Training will be slow on CPU.")
            print("   Consider using Google Colab with GPU runtime.")
            return False
    except Exception as e:
        print(f"❌ Error checking GPU: {e}")
        return False


def check_files():
    """Check if required files exist."""
    print("\nChecking project files...")
    import os
    
    required_files = [
        "kira_health_assistant.ipynb",
        "requirements.txt",
        "config.py",
        "inference.py",
        "README.md"
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - not found")
            all_exist = False
    
    return all_exist


def main():
    """Run all checks."""
    print("=" * 70)
    print("🩺 Kira Health Assistant - Setup Verification")
    print("=" * 70)
    
    checks = [
        ("Python Version", check_python_version),
        ("Project Files", check_files),
        ("GPU", check_gpu),
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ Error during {name} check: {e}")
            results.append((name, False))
        print()
    
    # Ask about installing requirements
    print("=" * 70)
    response = input("Install/Update requirements? (y/n): ").lower().strip()
    if response == 'y':
        install_success = install_requirements()
        if install_success:
            import_success = check_imports()
            results.append(("Package Imports", import_success))
    
    # Summary
    print("\n" + "=" * 70)
    print("SETUP VERIFICATION SUMMARY")
    print("=" * 70)
    
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {name}")
    
    all_passed = all(passed for _, passed in results)
    
    print("=" * 70)
    if all_passed:
        print("🎉 All checks passed! You're ready to go!")
        print("\nNext steps:")
        print("1. Open kira_health_assistant.ipynb in Jupyter or Google Colab")
        print("2. Run all cells to train the model")
        print("3. Use the Gradio interface to interact with Kira")
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
        print("\nTroubleshooting:")
        print("- Make sure you're in the project directory")
        print("- Install requirements: pip install -r requirements.txt")
        print("- For GPU training, use Google Colab with GPU runtime")
    print("=" * 70)


if __name__ == "__main__":
    main()
