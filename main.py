# coding:utf-8

import menu
import data

menu.ShowMenu()
with open('Database.data','r') as f:
    print(f.read())