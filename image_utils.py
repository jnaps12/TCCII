from PIL import Image
import os
from pathlib import Path
from rembg import remove

directory = './renamed'


def resize_images(dir):
    width = 640
    height = 480

    splited_dir = dir.split('/')
    dir_name = splited_dir[1]
    count = 0
    for image in os.scandir(dir):
        file_extension = Path(image).suffix
        if image.is_file() and (file_extension == '.jpg' or file_extension == '.JPG' ):
            print(f"{count} - Redimensionando {image.name}")
            img = Image.open(image.path)
            img_resized = img.resize((width, height))
            img_resized.save(f'./dataset_resized2/{image.name}')
            count += 1
    
    

def remove_background(dir):
    splited_dir = dir.split('/')
    dir_name = splited_dir[1]
    
    for image in os.scandir(dir):
        file_extension = Path(image).suffix
        if image.is_file() and file_extension == '.jpg':
            print(f"Removendo fundo {image.name}")
            img = Image.open(image.path)
            output = remove(img)
            output = output.convert('RGB')
            output.save(f'./rem/{image.name}')
    


def rename_files(dir):
    arquivos = os.listdir(dir)
    nova_extensao = ".jpg"
    count = 1262
    index = 1

    for arquivo in arquivos:
        # Criar o novo nome do arquivo com a nova extensão
        novo_nome = "healthy_" + str(count) + nova_extensao
        # Renomear o arquivo
        os.rename(f'./dataset_resized2/{arquivo}', f'./renamed/{novo_nome}')
        count += 1
        index += 1

remove_background(directory)
# resize_images(directory)
# rename_files('./dataset_resized2')
