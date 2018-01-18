# coding:utf-8

import menu
import data

menu.mainMenu()

with open('DataTest.data','r',encoding='utf-8') as f:
    list = eval(f.read())

def main():
    while(True):

        command = input('请输入要进行的操作(输入9可以呼出菜单):')
        if command == '1':
            # 增加
            print('\n')
            name = input('请输入要添加的球员姓名:')
            i = 0
            length = len(list)
            while i < length:
                if list[i]['姓名'] == name:
                    print('已查询到'+name+'的数据,添加失败!')
                    flag = input('要显示'+name+'的数据请输入Y,否则请按任意键退出.')
                    if flag == 'Y':
                        data.searchData(name)
                        break
                    else:
                        print('用户取消!\n')
                        break
                else:
                    if i == (length-1):
                        data.createData(name)
                i += 1

        elif command == '2':
            # 删除
            print('\n')
            name = input('请输入要删除数据的球员姓名:')
            data.delteData(name)

        elif command == '3':
            # 改变
            print('\n')
            name = input('请输入要修改数据的球员姓名:')
            i = 0
            length = len(list)
            while i < length:
                if list[i]['姓名'] != name:
                    if i == (length-1):
                        print('未查询到'+name+'的数据!\n')
                else:
                    print('-------------')
                    print(' 1. 球队\n 2. 球衣号码\n 3. 位置\n 4. 身高\n 5. 以上所有\n 0. 取消')
                    print('-------------')
                    key = input('请输入要修改的数据:')
                    if key == '1':
                        data.changeTeam(name)
                        break
                    
                    elif key == '2':
                        data.changeNumber(name)
                        break

                    elif key == '3':
                        data.changeSeat(name)
                        break

                    elif key == '4':
                        data.changeHeight(name)
                        break

                    elif key == '5':
                        data.changeAll(name)
                        break
                    
                    elif key == '0':
                        break
                i += 1

        elif command == '4':
            # 查询某一条数据
            print('\n')
            name = input('请输入要查询的球员姓名:')
            data.searchData(name)

        elif command == '5':
            # 查询所有数据
            data.searchAll()

        elif command == '9':
            # 显示菜单
            menu.mainMenu()

        elif command == '0':
            # 退出
            break

        else:
            print('输入错误,请重新输入!')

if __name__ == '__main__':
    main()