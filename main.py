import os
import time
import subprocess

# Mengambil data dari Environment Variables Railway
# Jika variabel tidak ditemukan, dia akan pakai nilai default (opsional)
VIDEO_URL = os.getenv("VIDEO_URL")
STREAM_URL = os.getenv("STREAM_URL", "rtmp://a.rtmp.youtube.com/live2")
STREAM_KEY = os.getenv("STREAM_KEY")

def start_streaming():
    if not VIDEO_URL or not STREAM_KEY:
        print("❌ ERROR: VIDEO_URL atau STREAM_KEY belum di-set di Variables Railway!")
        return

    # Perintah FFmpeg
    cmd = [
        'ffmpeg', '-re', '-stream_loop', '-1', '-i', VIDEO_URL,
        '-c:v', 'libx264', '-preset', 'veryfast', '-b:v', '3000k',
        '-maxrate', '3000k', '-bufsize', '6000k', '-pix_fmt', 'yuv420p',
        '-g', '50', '-c:a', 'aac', '-b:a', '128k', '-ar', '44100',
        '-f', 'flv', f"{STREAM_URL}/{STREAM_KEY}"
    ]

    while True:
        print(f"🚀 Memulai Stream: {VIDEO_URL}")
        process = subprocess.Popen(cmd)
        process.wait() 
        
        print("⚠️ Koneksi terputus/Error. Mencoba reconnect dalam 10 detik...")
        time.sleep(10)

if __name__ == "__main__":
    start_streaming()