FROM python:3.12-slim
WORKDIR /app

RUN pip install --no-cache-dir \
        torch==2.6.0 \
        --index-url https://download.pytorch.org/whl/cpu

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/app

EXPOSE 8002
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]