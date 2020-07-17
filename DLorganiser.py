import os
import shutil

path = 'D:/Downloads'

os.chdir(f'{path}') # Changes the directory to D:/Downloads

# print(os.getcwd()) # Prints the name of the current directory

# print(f"\n {os.listdir()}") # Lists all items in the current directory

def organiseImage():
    if not os.path.exists('Images'): # Only makes sure this folder exists when attempting to create it and its contents to avoid overwriting
        os.mkdir('Images') # Creates parent directory
        os.chdir(f'{path}/Images') # Switches to parent directory
        os.mkdir('jpg') # Creates children directories
        os.mkdir('png')
        os.mkdir('png_thumb')
        os.mkdir('gif')
        os.mkdir('tiff')
        os.mkdir('psd')
        os.mkdir('ico')
        os.mkdir('svg')
        os.mkdir('bmp')
        os.mkdir('ps')
        os.mkdir('webp')
        os.chdir(f'{path}') # Switches back to master directory to provide environment for other functions
    for file in os.listdir(): # Grabs every file inside master directory
        if file.endswith('.jpg') or file.endswith('.JPG'): # Checks file extension
            shutil.move(f'{path}/{file}', f'{path}/Images/jpg/{file}') # Moves file to appropriate directory
        if file.endswith('.png') or file.endswith('.PNG'):
            shutil.move(f'{path}/{file}', f'{path}/Images/png/{file}')
        if file.endswith('.png_thumb') or file.endswith('.PNG_THUMB'):
            shutil.move(f'{path}/{file}', f'{path}/Images/png_thumb/{file}')
        if file.endswith('.gif') or file.endswith('.GIF'):
            shutil.move(f'{path}/{file}', f'{path}/Images/gif/{file}')
        if file.endswith('.tiff') or file.endswith('.TIFF') or file.endswith('.tif') or file.endswith('.TIF'):
            shutil.move(f'{path}/{file}', f'{path}/Images/tiff/{file}')
        if file.endswith('.psd') or file.endswith('.PSD'):
            shutil.move(f'{path}/{file}', f'{path}/Images/psd/{file}')
        if file.endswith('.ico') or file.endswith('.ICO'):
            shutil.move(f'{path}/{file}', f'{path}/Images/ico/{file}')
        if file.endswith('.svg') or file.endswith('.SVG'):
            shutil.move(f'{path}/{file}', f'{path}/Images/svg/{file}')
        if file.endswith('.bmp') or file.endswith('.BMP'):
            shutil.move(f'{path}/{file}', f'{path}/Images/bmp/{file}')
        if file.endswith('.ps') or file.endswith('.PS'):
            shutil.move(f'{path}/{file}', f'{path}/Images/ps/{file}')
        if file.endswith('.webp') or file.endswith('.WEBP'):
            shutil.move(f'{path}/{file}', f'{path}/Images/webp/{file}')

def organiseText():
    if not os.path.exists('Documents'):
        os.mkdir('Documents')
        os.chdir(f'{path}/Documents')
        os.mkdir('txt')
        os.mkdir('odt')
        os.mkdir('pdf')
        os.mkdir('rtf')
        os.mkdir('tex')
        os.mkdir('wpd')
        os.mkdir('log')
        os.mkdir('cfg')
        os.mkdir('json')
        os.mkdir('xml')
        os.mkdir('dxf')
        os.mkdir('hex')
        os.chdir(f'{path}')
    for file in os.listdir():
        if file.endswith('.txt') or file.endswith('.TXT'):
            shutil.move(f'{path}/{file}', f'{path}/Documents/txt/{file}')
        if file.endswith('.odt') or file.endswith('.ODT'):
            shutil.move(f'{path}/{file}', f'{path}/Documents/odt/{file}')
        if file.endswith('.pdf') or file.endswith('.PDF'):
            shutil.move(f'{path}/{file}', f'{path}/Documents/pdf/{file}')
        if file.endswith('.rtf') or file.endswith('.RTF'):
            shutil.move(f'{path}/{file}', f'{path}/Documents/rtf/{file}')
        if file.endswith('.tex') or file.endswith('.TEX'):
            shutil.move(f'{path}/{file}', f'{path}/Documents/tex/{file}')
        if file.endswith('.wpd') or file.endswith('.WPD'):
            shutil.move(f'{path}/{file}', f'{path}/Documents/wpd/{file}')
        if file.endswith('.log') or file.endswith('.LOG'):
            shutil.move(f'{path}/{file}', f'{path}/Documents/log/{file}')
        if file.endswith('.cfg') or file.endswith('.CFG'):
            shutil.move(f'{path}/{file}', f'{path}/Documents/cfg/{file}')
        if file.endswith('.json') or file.endswith('.JSON'):
            shutil.move(f'{path}/{file}', f'{path}/Documents/json/{file}')
        if file.endswith('.xml') or file.endswith('.XML'):
            shutil.move(f'{path}/{file}', f'{path}/Documents/xml/{file}')
        if file.endswith('.dxf') or file.endswith('.DXF'):
            shutil.move(f'{path}/{file}', f'{path}/Documents/dxf/{file}')
        if file.endswith('.hex') or file.endswith('.HEX'):
            shutil.move(f'{path}/{file}', f'{path}/Documents/hex/{file}')

def organiseOffice():
    if not os.path.exists('Microsoft Office'):
        os.mkdir('Microsoft Office')
        os.chdir(f'{path}/Microsoft Office')
        os.mkdir('Word')
        os.mkdir('Powerpoint')
        os.mkdir('Excel')
        os.mkdir('Publisher')
        os.chdir(f'{path}')
    for file in os.listdir():
        if file.endswith('.doc') or file.endswith('.DOC') or file.endswith('.docx') or file.endswith('.DOCX'):
            shutil.move(f'{path}/{file}', f'{path}/Microsoft Office/Word/{file}')
        if file.endswith('.key') or file.endswith('.KEY') or file.endswith('.odp') or file.endswith('.ODP') or file.endswith('.pps') or file.endswith('.PPS') or file.endswith('.ppt') or file.endswith('.PPT') or file.endswith('.pptx') or file.endswith('.PPTX'):
            shutil.move(f'{path}/{file}', f'{path}/Microsoft Office/Powerpoint/{file}')
        if file.endswith('.ods') or file.endswith('.ODS') or file.endswith('.xls') or file.endswith('.XLS') or file.endswith('.xlsm') or file.endswith('.XLSM') or file.endswith('.xlsx') or file.endswith('.xlsx'):
            shutil.move(f'{path}/{file}', f'{path}/Microsoft Office/Excel/{file}')
        if file.endswith('.pub') or file.endswith('.PUB'):
            shutil.move(f'{path}/{file}', f'{path}/Microsoft Office/Publisher/{file}')

def organiseVideo():
    if not os.path.exists('Video'):
        os.mkdir('Video')
        os.chdir(f'{path}/Video')
        os.mkdir('avi')
        os.mkdir('flv')
        os.mkdir('h264')
        os.mkdir('m4v')
        os.mkdir('mkv')
        os.mkdir('mov')
        os.mkdir('mp4')
        os.mkdir('mpg')
        os.mkdir('wmv')
        os.chdir(f'{path}')
    for file in os.listdir():
        if file.endswith('.avi') or file.endswith('.AVI'):
            shutil.move(f'{path}/{file}', f'{path}/Video/avi/{file}')
        if file.endswith('.flv') or file.endswith('.FLV'):
            shutil.move(f'{path}/{file}', f'{path}/Video/flv/{file}')
        if file.endswith('.h264') or file.endswith('.H264'):
            shutil.move(f'{path}/{file}', f'{path}/Video/h264/{file}')
        if file.endswith('.m4v') or file.endswith('.M4V'):
            shutil.move(f'{path}/{file}', f'{path}/Video/m4v/{file}')
        if file.endswith('.mkv') or file.endswith('.MKV'):
            shutil.move(f'{path}/{file}', f'{path}/Video/mkv/{file}')
        if file.endswith('.mov') or file.endswith('.MOV'):
            shutil.move(f'{path}/{file}', f'{path}/Video/mov/{file}')
        if file.endswith('.mp4') or file.endswith('.MP4'):
            shutil.move(f'{path}/{file}', f'{path}/Video/mp4/{file}')
        if file.endswith('.mpg') or file.endswith('.MPG'):
            shutil.move(f'{path}/{file}', f'{path}/Video/mpg/{file}')
        if file.endswith('.wmv') or file.endswith('.WMV'):
            shutil.move(f'{path}/{file}', f'{path}/Video/wmv/{file}')

def organiseAudio():
    if not os.path.exists('Audio'):
        os.mkdir('Audio')
        os.chdir(f'{path}/Audio')
        os.mkdir('aif')
        os.mkdir('cda')
        os.mkdir('midi')
        os.mkdir('mp3')
        os.mkdir('mpa')
        os.mkdir('wav')
        os.mkdir('wma')
        os.mkdir('wpl')
        os.chdir(f'{path}')
    for file in os.listdir():
        if file.endswith('.aif') or file.endswith('.AIF'):
            shutil.move(f'{path}/{file}', f'{path}/Audio/aif/{file}')
        if file.endswith('.cda') or file.endswith('.CDA'):
            shutil.move(f'{path}/{file}', f'{path}/Audio/cda/{file}')
        if file.endswith('.midi') or file.endswith('.MIDI'):
            shutil.move(f'{path}/{file}', f'{path}/Audio/midi/{file}')
        if file.endswith('.mp3') or file.endswith('.MP3'):
            shutil.move(f'{path}/{file}', f'{path}/Audio/mp3/{file}')
        if file.endswith('.mpa') or file.endswith('MPA'):
            shutil.move(f'{path}/{file}', f'{path}/Audio/mpa/{file}')
        if file.endswith('.wav') or file.endswith('.WAV'):
            shutil.move(f'{path}/{file}', f'{path}/Audio/wav/{file}')
        if file.endswith('.wma') or file.endswith('.WMA'):
            shutil.move(f'{path}/{file}', f'{path}/Audio/wma/{file}')
        if file.endswith('.wpl') or file.endswith('.WPL'):
            shutil.move(f'{path}/{file}', f'{path}/Audio/wpl/{file}')

def organiseApp():
    if not os.path.exists('Apps'):
        os.mkdir('Apps')
        os.chdir(f'{path}/Apps')
        os.mkdir('exe')
        os.mkdir('bat')
        os.mkdir('ahk')
        os.mkdir('gb')
        os.mkdir('gbc')
        os.mkdir('gba')
        os.mkdir('ipa')
        os.mkdir('msi')
        os.mkdir('iso')
        os.chdir(f'{path}')
    for file in os.listdir():
        if file.endswith('.exe') or file.endswith('.EXE'):
            shutil.move(f'{path}/{file}', f'{path}/Apps/exe/{file}')
        if file.endswith('.bat') or file.endswith('.BAT'):
            shutil.move(f'{path}/{file}', f'{path}/Apps/bat/{file}')
        if file.endswith('.apk') or file.endswith('.APK'):
            shutil.move(f'{path}/{file}', f'{path}/Apps/apk/{file}')
        if file.endswith('.wsf') or file.endswith('.WSF'):
            shutil.move(f'{path}/{file}', f'{path}/Apps/wsf/{file}')
        if file.endswith('.ahk') or file.endswith('.AHK'):
            shutil.move(f'{path}/{file}', f'{path}/Apps/ahk/{file}')
        if file.endswith('.gb') or file.endswith('.GB'):
            shutil.move(f'{path}/{file}', f'{path}/Apps/gb/{file}')
        if file.endswith('.gbc') or file.endswith('.GBC'):
            shutil.move(f'{path}/{file}', f'{path}/Apps/gbc/{file}')
        if file.endswith('.gba') or file.endswith('.GBA'):
            shutil.move(f'{path}/{file}', f'{path}/Apps/gba/{file}')
        if file.endswith('.ipa') or file.endswith('.IPA'):
            shutil.move(f'{path}/{file}', f'{path}/Apps/ipa/{file}')
        if file.endswith('.msi') or file.endswith('.MSI'):
            shutil.move(f'{path}/{file}', f'{path}/Apps/msi/{file}')
        if file.endswith('.iso') or file.endswith('.ISO'):
            shutil.move(f'{path}/{file}', f'{path}/Apps/iso/{file}')

def organiseArchive():
    if not os.path.exists('Archives'):
        os.mkdir('Archives')
        os.chdir(f'{path}/Archives')
        os.mkdir('zip')
        os.mkdir('7z')
        os.mkdir('rar')
        os.mkdir('gz')
        os.chdir(f'{path}')
    for file in os.listdir():
        if file.endswith('.zip') or file.endswith('.ZIP'):
            shutil.move(f'{path}/{file}', f'{path}/Archives/zip/{file}')
        if file.endswith('.7z') or file.endswith('.7Z'):
            shutil.move(f'{path}/{file}', f'{path}/Archives/7z/{file}')
        if file.endswith('.rar') or file.endswith('.RAR'):
            shutil.move(f'{path}/{file}', f'{path}/Archives/rar/{file}')
        if file.endswith('.gz') or file.endswith('.GZ'):
            shutil.move(f'{path}/{file}', f'{path}/Archives/gz/{file}')

def organiseMods():
    if not os.path.exists('Minecraft Mods'):
        os.mkdir('Minecraft Mods')
        os.chdir(f'{path}/Minecraft Mods')
        os.chdir(f'{path}')
    for file in os.listdir():
        if file.endswith('.jar') or file.endswith('.JAR'):
            shutil.move(f'{path}/{file}', f'{path}/Minecraft Mods/{file}')

def organiseCode():
    if not os.path.exists('Programming'):
        os.mkdir('Programming')
        os.chdir(f'{path}/Programming')
        os.mkdir('py')
        os.mkdir('js')
        os.mkdir('html')
        os.mkdir('css')
        os.mkdir('jsp')
        os.mkdir('php')
        os.mkdir('c')
        os.mkdir('cpp')
        os.mkdir('cs')
        os.mkdir('jupyter')
        os.mkdir('ino')
        os.chdir(f'{path}')
        for file in os.listdir():
            if file.endswith('.py') or file.endswith('.PY'):
                shutil.move(f'{path}/{file}', f'{path}/Programming/py/{file}')
            if file.endswith('.js') or file.endswith('.JS'):
                shutil.move(f'{path}/{file}', f'{path}/Programming/js/{file}')
            if file.endswith('.html') or file.endswith('.HTML') or file.endswith('.htm') or file.endswith('.HTM') or file.endswith('.xhtml') or file.endswith('.XHTML') or file.endswith('.chm') or file.endswith('.CHM'):
                shutil.move(f'{path}/{file}', f'{path}/Programming/html/{file}')
            if file.endswith('.css') or file.endswith('.CSS'):
                shutil.move(f'{path}/{file}', f'{path}/Programming/css/{file}')
            if file.endswith('.jsp') or file.endswith('.JSP'):
                shutil.move(f'{path}/{file}', f'{path}/Programming/jsp/{file}')
            if file.endswith('.php') or file.endswith('.PHP') or file.endswith('.php4') or file.endswith('.PHP4') or file.endswith('.php3') or file.endswith('.PHP3'):
                shutil.move(f'{path}/{file}', f'{path}/Programming/php/{file}')
            if file.endswith('.c') or file.endswith('.C'):
                shutil.move(f'{path}/{file}', f'{path}/Programming/c/{file}')
            if file.endswith('.cpp') or file.endswith('.CPP'):
                shutil.move(f'{path}/{file}', f'{path}/Programming/cpp/{file}')
            if file.endswith('.cs') or file.endswith('.CS'):
                shutil.move(f'{path}/{file}', f'{path}/Programming/cs/{file}')
            if file.endswith('.ipynb') or file.endswith('.IPYNB'):
                shutil.move(f'{path}/{file}', f'{path}/Programming/jupyter/{file}')
            if file.endswith('.ino') or file.endswith('.INO'):
                shutil.move(f'{path}/{file}', f'{path}/Programming/ino/{file}')

def organiseOther():
    if not os.path.exists('Other'):
        os.mkdir('Other')
        os.chdir(f'{path}/Other')
        os.mkdir('torrents')
        os.mkdir('rainmeter')
        os.mkdir('anki')
        os.mkdir('ica')
        os.chdir(f'{path}')
        for file in os.listdir():
            if file.endswith('.torrent') or file.endswith('.TORRENT'):
                shutil.move(f'{path}/{file}', f'{path}/Other/torrents/{file}')
            if file.endswith('.rmskin') or file.endswith('.RMSKIN'):
                shutil.move(f'{path}/{file}', f'{path}/Other/rainmeter/{file}')
            if file.endswith('.apkg') or file.endswith('.APKG'):
                shutil.move(f'{path}/{file}', f'{path}/Other/anki/{file}')
            if file.endswith('.ica') or file.endswith('.ICA'):
                shutil.move(f'{path}/{file}', f'{path}/Other/ica/{file}')

def organise():
    organiseImage()
    organiseText()
    organiseOffice()
    organiseVideo()
    organiseAudio()
    organiseApp()
    organiseArchive()
    organiseMods()
    organiseCode()
    organiseOther()

organise()