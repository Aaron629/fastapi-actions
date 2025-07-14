# 使用官方 Python 映像
FROM python:3.12-slim

# 設定工作目錄
WORKDIR /app

# 複製檔案
COPY requirements.txt .
COPY main.py .
COPY model.pkl .

# 安裝相依套件
RUN pip install --no-cache-dir -r requirements.txt

# 開放埠口
EXPOSE 8000

# 啟動指令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
