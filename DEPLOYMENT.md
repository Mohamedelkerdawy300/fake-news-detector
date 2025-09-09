# 🚀 Deployment Guide

## Prerequisites
1. **Train your model**: Run `WEL_FAKE.ipynb` completely to generate `fake_news_detector.h5`
2. **Test locally**: Make sure everything works with `streamlit run app.py`

---

## 🌐 Option 1: Streamlit Cloud (FREE & EASIEST)

**Perfect for**: Quick sharing, demos, portfolios

### Steps:
1. **Create a GitHub repository** and push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/fake-news-detector.git
   git push -u origin main
   ```

2. **Go to [share.streamlit.io](https://share.streamlit.io)**

3. **Connect your GitHub** and select your repository

4. **Set main file path**: `app.py`

5. **Deploy!** Your app will be live at `https://yourusername-fake-news-detector-app-xyz.streamlit.app`

**⚠️ Note**: Upload your model file `fake_news_detector.h5` to GitHub (or use Git LFS for large files)

---

## 🐳 Option 2: Docker (ANY PLATFORM)

**Perfect for**: Local development, self-hosting

### Quick Start:
```bash
# Build and run with Docker Compose
docker-compose up --build

# Access:
# Web App: http://localhost:8501
# API: http://localhost:5000
```

### Manual Docker:
```bash
# Build image
docker build -t fake-news-detector .

# Run web app
docker run -p 8501:8501 fake-news-detector

# Run API
docker run -p 5000:5000 fake-news-detector python api.py
```

---

## 🚂 Option 3: Railway (FREE TIER)

**Perfect for**: Production apps, custom domains

### Steps:
1. **Sign up at [railway.app](https://railway.app)**

2. **Connect GitHub** and select your repo

3. **Railway auto-detects** the config from `railway.toml`

4. **Add environment variables** (if needed):
   - `PYTHON_VERSION=3.11`

5. **Deploy!** You'll get a URL like `https://your-app.railway.app`

---

## 🟣 Option 4: Heroku

**Perfect for**: Traditional hosting, add-ons

### Steps:
1. **Install Heroku CLI** and login:
   ```bash
   heroku login
   ```

2. **Create Heroku app**:
   ```bash
   heroku create your-fake-news-detector
   ```

3. **Deploy**:
   ```bash
   git push heroku main
   ```

4. **Scale web dyno**:
   ```bash
   heroku ps:scale web=1
   ```

---

## ☁️ Option 5: Other Cloud Platforms

### Google Cloud Run:
```bash
gcloud run deploy --source .
```

### AWS App Runner:
- Connect GitHub repo
- Use `Dockerfile` for deployment

### Azure Container Instances:
```bash
az container create --resource-group myResourceGroup --name fake-news-detector --image your-image
```

---

## 📊 Deployment Comparison

| Platform | Cost | Ease | Performance | Custom Domain |
|----------|------|------|-------------|---------------|
| Streamlit Cloud | Free | ⭐⭐⭐⭐⭐ | Good | Limited |
| Railway | Free tier | ⭐⭐⭐⭐ | Excellent | Yes |
| Heroku | Free tier ending | ⭐⭐⭐ | Good | Yes |
| Docker (Self-host) | Your server | ⭐⭐ | Depends | Yes |

---

## 🔧 Troubleshooting

### Model File Too Large for Git
If `fake_news_detector.h5` is too large (>100MB):

1. **Use Git LFS**:
   ```bash
   git lfs track "*.h5"
   git add .gitattributes
   git add fake_news_detector.h5
   git commit -m "Add model with LFS"
   ```

2. **Or use cloud storage**:
   - Upload to Google Drive/Dropbox
   - Modify `app.py` to download on startup

### Memory Issues
If deployment fails due to memory:
- Use smaller model architecture
- Reduce vocabulary size
- Consider model quantization

### NLTK Data Issues
Add to your app startup:
```python
import nltk
nltk.download('stopwords', quiet=True)
```

---

## 🎯 Recommended Approach

**For beginners**: Start with **Streamlit Cloud**
**For production**: Use **Railway** or **Docker**
**For learning**: Try **Docker** locally first

---

## 📱 After Deployment

1. **Test your deployed app** with various inputs
2. **Share the URL** with friends/colleagues
3. **Monitor usage** through platform dashboards
4. **Update model** by retraining and redeploying

**Your app will be live and accessible to anyone with the URL! 🎉**
