import os
import shutil

path = 'G:/home school work'

os.chdir(f'{path}') # Changes the directory to D:/Downloads

def organiseSchool():
    if not os.path.exists('English'): # Only makes sure this folder exists when attempting to create it and its contents to avoid overwriting
        os.mkdir('English')
    if not os.path.exists('Science'):
        os.mkdir('Science')
    if not os.path.exists('French'):
        os.mkdir('French')
    if not os.path.exists('RE'):
        os.mkdir('RE')
    if not os.path.exists('History'):
        os.mkdir('History')
    if not os.path.exists('Geography'):
        os.mkdir('Geography')
    for file in os.listdir(): # Grabs every file inside master directory
        if file.startswith('en ') or file.startswith('EN '):
            shutil.move(f'{path}/{file}', f'{path}/English/{file}')
            print("Organised English")
        if file.startswith('sc ') or file.startswith('SC '):
            shutil.move(f'{path}/{file}', f'{path}/Science/{file}')
            print("Organised Science")
        if file.startswith('fr ') or file.startswith('FR '):
            shutil.move(f'{path}/{file}', f'{path}/French/{file}')
            print("Organised French")
        if file.startswith('re ') or file.startswith('RE '):
            shutil.move(f'{path}/{file}', f'{path}/RE/{file}')
            print("Organised RE")
        if file.startswith('hi ') or file.startswith('HI '):
            shutil.move(f'{path}/{file}', f'{path}/History/{file}')
            print("Organised History")
        if file.startswith('gg ') or file.startswith('GG '):
            shutil.move(f'{path}/{file}', f'{path}/Geography/{file}')
            print("Organised Geography")
        print("ORGANISED FOLDER")

organiseSchool()
