



import os
import sys
import time
from time import sleep

p = "\033[37;1m"

def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/90)

os.system("clear")
start=(p+"""
ーーーーーーーーーーーーーーーーー
 ____ _____  _    ____ _____
/ ___|_   _|/ \  |  _ \_   _|
\___ \ | | / _ \ | |_) || |
 ___) || |/ ___ \|  _ < | |
|____/ |_/_/   \_\_| \_\|_| 
ーーーーーーーーーーーーーーーーー
""")
slowprints(start)
slowprints("INSTALL SEKARANG ?")
input('\n   Tekan ENTER -»')
sleep(1)
slowprints("     Sedang Memproses•••••")
sleep(2)
try:
      os.mkdir("/data/data/com.termux/files/home/.termux")
except:
      pass
slowprints("ーSelesai")
sleep(3)
slowprints("     Memasang File•••••")
sleep(1)

shortcutkey = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
script = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
script.write(shortcutkey)
script.close()
sleep(1)
slowprints("ーSelesai")
sleep(2)
slowprints("     MENGATUR File•••••")
sleep(2)
os.system("termux-reload-settings")
slowprints("\nーSelesai")
os.system('exit')
os.system('clear')
os.system('login')
