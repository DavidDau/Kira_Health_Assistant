"""
Windows-specific setup script for Kira Health Assistant.
Handles common Windows + Python 3.13 compatibility issues.
"""

import subprocess
import sys
import os

def install_package(package):
    """Install a single package."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    print("=" * 70)
    print("🩺 Kira Health Assistant - Windows Setup")
    print("=" * 70)
    print()
    
    # Check Python version
    if sys.version_info >= (3, 13):
        print("⚠️  WARNING: You're using Python 3.13 or newer.")
        print("   Some packages may have compatibility issues.")
        print("   Consider using Python 3.11 or 3.12 for local training.")
        print()
        response = input("Continue anyway? (y/n): ").lower().strip()
        if response != 'y':
            print("\n💡 Recommended: Use Google Colab instead (free GPU + no setup issues)")
            print("   Or install Python 3.11: https://www.python.org/downloads/")
            return
    
    print("\n📦 Installing core packages...")
    
    # Core packages that usually work
    core_packages = [
        "torch",
        "transformers==4.36.0",
        "accelerate==0.25.0",
        "datasets==2.16.0",
        "peft==0.7.1",
        "trl==0.7.10",
        "gradio==4.13.0",
        "evaluate==0.4.1",
    ]
    
    for package in core_packages:
        try:
            print(f"\nInstalling {package}...")
            install_package(package)
            print(f"✅ {package}")
        except Exception as e:
            print(f"❌ Failed to install {package}: {e}")
    
    # Optional packages
    print("\n\n📦 Installing optional packages...")
    optional_packages = [
        "rouge-score",
        "protobuf",
        "tqdm",
        "matplotlib",
        "jupyter",
        "ipywidgets"
    ]
    
    for package in optional_packages:
        try:
            print(f"Installing {package}...")
            install_package(package)
            print(f"✅ {package}")
        except Exception as e:
            print(f"⚠️  Optional package {package} failed (not critical)")
    
    # Skip sentencepiece on Windows + Python 3.13
    if sys.platform.startswith('win') and sys.version_info >= (3, 13):
        print("\n⚠️  Skipping sentencepiece (Windows + Python 3.13 compatibility issue)")
        print("   Not required for TinyLlama - tokenizer will work without it")
    else:
        try:
            print("\nInstalling sentencepiece...")
            install_package("sentencepiece")
            print("✅ sentencepiece")
        except:
            print("⚠️  sentencepiece installation failed (not critical for TinyLlama)")
    
    # Skip bitsandbytes on Windows
    if sys.platform.startswith('win'):
        print("\n⚠️  Skipping bitsandbytes (not supported on Windows)")
        print("   To use 4-bit quantization, please use:")
        print("   - Google Colab (recommended)")
        print("   - Linux/WSL")
        print("   - Or train without quantization (requires more GPU memory)")
    else:
        try:
            print("\nInstalling bitsandbytes...")
            install_package("bitsandbytes==0.41.3")
            print("✅ bitsandbytes")
        except:
            print("⚠️  bitsandbytes installation failed")
    
    print("\n\n" + "=" * 70)
    print("✅ Core installation complete!")
    print("=" * 70)
    print()
    print("📝 Important Notes:")
    print()
    if sys.platform.startswith('win'):
        print("🪟 Windows Setup:")
        print("   - bitsandbytes (4-bit quantization) is NOT available on Windows")
        print("   - For full functionality, use Google Colab with GPU")
        print("   - Or use WSL (Windows Subsystem for Linux)")
        print()
    print("🚀 Recommended Next Steps:")
    print("   1. Use Google Colab for training (free GPU, no setup issues)")
    print("   2. Open: kira_health_assistant.ipynb in Colab")
    print("   3. Enable T4 GPU runtime")
    print("   4. Run all cells")
    print()
    print("💡 For local development on Windows:")
    print("   - You can still edit code and notebooks locally")
    print("   - Run training on Colab (takes ~25 minutes)")
    print("   - Download trained model for local inference")
    print()
    print("=" * 70)
    
    # Save installation notes
    with open("WINDOWS_SETUP_NOTES.txt", "w") as f:
        f.write("Kira Health Assistant - Windows Setup Notes\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Python Version: {sys.version}\n")
        f.write(f"Platform: {sys.platform}\n\n")
        f.write("Limitations on Windows:\n")
        f.write("- bitsandbytes not available (4-bit quantization)\n")
        f.write("- sentencepiece may fail on Python 3.13+\n\n")
        f.write("Solution: Use Google Colab for training\n")
        f.write("- Free GPU access\n")
        f.write("- All packages work correctly\n")
        f.write("- Takes ~25 minutes to train\n\n")
        f.write("Colab link: See README.md for Colab badge\n")
    
    print("📄 Setup notes saved to: WINDOWS_SETUP_NOTES.txt")
    print()

if __name__ == "__main__":
    main()
