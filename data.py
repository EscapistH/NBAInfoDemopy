# coding:utf-8

with open('DataTest.data','r',encoding='utf-8') as f:
    list = eval(f.read())

def createData(name):
        message = {}
        message['姓名'] = name
        message['球队'] = input('请输入球员所属球队:')
        message['球衣号码'] = input('请输入球员的球衣号码:')
        message['位置'] = input('请输入球员擅长位置:')
        message['身高'] = input('请输入球员身高:')
        list.append(message)
        with open('DataTest.data','w',encoding='utf-8') as f:
            f.write(str(list))
        print('添加成功!\n')

def delteData(name):
    i = 0
    length = len(list)
    while i < length:
        if list[i]['姓名'] == name:
            flag = input('已找到'+name+'的数据,确认删除请输入Y,否则请按任意键.')
            if flag == 'Y':
                del list[i]
                print('删除成功!\n')
                with open('DataTest.data','w',encoding='utf-8') as f:
                    f.write(str(list))
            else:
                print('用户取消!\n')
        else:
            if i == (length-1):
                print('未查询到'+name+'的数据,操作失败.\n')
        i += 1

def changeTeam(name):
    i = 0
    length = len(list)
    while i < length:
        if list[i]['姓名'] == name:
            list[i]['球队'] = input('请输入球员现役球队:')
            with open('DataTest.data','w',encoding='utf-8') as f:
                f.write(str(list))
            print('修改成功!\n')
        i += 1

def changeNumber(name):
    i = 0
    length = len(list)
    while i < length:
        if list[i]['姓名'] == name:
            list[i]['球衣号码'] = input('请输入球员现在的球衣号码:')
            with open('DataTest.data','w',encoding='utf-8') as f:
                f.write(str(list))
            print('修改成功!\n')
        i += 1

def changeSeat(name):
    i = 0
    length = len(list)
    while i < length:
        if list[i]['姓名'] == name:
            list[i]['位置'] = input('请输入球员现在担任的位置:')
            with open('DataTest.data','w',encoding='utf-8') as f:
                f.write(str(list))
            print('修改成功!\n')
        i += 1

def changeHeight(name):
    i = 0
    length = len(list)
    while i < length:
        if list[i]['姓名'] == name:
            list[i]['身高'] = input('请输入球员现在的身高:')
            with open('DataTest.data','w',encoding='utf-8') as f:
                f.write(str(list))
            print('修改成功!\n')
        i += 1

def changeAll(name):
    i = 0
    length = len(list)
    while i < length:
        if list[i]['姓名'] == name:
            list[i]['球队'] = input('请输入球员现役球队:')
            list[i]['球衣号码'] = input('请输入球员现在的球衣号码:')
            list[i]['位置'] = input('请输入球员现在担任的位置:')
            list[i]['身高'] = input('请输入球员现在的身高:')
            with open('DataTest.data','w',encoding='utf-8') as f:
                f.write(str(list))
            print('修改成功!\n')
        i += 1

def searchData(name):
    i = 0
    length = len(list)
    while i < length:
        if list[i]['姓名'] == name:
            print('\n+------------+--------------------+')
            print('|  姓    名  | ',list[i]['姓名'])
            print('+------------+--------------------+')
            print('|  球    队  | ',list[i]['球队'])
            print('+------------+--------------------+')
            print('|  球衣号码  | ',list[i]['球衣号码'])
            print('+------------+--------------------+')
            print('|  擅长位置  | ',list[i]['位置'])
            print('+------------+--------------------+')
            print('|  身    高  | ',list[i]['身高'])
            print('+------------+--------------------+\n')
            with open('DataTest.data','r',encoding='utf-8') as f:
                f.read()
                break
        else:
            if i == (length-1):
                print('未查询到'+name+'的数据.\n')
        i += 1

def searchAll():
    i = 0
    length = len(list)
    while i < length:
        print('\n+------------+--------------------+')
        print('|  姓    名  | ',list[i]['姓名'])
        print('+------------+--------------------+')
        print('|  球    队  | ',list[i]['球队'])
        print('+------------+--------------------+')
        print('|  球衣号码  | ',list[i]['球衣号码'])
        print('+------------+--------------------+')
        print('|  擅长位置  | ',list[i]['位置'])
        print('+------------+--------------------+')
        print('|  身    高  | ',list[i]['身高'])
        print('+------------+--------------------+\n')
        with open('DataTest.data','r',encoding='utf-8') as f:
            f.read()
        i += 1
