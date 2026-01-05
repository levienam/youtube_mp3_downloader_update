import pyperclip
import time
import yt_dlp

def is_youtube_link(text):
    return "youtube.com/watch?v=" in text or "youtu.be/" in text

def download_audio(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': False,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print(f"✅ Audio téléchargé pour : {link}")

print("🎧 Copie un lien YouTube dans ton presse‑papier...")

last_link = ""

while True:
    clip = pyperclip.paste()
    if clip != last_link and is_youtube_link(clip):
        print(f"🔗 Lien détecté : {clip}")
        download_audio(clip)
        last_link = clip
        # 🔴 On sort de la boucle après un téléchargement
        break
    time.sleep(2)

print("⏸️ Téléchargement terminé. Relance le script pour un nouveau lien.")
