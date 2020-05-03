import os
import subprocess
import time
from threading import Thread
import ctypes

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_HIDE = 0

hWnd = kernel32.GetConsoleWindow()


def get_tasks(action):
    list = os.popen('tasklist').read().strip().split('\n')
    if action == "length":
        return len(list)
    elif action == "list":
        return list
    else:
        raise ValueError("Invalid input to 'get_tasks' on argument 'action'.")


def kill_task(task):
    killcmd = r"TASKKILL /F /IM %s" % task
    os.system(killcmd)


def recursive_kill(task):
    while True:
        time.sleep(1)
        r = os.popen('tasklist').read().strip().split('\n')
        for i in range(len(r)):
            if task in r[i]:
                kill_task(task)
                print("killed")


def home():
    e = input("Valid Commands: 'list', 'list_len', 'kill *app*', 'recursive_kill' *app*, 'stop'\n")
    d = e.split(" ")
    if d[0] == "list":
        print(get_tasks("list"))
        home()
    elif d[0] == "list_len":
        print(get_tasks("length"))
        home()
    elif d[0] == "kill":
        kill_task(d[1])
        home()
    elif d[0] == "recursive_kill":
        if hWnd:
            user32.ShowWindow(hWnd, SW_HIDE)
        for i in d[1].split(" "):
            Thread(target=recursive_kill(i)).start()
    else:
        print("Invalid Input")
        home()



home()