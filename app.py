import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Set a title through streamlit
st.title("Find Those Most Important Words in Article")

user_input = st.text_area("Enter your text","")

if user_input:
	wordcloud = WordCloud(width=800, height=300, background_color='white').generate(user_input)
	fig, ax = plt.subplots(figsize=(8,4))
	ax.imshow(wordcloud, interpolation='bilinear')
	ax.axis('off')
	st.pyplot(fig)