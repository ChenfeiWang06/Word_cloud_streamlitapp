# Word Cloud Generator

This app allows users to upload a paragraph of text, and it generates a word cloud based on the content. The application is built using Streamlit and Docker, making it easy to deploy and run anywhere.

## Features:
- Upload a text file or enter text directly into the app.
- Generates a dynamic word cloud based on the frequency of words in the content.
- Easily containerized with Docker for portability and reproducibility.

## How to Run the App:
I have already uploaded this to my dockerhub. So, if you want to try the app, you can pull the Docker image and run it locally with the following commands:
```bash
  docker pull miffyeewang/nlp_wordcloud_app:latest
  docker run -d -p 8501:8501 miffyeewang/nlp_wordcloud_app:latest
```
You will have the port to open my app.

