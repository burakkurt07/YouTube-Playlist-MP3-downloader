#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
YouTube Playlist MP3 Downloader
-------------------------------
Bu program, YouTube oynatma listesindeki videoları doğrudan MP3 formatında indirir ve
video küçük resimlerini (thumbnail) MP3 dosyalarına albüm kapağı olarak ekler.
"""

import os
import sys
import yt_dlp
import logging

# Logging ayarları
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class YouTubePlaylistDownloader:
    """YouTube oynatma listesinden MP3 indirme ve thumbnail ekleme işlemlerini yönetir."""
    
    def __init__(self):
        """Sınıfı başlat ve gerekli değişkenleri tanımla."""
        self.output_dir = ""
        self.playlist_url = ""
        self.include_thumbnail = True
    
    def validate_directory(self, directory):
        """Dizinin var olup olmadığını kontrol eder, yoksa oluşturmayı dener."""
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
                logger.info(f"Dizin oluşturuldu: {directory}")
                return True
            except Exception as e:
                logger.error(f"Dizin oluşturulamadı: {e}")
                return False
        return True
    
    def download_and_convert(self):
        """Videoları doğrudan MP3'e dönüştürür ve thumbnail'i gömülü olarak ekler."""
        try:
            print(f"\nOynatma listesi indiriliyor: {self.playlist_url}")
            print(f"Dosyalar şuraya kaydedilecek: {self.output_dir}\n")
            
            # yt-dlp seçenekleri
            ydl_opts = {
                'format': 'bestaudio/best',
                'paths': {'home': self.output_dir},
                'outtmpl': {'default': '%(title)s.%(ext)s'},
                'writethumbnail': self.include_thumbnail,
                'postprocessors': [
                    {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    },
                    {
                        'key': 'EmbedThumbnail',
                        # Thumbnail'i dosyaya göm ve ayrı dosya olarak kaydetme
                        'already_have_thumbnail': False,
                    },
                    {
                        'key': 'FFmpegMetadata',
                        'add_metadata': True,
                    },
                ],
                'quiet': False,
                'no_warnings': False,
                'ignoreerrors': True,
                # Playlist işleme
                'extract_flat': False,
                'playlistend': None,  # Tüm oynatma listesini indir
            }
            
            # Thumbnail eklenmeyecekse postprocessor'dan kaldır
            if not self.include_thumbnail:
                ydl_opts['writethumbnail'] = False
                # EmbedThumbnail işlemcisini kaldır
                ydl_opts['postprocessors'] = [pp for pp in ydl_opts['postprocessors'] 
                                             if pp.get('key') != 'EmbedThumbnail']
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                error = ydl.download([self.playlist_url])
                
                if error:
                    logger.warning(f"Bazı videolar indirilemedi. Hata kodu: {error}")
                else:
                    logger.info("Tüm videolar başarıyla indirildi.")
            
            return True
            
        except Exception as e:
            logger.error(f"İndirme hatası: {e}")
            return False
    
    def run(self):
        """Ana çalıştırma fonksiyonu."""
        print("\n===== YouTube Oynatma Listesi MP3 İndirici =====\n")
        
        # Çıkış dizinini al
        while True:
            self.output_dir = input("MP3 dosyalarının kaydedileceği dizini girin: ").strip()
            if self.output_dir and self.validate_directory(self.output_dir):
                break
            print("Geçersiz dizin. Lütfen geçerli bir dizin girin veya oluşturulabilecek bir yol belirtin.")
        
        # Oynatma listesi URL'sini al
        while True:
            self.playlist_url = input("YouTube oynatma listesi URL'sini girin: ").strip()
            if self.playlist_url and ('youtube.com' in self.playlist_url or 'youtu.be' in self.playlist_url):
                break
            print("Geçersiz YouTube URL'si. Lütfen geçerli bir URL girin.")
        
        # Thumbnail seçeneğini al
        thumbnail_choice = input("Video küçük resimlerini (thumbnail) MP3 dosyalarına eklemek istiyor musunuz? (E/H): ").strip().upper()
        self.include_thumbnail = thumbnail_choice != "H"
        
        print("\nİndirme işlemi başlatılıyor...\n")
        
        # İndirme ve dönüştürme işlemini başlat
        if self.download_and_convert():
            print(f"\nİndirme tamamlandı! MP3 dosyaları '{self.output_dir}' dizinine kaydedildi.")
        else:
            print("\nİndirme sırasında hatalar oluştu. Lütfen log dosyasını kontrol edin.")

if __name__ == "__main__":
    try:
        downloader = YouTubePlaylistDownloader()
        downloader.run()
    except KeyboardInterrupt:
        print("\nİşlem kullanıcı tarafından iptal edildi.")
    except Exception as e:
        print(f"\nBeklenmeyen bir hata oluştu: {e}")
        logger.exception("Beklenmeyen hata")
