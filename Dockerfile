# 使用官方 Python 映像
FROM python:3.12-slim

# 設定工作目錄
WORKDIR /app

# 複製檔案
COPY requirements.txt .

# 複製應用程式（main.py 和 model.pkl）
COPY app/ .

# 安裝相依套件
RUN pip install --no-cache-dir -r requirements.txt

# 開放埠口
EXPOSE 8000

# 啟動指令
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

