# 使用官方 Python 3.10 映像檔作為基礎
FROM python:3.10

# 設定工作目錄
WORKDIR /app

# 複製專案內所有檔案到容器
COPY . /app

# 安裝 FastAPI、Uvicorn 及 Redis
RUN pip install --no-cache-dir fastapi uvicorn redis

# 容器啟動時執行 FastAPI 服務
CMD ["uvicorn", "fastapi_test:app", "--host", "0.0.0.0", "--port", "8000"]
