import streamlit as st
from wordcloud import WordCloud
from collections import Counter
from textblob import TextBlob
import matplotlib.pyplot as plt

st.set_page_config(page_title="Text Visualizations", layout="wide")
st.title("📊 Text Visualizations App")

# Text input
st.sidebar.header("Input Text")
text = st.sidebar.text_area("Paste your text here:", 
                            "Streamlit makes it easy to build apps with Python. Streamlit is fun and interactive.")

# Tabs for three visualizations
tab1, tab2, tab3 = st.tabs(["☁️ Word Cloud", "📈 Word Frequency", "😊 Sentiment Analysis"])

# --- Tab 1: Word Cloud ---
with tab1:
    st.subheader("Word Cloud")
    if text.strip():
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)

# --- Tab 2: Word Frequency ---
with tab2:
    st.subheader("Top 10 Word Frequencies")
    if text.strip():
        words = text.lower().split()
        word_counts = Counter(words)
        common_words = word_counts.most_common(10)
        labels, values = zip(*common_words)

        fig, ax = plt.subplots()
        ax.bar(labels, values)
        plt.xticks(rotation=45)
        st.pyplot(fig)

# --- Tab 3: Sentiment Analysis ---
with tab3:
    st.subheader("Sentiment Analysis")
    if text.strip():
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            labels = ['Positive', 'Negative']
            sizes = [polarity, 1 - polarity]
        elif polarity < 0:
            labels = ['Negative', 'Positive']
            sizes = [-polarity, 1 + polarity]
        else:
            labels = ['Neutral']
            sizes = [1]

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis("equal")
        st.pyplot(fig)
