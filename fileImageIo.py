# -*- coding: utf-8 -*-
from scipy import misc
from tkinter import filedialog
import os


'''
    Open an image
    msg = Message to show to user
    flaten = if grayscaleImg
    mode = type of the image -> RGB,
    * 'L' (8-bit pixels, black and white)
    * 'P' (8-bit pixels, mapped to any other mode using a color palette)
    * 'RGB' (3x8-bit pixels, true color)
    * 'RGBA' (4x8-bit pixels, true color with transparency mask)
    * 'CMYK' (4x8-bit pixels, color separation)
    * 'YCbCr' (3x8-bit pixels, color video format)
    * 'I' (32-bit signed integer pixels)
    * 'F' (32-bit floating point pixels)
'''
def open_image(msg,flatten=False, mode=None):
    file_path = filedialog.askopenfilename(initialdir="d:/", title=msg)
    return misc.imread(file_path,flatten=flatten, mode=mode), file_path

def saveimg(file,arr):
    misc.imsave(file,arr)

def openfile(msg):
    file_path = filedialog.askopenfilename(initialdir="d:/", title=msg)
    return file_path

def returnFolder(msg):
    pasta = filedialog.askdirectory(initialdir="d:/", title=msg)
    return pasta

# abre uma relação de arquivos do tipo imagem em uma pasta (extensões possíveis .jpg, .png e .bmp
# msg = mensagem para o Título da caixa de diálogo
def openImgFolder(msg):
    pasta = filedialog.askdirectory(initialdir="d:/", title=msg)
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    imgs = [arq for arq in arquivos if
            arq.lower().endswith(".jpg") or arq.lower().endswith(".png") or arq.lower().endswith(".bmp") or arq.lower().endswith(".jpeg")]
    return imgs

# abre uma relação de arquivos em uma pasta de uma extensão especificada (ex.: .csv)
# msg = mensagem para o Título da caixa de diálogo
def openFolder_ext(msg, extensao):
    pasta = filedialog.askdirectory(initialdir="d:/", title=msg)
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    arquivosExt = [arq for arq in arquivos if arq.lower().endswith(extensao)]
    return arquivosExt

