import os
import subprocess
import sys

def setup_model():
    """
    Setup script to prepare the model for deployment
    """
    print("🚀 Setting up Fake News Detector for deployment...")
    
    # Check if model file exists
    if not os.path.exists('fake_news_detector.h5'):
        print("❌ Model file 'fake_news_detector.h5' not found!")
        print("📝 Please run the Jupyter notebook to train and save the model first.")
        return False
    
    # Install required packages
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages")
        return False
    
    # Download NLTK data
    print("📚 Downloading NLTK data...")
    try:
        import nltk
        nltk.download('stopwords', quiet=True)
        print("✅ NLTK data downloaded!")
    except Exception as e:
        print(f"⚠️ NLTK download warning: {e}")
    
    print("🎉 Setup complete! You can now deploy the application.")
    return True

if __name__ == "__main__":
    setup_model()
