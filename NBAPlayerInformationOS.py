# -*- coding: utf-8 -*-
# System version: Alpha 1.1
def Showmenu():
    print('---------------------------------------')
    print('|    N B A 球 员 数 据 查 询 系 统    |')
    print('|                        --Alpha 1.1  |')
    print('---------------------------------------')
    print('|   1.  增   加   球   员   信   息   |')
    print('|   2.  删   除   球   员   信   息   |')
    print('|   3.  更   改   球   员   信   息   |')
    print('|   4.  查   询   球   员   信   息   |')
    print('|   5.  显   示   所   有   信   息   |')
    print('|   0.  退     出        系      统   |')
    print('---------------------------------------')

def Showdata():
    print('------------------------')
    print('姓名:',list[i]['姓名'])
    print('球队:',list[i]['球队'])
    print('球衣号码:',list[i]['球衣号码'])
    print('擅长位置:',list[i]['位置'])
    print('身高:',list[i]['身高'])
    print('------------------------\n')

Showmenu()

f = open('DataTest.data',encoding='utf-8')
list = eval(f.read())
f.close()

while(True):
    command = input("请输入要进行的操作:")
    if command == '1':
        message = {}
        message['姓名'] = input('请输入要添加的球员姓名:')
        message['球队'] = input('请输入球员所属球队:')
        message['球衣号码'] = input('请输入球员的球衣号码:')
        message['位置'] = input('请输入球员擅长位置:')
        message['身高'] = input('请输入球员身高:')
        list.append(message)
        f = open('DataTest.data','w',encoding='utf-8')
        f.write(str(list))
        f.close()
    
    elif command == '2':
        name = input('请输入要删除的球员的姓名:')
        i = 0
        length = len(list)
        while i <length:
            if list[i]['姓名'] == name:
                del list[i]
                f = open('DataTest.data','w',encoding='utf-8')
                f.write(str(list))
                f.close()
            i += 1
    
    elif command == '3':
        name = input('请输入要修改的球员的姓名:')
        i = 0
        length = len(list)
        while i < length:
            if list[i]['姓名'] == name:
                list[i]['球队'] = input('请输入球员现役球队:')
                list[i]['球衣号码'] = input('请输入球员现在的球衣号码:')
                list[i]['位置'] = input('请输入球员现在担任的位置:')
                list[i]['身高'] = input('请输入球员现在的身高:')
                f = open('DataTest.data','w',encoding='utf-8')
                f.write(str(list))
                f.close()
                Showdata()
            i += 1
            print('\n\n')
    
    elif command == '4':
        name = input('请输入要查询的球员的姓名:')
        i = 0
        length = len(list)
        while i < length:
            if list[i]['姓名'] == name:
                Showdata()
                f = open('DataTest.data',encoding='utf-8')
                f.read()
                f.close()
            i += 1
        Showmenu()
        print('\n\n')
    
    elif command == '5':
        i = 0
        length = len(list)
        while i < length:
            Showdata()
            f = open('DataTest.data',encoding='utf -8')
            f.read()
            f.close()
            i += 1
        Showmenu()

    elif command == '0':
        break
    
    else:
        print('输入错误，请重新输入!')
