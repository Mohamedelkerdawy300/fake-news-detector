import streamlit as st
import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Download required NLTK data
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Initialize components
ps = PorterStemmer()
vocab_size = 10000
sent_length = 20

# Load the trained model
@st.cache_resource
def load_trained_model():
    try:
        model = load_model('fake_news_detector.h5')
        return model
    except FileNotFoundError:
        st.error("""
        🚨 **Model file not found!**
        
        The trained model 'fake_news_detector.h5' is missing. To fix this:
        1. Run the Jupyter notebook `WEL_FAKE.ipynb` completely
        2. Make sure the last cell saves the model
        3. Upload the model file to your deployment
        """)
        return None
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def predict_fake_news(text, model):
    """
    Predict if a news article is fake or real
    """
    # Preprocess the text (same steps as training)
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    
    # Convert to one-hot representation
    one_hot_words = one_hot(review, vocab_size)
    
    # Pad the sequence
    embedded_words = pad_sequences([one_hot_words], padding='pre', maxlen=sent_length)
    
    # Make prediction
    prediction = model.predict(embedded_words, verbose=0)[0][0]
    
    # Convert to human readable format
    if prediction > 0.5:
        result = "🚨 FAKE NEWS"
        confidence = prediction * 100
        color = "red"
    else:
        result = "✅ REAL NEWS"
        confidence = (1 - prediction) * 100
        color = "green"
    
    return result, confidence, color

# Streamlit App
def main():
    st.set_page_config(
        page_title="Fake News Detector",
        page_icon="📰",
        layout="centered"
    )
    
    st.title("🔍 Fake News Detector")
    st.markdown("### Powered by LSTM Neural Network")
    st.markdown("Enter a news headline or article text to check if it's likely to be fake or real.")
    
    # Load model
    model = load_trained_model()
    
    if model is not None:
        # Text input
        st.markdown("---")
        text_input = st.text_area(
            "📝 Enter news text or headline:",
            placeholder="Type or paste the news article text here...",
            height=150
        )
        
        # Predict button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            predict_button = st.button("🔍 Analyze News", type="primary")
        
        if predict_button and text_input.strip():
            with st.spinner("Analyzing..."):
                try:
                    result, confidence, color = predict_fake_news(text_input, model)
                    
                    # Display results
                    st.markdown("---")
                    st.markdown("### 📊 Analysis Results")
                    
                    # Create columns for better layout
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if color == "red":
                            st.error(f"**{result}**")
                        else:
                            st.success(f"**{result}**")
                    
                    with col2:
                        st.metric("Confidence", f"{confidence:.1f}%")
                    
                    # Confidence bar
                    progress_color = "red" if color == "red" else "green"
                    st.progress(confidence/100)
                    
                    # Additional info
                    st.markdown("---")
                    st.info("""
                    **ℹ️ How it works:**
                    - This model was trained on the WELFake dataset
                    - It uses LSTM neural networks to analyze text patterns
                    - Model accuracy: ~89% on test data
                    - Results are predictions and should be used as guidance only
                    """)
                    
                except Exception as e:
                    st.error(f"Error during prediction: {str(e)}")
        
        elif predict_button and not text_input.strip():
            st.warning("Please enter some text to analyze!")
        
        # Example texts
        st.markdown("---")
        st.markdown("### 📝 Try these examples:")
        
        examples = [
            "Scientists discover revolutionary cure for cancer using artificial intelligence",
            "Local weather forecast shows sunny skies for the weekend",
            "BREAKING: World leaders announce shocking secret agreement",
            "Stock market closes with modest gains amid economic uncertainty"
        ]
        
        for i, example in enumerate(examples):
            if st.button(f"Example {i+1}: {example[:50]}...", key=f"example_{i}"):
                st.text_area("📝 Enter news text or headline:", value=example, height=150, key=f"filled_{i}")
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center'>
            <p>Built with ❤️ using Streamlit and TensorFlow</p>
            <p><small>Model trained on WELFake dataset for educational purposes</small></p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
