import pyautogui as pg
import time
import keyboard as kb
import os

#Contantes
largura, altura = pg.size()
centro_x = largura / 2
centro_y = altura / 2
pg.PAUSE = 0.3
FRAME2 = 0.1
TIME1 = 4
TIME2 = 4
WAY_EDD = r'\\192.168.1.249\redacao\diagramacao\edicao'
WAY_WEB = r'\\192.168.1.249\redacao\web'

#variáveis
EDD = r"0001 - TESTE"

#funções
def max_windows():
    kb.press_and_release('alt+space')
    time.sleep(0.2)
    kb.press_and_release('x')

def take_file(arquivo):
    kb.press_and_release('ctrl+f')
    time.sleep(0.5)
    kb.write(str(arquivo))
    time.sleep(2)
    pg.click(centro_x, centro_y)
    pg.press('down')
    time.sleep(0.3)
    pg.press('down')
    time.sleep(0.3)
    kb.press_and_release('enter')

def open_web():
    os.startfile(WAY_WEB + "\\" + EDD)
    time.sleep(0.9)
    max_windows()

#funções-específicas
def close_and_open_quark():
    kb.press_and_release('alt+f4')
    pg.hotkey('win', '1')
    time.sleep(TIME2)

def take_tool(tool):
    pg.click(centro_x, 10)
    kb.press(str(tool))

def confirmancia():
    pg.press('down')
    pg.press('enter')
    
def open_paste_page_done():
    pg.press('esc')
    take_tool("v")
    pg.hotkey('ctrl', '0')
    pg.hotkey('ctrl', 'o')
    kb.write(WAY_EDD + "\\" + EDD + "\\" + 'Páginas prontas')
    pg.press('enter')

def agrupar_e_fechar_agora():
    take_tool("v")
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'g')
    pg.hotkey('ctrl', 's')
    pg.hotkey('ctrl', 'c')
    pg.hotkey('ctrl', 'f4')

def move_page(left, right):
    pg.hotkey('ctrl', 'shift', 'alt', 'm')
    time.sleep(FRAME2)
    kb.write(str(left))
    time.sleep(FRAME2)
    pg.press('tab')
    time.sleep(FRAME2)
    kb.write(str(right))
    pg.press('enter')
    time.sleep(FRAME2)
    pg.press('down')
    time.sleep(FRAME2)
    pg.press('up')
    
def process_page(page_number, is_even):
    open_paste_page_done()
    pg.write(str(page_number))
    confirmancia()
    time.sleep(TIME1)
    agrupar_e_fechar_agora()
    time.sleep(TIME1)
    pg.hotkey('ctrl', '0')
    pg.click(centro_x, centro_y)
    pg.hotkey('ctrl', 'v')
    time.sleep(TIME1)
    if is_even: 
        move_page(10, 20) 
    else: 
        move_page(290, 20)
    pg.hotkey('ctrl', 's')

def process_casamento(nome_arquivo, paginas):
    open_web()
    take_file(nome_arquivo)
    close_and_open_quark()

    for page_number in paginas:
        is_even = page_number % 2 == 0
        process_page(page_number, is_even)

def process_casamento_basico():
    process_casamento("17_20", [20, 17])
    process_casamento("13_16", [13, 16])
    process_casamento("14_15", [14, 15])
    process_casamento("9_12", [9, 12])
    process_casamento("10_11", [10, 11])

def process_casamento_miolo():
    process_casamento("4_5", [4, 5])
    process_casamento("3_6", [3, 6])
    process_casamento("2_7", [2, 7])

def process_casamento_capa():
    process_casamento("1_8", [1, 8])

def process_casamento_primeiro_caderno():
    process_casamento_miolo()
    process_casamento_capa()
    
def process_casamento_completo():
    process_casamento_basico()
    process_casamento_primeiro_caderno()

process_casamento_basico()
process_casamento_miolo()
process_casamento_capa()