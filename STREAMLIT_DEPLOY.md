# 🚀 Streamlit Cloud Deployment Guide

## ✅ Prerequisites (Already Done!)
- ✅ Trained model (`fake_news_detector.h5`) - READY
- ✅ Streamlit app (`app.py`) - READY  
- ✅ Requirements file (`requirements.txt`) - READY
- ✅ Streamlit config (`.streamlit/config.toml`) - READY

## 🎯 Step-by-Step Deployment

### Step 1: Create GitHub Repository

1. **Go to [GitHub.com](https://github.com) and sign in**

2. **Click "New Repository" (green button)**

3. **Fill in repository details:**
   - Repository name: `fake-news-detector` (or any name you like)
   - Description: `AI-powered fake news detection using LSTM neural networks`
   - Make it **Public** (required for free Streamlit deployment)
   - ✅ Add README file
   - Click **"Create repository"**

### Step 2: Upload Your Files

**Option A: Upload via GitHub Web Interface**
1. In your new repository, click **"uploading an existing file"**
2. Drag and drop ALL files from your `D:\WELFAKE` folder
3. Write commit message: `Add fake news detector app`
4. Click **"Commit changes"**

**Option B: Use Git Commands** (if you prefer command line)
```bash
git init
git add .
git commit -m "Add fake news detector app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/fake-news-detector.git
git push -u origin main
```

### Step 3: Deploy to Streamlit Cloud

1. **Go to [share.streamlit.io](https://share.streamlit.io)**

2. **Sign in with GitHub** (same account you used above)

3. **Click "New app"**

4. **Fill in deployment details:**
   - Repository: Select your `fake-news-detector` repository
   - Branch: `main`
   - Main file path: `app.py`
   - App URL: Choose a custom URL (optional)

5. **Click "Deploy!"**

6. **Wait 2-3 minutes** for deployment to complete

### Step 4: Your App is Live! 🎉

- You'll get a URL like: `https://your-app-name.streamlit.app`
- Share this URL with anyone to test your fake news detector!

## 🔧 Troubleshooting

### If deployment fails:
- Check that `fake_news_detector.h5` was uploaded to GitHub
- Ensure all files are in the repository root (not in subfolders)
- Check the deployment logs in Streamlit Cloud

### If model file is too large:
- GitHub has a 100MB file limit
- If your model is larger, consider using Git LFS or hosting the model elsewhere

## 🎯 After Deployment

1. **Test your app** with different news headlines
2. **Share the URL** with friends and colleagues  
3. **Monitor usage** in Streamlit Cloud dashboard
4. **Update by pushing new commits** to GitHub

Your fake news detector is now live and accessible worldwide! 🌍✨
