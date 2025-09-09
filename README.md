# 🔍 Fake News Detector

A machine learning-powered fake news detection system using LSTM neural networks, trained on the WELFake dataset.

## 📊 Model Performance
- **Accuracy**: ~89% on test data
- **Architecture**: Bidirectional LSTM with Embedding and Dropout layers
- **Dataset**: WELFake dataset with 71,537 samples

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the Model (if not already done)
Run the Jupyter notebook `WEL_FAKE.ipynb` to train and save the model:
```bash
jupyter notebook WEL_FAKE.ipynb
```

### 3. Run the Web Interface
```bash
streamlit run app.py
```
Then open your browser to `http://localhost:8501`

### 4. Run the API Server
```bash
python api.py
```
The API will be available at `http://localhost:5000`

## 🌐 Usage Options

### Option 1: Web Interface (Streamlit)
- Easy-to-use graphical interface
- Real-time predictions
- Example texts included
- Visual confidence indicators

### Option 2: REST API
Perfect for integrating with other applications:

#### Single Prediction
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Your news text here"}'
```

#### Batch Predictions
```bash
curl -X POST http://localhost:5000/batch_predict \
  -H "Content-Type: application/json" \
  -d '{"texts": ["News text 1", "News text 2"]}'
```

### Option 3: Direct Python Usage
```python
from tensorflow.keras.models import load_model
import numpy as np
# ... (use the predict_fake_news function from the notebook)

model = load_model('fake_news_detector.h5')
result, confidence = predict_fake_news("Your news text here")
print(f"Prediction: {result} (Confidence: {confidence:.2f}%)")
```

## 📱 API Endpoints

- `GET /` - API information
- `GET /health` - Health check
- `POST /predict` - Single text prediction
- `POST /batch_predict` - Multiple texts prediction

### Example API Response
```json
{
  "text": "Breaking news about amazing discovery",
  "prediction": "FAKE",
  "confidence": 78.5,
  "is_fake": true
}
```

## 🛠️ Files Structure

- `WEL_FAKE.ipynb` - Main training notebook
- `WELFake_Dataset.csv` - Training dataset
- `fake_news_detector.h5` - Trained model (generated after training)
- `app.py` - Streamlit web interface
- `api.py` - Flask REST API
- `requirements.txt` - Dependencies

## 🔧 Troubleshooting

### Model Not Found Error
If you get "Model file not found":
1. Run the Jupyter notebook completely
2. Make sure the last cell saves the model as 'fake_news_detector.h5'
3. Check that the file exists in your working directory

### NLTK Data Error
If you get NLTK data errors:
```python
import nltk
nltk.download('stopwords')
```

### Port Already in Use
If port 5000 or 8501 is busy:
- For API: Change port in `api.py` (line with `app.run`)
- For Streamlit: Use `streamlit run app.py --server.port 8502`

## 📈 Model Details

- **Input**: News article text/headlines
- **Preprocessing**: Text cleaning, stemming, stopword removal
- **Encoding**: One-hot encoding with vocabulary size 10,000
- **Sequence Length**: 20 words (padded/truncated)
- **Architecture**: 
  - Embedding layer (40 dimensions)
  - Bidirectional LSTM (100 units)
  - Dropout (0.3)
  - Dense output layer (sigmoid activation)

## ⚠️ Disclaimer

This model is for educational purposes. Always verify news from multiple reliable sources. The model's predictions should be used as guidance only and not as definitive truth.

## 🤝 Contributing

Feel free to improve the model, add features, or fix bugs! Some ideas:
- Add more preprocessing techniques
- Experiment with different architectures
- Create a mobile app interface
- Add news source analysis
- Implement explainable AI features
