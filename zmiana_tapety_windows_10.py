import os
import shutil


# pamiętaj żeby dodać userów w ścieżce różnych które mają mieć zmienioną tapetę

wallpaper_dir = r'C:\Users\kamil\AppData\Roaming\Microsoft\Windows\Themes'
#wallpaper_dir_SP1-3
#wallpaper_dir_liceum


# zmiana folderu tam gdzie system przechowuje tapetę
os.chdir(wallpaper_dir)
# pobranie tapety na windows 10 --> ważne żeby plik nazywał się Transco...
os.system('curl --output TranscodedWallpaper --url https://wallpaperaccess.com/full/1139033.jpg')
#kopiowanie pliku do podfolderu cache
shutil.copyfile('./TranscodedWallpaper', './CachedFiles/CachedImage_1024_768_POS_4.jpg')
os.system('RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True')
