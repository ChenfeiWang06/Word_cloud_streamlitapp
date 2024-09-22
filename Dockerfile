FROM python:3.9-slim

WORKDIR /app

# Install required packages
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y build-essential
RUN pip install --no-cache-dir -r requirements.txt


# Copy the app
COPY app.py /app/

# Expose the Streamlit port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
