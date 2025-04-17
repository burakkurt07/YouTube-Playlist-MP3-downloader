TR & EN 


# YouTube Playlist MP3 İndirici

Bu Python programı, YouTube oynatma listelerindeki videoları doğrudan MP3 formatında indirmenizi ve video küçük resimlerini (thumbnail) MP3 dosyalarına albüm kapağı olarak eklemenizi sağlar.

## Özellikler

- YouTube oynatma listesindeki tüm videoları otomatik olarak indirir
- Videoları doğrudan yüksek kaliteli MP3 formatına dönüştürür
- Video küçük resimlerini (thumbnail) MP3 dosyalarına albüm kapağı olarak ekler (ayrı dosya olarak kaydetmez)
- Video başlığı ve kanal adını MP3 meta verilerine ekler
- Kullanıcı dostu arayüz ile kolay kullanım

## Gereksinimler

Program aşağıdaki Python kütüphanelerini kullanmaktadır:

- yt-dlp (YouTube video indirme ve dönüştürme)
- ffmpeg (MP3 dönüştürme ve thumbnail ekleme için gerekli)

## Kurulum

1. Python 3.6 veya daha yeni bir sürümün yüklü olduğundan emin olun
2. Gerekli kütüphaneleri yükleyin:

```bash
pip install yt-dlp
```

3. FFmpeg'i yükleyin:
   - Windows: [FFmpeg indirme sayfası](https://ffmpeg.org/download.html)
   - macOS: `brew install ffmpeg`
   - Linux: `sudo apt install ffmpeg`

4. Programı indirin ve çalıştırma izni verin:

```bash
chmod +x youtube_to_mp3_direct.py
```

## Kullanım

Programı çalıştırmak için:

```bash
python youtube_to_mp3_direct.py
```

Program çalıştığında:

1. MP3 dosyalarının kaydedileceği dizini girmeniz istenecek
2. YouTube oynatma listesi URL'sini girmeniz istenecek
3. Video küçük resimlerini (thumbnail) MP3 dosyalarına eklemek isteyip istemediğiniz sorulacak

İndirme işlemi tamamlandıktan sonra, MP3 dosyaları belirttiğiniz dizinde olacaktır. MP3 dosyalarını açtığınızda, video küçük resimleri albüm kapağı olarak görünecektir.

## Örnek Kullanım

```
===== YouTube Oynatma Listesi MP3 İndirici =====

MP3 dosyalarının kaydedileceği dizini girin: /home/kullanici/Muzik
YouTube oynatma listesi URL'sini girin: https://www.youtube.com/playlist?list=PLxxx
Video küçük resimlerini (thumbnail) MP3 dosyalarına eklemek istiyor musunuz? (E/H): E

İndirme işlemi başlatılıyor...

Oynatma listesi indiriliyor: https://www.youtube.com/playlist?list=PLxxx
Dosyalar şuraya kaydedilecek: /home/kullanici/Muzik

[youtube:playlist] PLxxx: Playlist indiriliyor...
[download] Şarkı Adı 1.mp3 indiriliyor...
[download] Şarkı Adı 2.mp3 indiriliyor...
...

İndirme tamamlandı! MP3 dosyaları '/home/kullanici/Muzik' dizinine kaydedildi.
```

## Notlar

- İndirme hızı internet bağlantınıza ve YouTube sunucularının durumuna bağlıdır
- Telif hakkı korumalı içerikleri indirmek yasal kısıtlamalara tabi olabilir
- Program, yalnızca kişisel kullanım için tasarlanmıştır

## Sorun Giderme

- Program çalışmazsa, gerekli kütüphanelerin doğru şekilde yüklendiğinden emin olun
- FFmpeg'in doğru şekilde yüklendiğinden ve PATH'e eklendiğinden emin olun
- YouTube URL'sinin doğru ve erişilebilir olduğundan emin olun
- Kaydetme dizininin yazma izinlerine sahip olduğundan emin olun

## Lisans

Bu program MIT lisansı altında dağıtılmaktadır.

## Katkıda Bulunma

Hata raporları, özellik istekleri ve pull request'ler için GitHub üzerinden iletişime geçebilirsiniz.


EN

# YouTube Playlist MP3 Downloader

This Python script allows you to download all videos in a YouTube playlist directly as high-quality MP3 files and embed their thumbnails as album covers.

## Features

- Automatically downloads all videos from a YouTube playlist
- Converts videos to high-quality MP3 format
- Embeds video thumbnails as album covers (not saved as separate files)
- Adds video title and channel name to MP3 metadata
- Easy-to-use, user-friendly interface

## Requirements

This program depends on the following Python libraries and tools:

- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) – for downloading and converting YouTube videos  
- [`ffmpeg`](https://ffmpeg.org/) – required for MP3 conversion and embedding thumbnails

## Installation

1. Make sure you have Python 3.6 or higher installed.

2. Install the required Python library:

```bash
pip install yt-dlp
Install FFmpeg:

    Windows: Download from the official FFmpeg page

    macOS:

brew install ffmpeg

Linux:

        sudo apt install ffmpeg

    Download the script and make it executable:

chmod +x youtube_to_mp3_direct.py

Usage

To run the script:

python youtube_to_mp3_direct.py

When executed, the script will:

    Ask for the directory to save MP3 files

    Ask for the YouTube playlist URL

    Ask whether to embed video thumbnails as album covers in the MP3 files

Once the process is completed, your MP3 files will be available in the specified directory, complete with album art.
Example Usage

===== YouTube Playlist MP3 Downloader =====

Enter directory to save MP3 files: /home/user/Music
Enter YouTube playlist URL: https://www.youtube.com/playlist?list=PLxxx
Do you want to embed thumbnails into MP3 files? (Y/N): Y

Starting download...

Downloading playlist: https://www.youtube.com/playlist?list=PLxxx
Files will be saved to: /home/user/Music

[youtube:playlist] PLxxx: Downloading playlist...
[download] Song Name 1.mp3 downloading...
[download] Song Name 2.mp3 downloading...
...

Download complete! MP3 files saved to '/home/user/Music'.

Notes

    Download speed depends on your internet connection and YouTube server status

    Downloading copyrighted content may be subject to legal restrictions

    This tool is intended for personal use only

Troubleshooting

    If the program doesn't run, make sure all required libraries are correctly installed

    Ensure FFmpeg is properly installed and added to your system PATH

    Verify that the YouTube URL is valid and accessible

    Make sure the save directory has write permissions

License

This project is licensed under the MIT License.
Contributing

Feel free to open issues or submit pull requests on GitHub for bug reports, feature requests, or 
