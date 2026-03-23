FROM python:3.12-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["sh", "-c", "streamlit run main.py ${PORT:+--server.port=$PORT} --server.address=0.0.0.0"]