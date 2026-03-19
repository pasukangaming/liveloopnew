# Gunakan image python yang ringan
FROM python:3.9-slim

# Install FFmpeg (Wajib ada untuk streaming)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Copy semua file ke dalam container
WORKDIR /app
COPY . .

# Jalankan script utama
CMD ["python", "main.py"]