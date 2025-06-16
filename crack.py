import codecs
import subprocess
import time
import multiprocessing
import itertools
from csv import excel
from idlelib.replace import replace
from operator import length_hint
from subprocess import Popen
import os
from Tools.scripts.objgraph import ignore
import threading

# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
def func(length):
    for i in itertools.product('0123456789',repeat=int(length)):
        try:
            command = fr'C:\WinRAR\Unrar.exe x C:\examp.rar example.txt -p{"".join(i)}'
            process = subprocess.call(command, timeout=3, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL,shell=True, encoding='cp866')
            print(''.join(i))
        except subprocess.TimeoutExpired:
            print('Пароль:', ''.join(i))
            exit(1)

def check(processes):
    while all(1 for i in processes if i.is_alive()):
        return True
    for p in processes:
        p.terminate()

if __name__ == '__main__':
    processes = []
    for length in range(2,5):
        p = multiprocessing.Process(target=func, args=str(length))
        c =  multiprocessing.Process(target=check, args=processes)
        processes.append(p)
        p.start()
        c.start()
