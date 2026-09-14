import os
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
from hashlib import sha512
import sys

USER_NAME = os.getenv('USER')
if USER_NAME == 'root':
    print('不要使用root权限运行!')
    sys.exit()
ORIG_JICHOU_FILE = '/Users/%s/Library/Application Support/com.biantou.jichou/framework/password/' % USER_NAME
jichou_file = ORIG_JICHOU_FILE
com_biantou_jichou = '/Users/%s/Library/Application Support/com.biantou.jichou/' % USER_NAME
unlock = False
if os.path.exists(os.path.join(com_biantou_jichou, 'framework', 'PASSWORD-HASH.txt')):
    with open(os.path.join(com_biantou_jichou, 'framework', 'PASSWORD-HASH.txt'), 'r') as file:
        PASSWORD = file.read()
else:
    PASSWORD = None

if not os.path.exists(com_biantou_jichou):
    os.mkdir(com_biantou_jichou)
if not os.path.exists(os.path.join(com_biantou_jichou, 'framework')):
    os.mkdir(os.path.join(com_biantou_jichou, 'framework'))
if not os.path.exists(os.path.join(com_biantou_jichou, 'framework', 'password')):
    os.mkdir(os.path.join(com_biantou_jichou, 'framework', 'password'))
    root_path = os.path.join(com_biantou_jichou, 'framework', 'password')

    print('请设置初始密码!')
    print('密码必须4位数!')

    while True:
        user_input = input('password: ')
        if len(user_input) == 4:
            break
        else:
            print('密码必须4位数!')
    jichou_file = os.path.join(jichou_file, '/'.join(user_input), 'data.jichou')

    for i in range(1, 10):
        os.mkdir(os.path.join(root_path, str(i)))
    for i in range(1, 10):
        for j in range(1, 10):
            path = os.path.join(root_path, str(i))
            os.mkdir(os.path.join(path, str(j)))
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                path = os.path.join(root_path, str(i), str(j))
                os.mkdir(os.path.join(path, str(k)))
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                for l in range(1, 10):
                    path = os.path.join(root_path, str(i), str(j), str(k))
                    os.mkdir(os.path.join(path, str(l)))

    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                for l in range(1, 10):
                    if '%d%d%d%d' % (i, j, k, l) != user_input:
                        with open(os.path.join(root_path, str(i), str(j), str(k), str(l), '密码错误'), 'w') as file:
                            file.write('密码错误')

    with open(os.path.join(com_biantou_jichou, 'framework', 'PASSWORD-HASH.txt'), 'w') as file:
        file.write(sha512(user_input.encode('utf-8')).hexdigest())

    PASSWORD = sha512(user_input.encode('utf-8')).hexdigest()

if not os.path.exists(os.path.join(com_biantou_jichou, 'framework', 'readme.txt')):
    with open(os.path.join(com_biantou_jichou, 'framework', 'readme.txt'), 'w') as file:
        context = """查看记仇文件, 需要输入密码
    
    请进入"password"文件夹, 然后输入密码"""
        file.write(context)

if 'api' in sys.argv:
    if 'check_password' in sys.argv:
        user_password = sys.argv[3]
        if sha512(user_password.encode('utf-8')).hexdigest() == PASSWORD:
            print('1')
        else:
            print('0')
        sys.exit()

    if 'new' in sys.argv:
        people = sys.argv[3]
        time = sys.argv[4]
        thing = sys.argv[5]
        user_password = sys.argv[6]
        jichou_file = os.path.join(jichou_file, '/'.join(user_password), 'data.jichou')
        try:
            with open(jichou_file, 'a') as file:
                file.write('\n')
                file.write('%s|%s|%s' % (people, time, thing))
            print('成功')
        except Exception as e:
            print(e)
        sys.exit()

    if 'del' in sys.argv:
        try:
            index = int(sys.argv[3])
        except Exception as e:
            print(e)
            sys.exit()
        user_password = sys.argv[4]
        jichou_file = os.path.join(jichou_file, '/'.join(user_password), 'data.jichou')
        items = []
        try:
            with open(jichou_file, 'r') as file:
                for line in file:
                    items.append(line)
        except Exception as e:
            print(e)
            sys.exit()
        items.pop(index - 1)
        new_items = []
        for item in items:
            new_items.append(item.rstrip('\n'))
        context = '\n'.join(new_items)
        try:
            with open(jichou_file, 'w') as file:
                file.write(context.strip('\n'))
        except Exception as e:
            print(e)
            sys.exit()
        print('成功')
        sys.exit()

    if 'show' in sys.argv:
        user_password = sys.argv[3]
        jichou_file = os.path.join(jichou_file, '/'.join(user_password), 'data.jichou')
        items = []
        try:
            with open(jichou_file, 'r') as file:
                for line in file:
                    items.append(line)
        except Exception as e:
            print(e)
            sys.exit()
        print(''.join(items))
        sys.exit()

    if 'help' in sys.argv:
        print('api new [people] [time] [thing] [password]')
        print('api del [index] [password]')
        print('api show [password]')

if len(sys.argv) > 1:
    if 'new' in sys.argv:
        print('====记仇本====')
        print('--添加一条--')
        print('请输入密码:')
        while True:
            user_input = input('password: ')
            if sha512(user_input.encode('utf-8')).hexdigest() == PASSWORD:
                jichou_file = os.path.join(jichou_file, '/'.join(user_input), 'data.jichou')
                break
            else:
                print('密码错误,请重试!')
        print('开始记仇')
        people = input('仇人名字: ')
        time = input('发生时间: ')
        thing = input('发生的事情: ')
        print('请核对信息:\n仇人:%s\n时间:%s\n事情:%s\n[y/n]' % (people, time, thing))
        user_choice = input('input: ').lower() == 'y'
        if user_choice:
            try:
                with open(jichou_file, 'a') as file:
                    file.write('\n')
                    file.write('%s|%s|%s' % (people, time, thing))
                print('成功添加,即将退出程序...')
            except Exception as e:
                print(e)
        else:
            print('你取消了选择,即将退出程序...')
        print('程序退出')
        sys.exit()

    if 'del' in sys.argv:
        print('====记仇本====')
        print('--删除一条--')
        print('请输入密码:')
        while True:
            user_input = input('password: ')
            if sha512(user_input.encode('utf-8')).hexdigest() == PASSWORD:
                jichou_file = os.path.join(jichou_file, '/'.join(user_input), 'data.jichou')
                break
            else:
                print('密码错误,请重试!')
        print('请选择删除项')
        num = 0
        items = []
        try:
            with open(jichou_file, 'r') as file:
                for line in file:
                    num += 1
                    data = line.rstrip()
                    name, time, thing = data.split('|')
                    print('%d   %s   %s   %s' % (num, name, time, thing))
                    items.append(line)
        except Exception as e:
            print(e)
        print('请选择要删除的项')
        num = input('编号: ')
        try:
            num = int(num)
            print('确定要删除此项吗?')
            line = items[num - 1]
            data = line.rstrip()
            name, time, thing = data.split('|')
            print('%d   %s   %s   %s' % (num, name, time, thing))
            print('[y/n]')
            user_choice = input('input: ').lower() == 'y'
            if user_choice:
                items.pop(num - 1)
                new_items = []
                for item in items:
                    new_items.append(item.rstrip('\n'))
                context = '\n'.join(new_items)
                with open(jichou_file, 'w') as file:
                    file.write(context.strip('\n'))
                print('删除成功')
            else:
                print('你取消了选择')
        except ValueError:
            print('请输入正确的值')
        except Exception as e:
            print(e)
        print('程序退出')
        sys.exit()

    if 'show' in sys.argv:
        print('====记仇本====')
        print('--显示内容--')
        print('请输入密码:')
        while True:
            user_input = input('password: ')
            if sha512(user_input.encode('utf-8')).hexdigest() == PASSWORD:
                jichou_file = os.path.join(jichou_file, '/'.join(user_input), 'data.jichou')
                break
            else:
                print('密码错误,请重试!')
        print('\n====记仇内容====')
        num = 0
        try:
            with open(jichou_file, 'r') as file:
                for line in file:
                    num += 1
                    data = line.rstrip()
                    name, time, thing = data.split('|')
                    num_space_name = 20 - (len(name) * 2) - (len(str(num)) - 1)
                    name_space_time = 20 - len(time)
                    time_space_thing = 30 - (len(thing) * 2)
                    print('%d%s%s%s%s%s%s' % (num, ' ' * num_space_name, name, ' ' * name_space_time, time, ' ' * time_space_thing, thing))
        except Exception as e:
            print(e)
        print('程序退出')
        sys.exit()

    if 'rank' in sys.argv:
        print('====记仇本====')
        print('--排行榜--')
        print('请输入密码:')
        while True:
            user_input = input('password: ')
            if sha512(user_input.encode('utf-8')).hexdigest() == PASSWORD:
                jichou_file = os.path.join(jichou_file, '/'.join(user_input), 'data.jichou')
                break
            else:
                print('密码错误,请重试!')

        print('====排行榜====')


        def term_rank_sort(values):
            a = {}
            for i in values:
                if i in a:
                    a[i] += 1
                else:
                    a[i] = 1
            return dict(sorted(a.items(), key=lambda x: x[1], reverse=True))


        c = 0
        all_people = []
        try:
            with open(jichou_file, 'r') as file:
                for line in file:
                    people, _, _ = line.rstrip().split('|')
                    all_people.append(people)
                rank = term_rank_sort(all_people)
                c = 0
                for people, count in rank.items():
                    c += 1
                    c_space_people = ' ' * (20 - (len(people) * 2) - 4 - len(str(c)))
                    people_space_count = ' ' * (40 - (len(people) * 2) - 6 - len(str(c)) - len(str(count)))
                    print('第%d名%s%s%s%d次' % (c, c_space_people, people, people_space_count, count))
        except Exception as e:
            print(e)

        print('\n程序退出')
        sys.exit()

    if 'version' in sys.argv:
        changelogs = {'v1.0': '基础gui功能',
                      'v2.0': '重写了删除逻辑',
                      'v3.0': '添加了命令行功能new',
                      'v4.0': '添加了排行榜(仅gui)',
                      'v5.0': '命令行del, show, help',
                      'v6.0': '现在数据将储存到~/Library/Application Support/com.biantou.jichou/framework/password/(password加斜杠)/data.jichou',
                      'v7.0': '自动生成和自定义密码',
                      'v8.0': 'rank命令',
                      'v9.0': 'version命令',
                      'v10.0': '格式化rank show version命令输出',
                      'v11.0': '增加了适合外部程序的api, 可用python3 %s api help查询, 不要用jichou命令调用api' % __file__}
        print('===记仇本===')
        print('版本: v9.0')
        print('作者: biantou')
        print('=' * 30)
        print('以下为更新日志:')
        for key, value in changelogs.items():
            key_space_colon = ' ' * (10 - len(key) - 1)
            print('%s%s: %s' % (key, key_space_colon, value))
        print('\n程序退出')
        sys.exit()

    if 'help' in sys.argv:
        print('===记仇本===')
        print('使用: jichou [new] [del] [show] [rank] [help] [version]')
        print('\nnew: 新增一条')
        print('del: 选择一条并删除')
        print('show: 显示所有记仇信息')
        print('rank: 显示排行榜')
        print('help: 显示此帮助信息')
        print('version: 显示版本信息')
        print('\n程序退出')
        sys.exit()

    print('===记仇本===')
    argv = sys.argv.copy()
    if 'term' in argv:
        argv.remove('term')
    if 'python' in argv:
        argv.remove('python')
    if 'python3' in argv:
        argv.remove('python3')
    for path in sys.path:
        if path in argv:
            argv.remove(path)
    if __file__ in argv:
        argv.remove(__file__)
    if len(argv) > 0:
        print('错误的参数: %s' % ', '.join(argv))
    print('使用: jichou [new] [del] [show] [rank] [help] [version]')
    print('\nnew: 新增一条')
    print('del: 选择一条并删除')
    print('show: 显示所有记仇信息')
    print('rank: 显示排行榜')
    print('help: 显示此帮助信息')
    print('version: 显示版本信息')
    print('\n程序退出')
    sys.exit()


def read():
    global unlock, jichou_file
    try:
        if not unlock:
            user_input = sd.askstring('记仇本已锁定', '请输入密码')
            if user_input is not None:
                if sha512(user_input.encode('utf-8')).hexdigest() == PASSWORD:
                    if jichou_file == ORIG_JICHOU_FILE:
                        jichou_file = os.path.join(jichou_file, '/'.join(user_input), 'data.jichou')
                        print('111')
                    unlock = True
                else:
                    mb.showinfo('提示', '密码错误')
                    root.after(10, read)
                    return
            else:
                mb.showinfo('提示', '你没输密码,即将退出程序')
                root.quit()
                return
        print(jichou_file)
        for item in tree.get_children():
            tree.delete(item)
        with open(jichou_file, 'r') as file:
            for line in file:
                data = line.rstrip()
                datas = data.split('|')
                tree.insert('', tk.END, text='#%d' % (len(tree.get_children()) + 1), values=tuple(datas))
    except FileNotFoundError:
        with open(jichou_file, 'w') as file:
            file.write('0|0|0')
        root.after(100, read)
    except Exception as e:
        print(e)
    root.focus_force()


def delete():
    row = tree.selection()
    if row is not None:
        user_choice = mb.askyesno('提示', '你确定要删除此项吗')
        if not user_choice:
            return
        tree.delete(row[0])
        context = []
        items = tree.get_children()
        for item in items:
            i = tree.item(item, 'values')
            context.append('|'.join(i))
        new_context = []
        for line in context:
            new_context.append(line.rstrip('\n') + '\n')
        temp = new_context.pop(-1)
        new_context.append(temp.rstrip('\n'))
        try:
            with open(jichou_file, 'w') as file:
                for line in new_context:
                    file.write(line)
        except Exception as e:
            mb.showerror('错误', '%s:%s' % (type(e).__name__, e))
    root.focus_force()


def get_select():
    if len(tree.selection()) == 0:
        return None
    all_rows = tree.get_children()
    select_row = tree.selection()[0]
    row_num = all_rows.index(select_row)
    return row_num


def new():
    people = sd.askstring('提示', '请输入仇人名字')
    if people is None:
        mb.showinfo('提示', '你取消了输入')
        return
    time = sd.askstring('提示', '请输入事情发生时间')
    if time is None:
        mb.showinfo('提示', '你取消了输入')
        return
    thing = sd.askstring('提示', '请输入发生的事情')
    if thing is None:
        mb.showinfo('提示', '你取消了输入')
        return
    user_choice = mb.askyesno('提示', '请核对信息:\n仇人:%s\n时间:%s\n事情:%s' % (people, time, thing))
    if user_choice:
        try:
            with open(jichou_file, 'a') as file:
                file.write('\n')
                file.write('%s|%s|%s' % (people, time, thing))
        except Exception as e:
            print(e)
        mb.showinfo('提示', '成功添加,点击确定后更新数据')
        root.after(100, read)
    else:
        mb.showinfo('提示', '你取消了选择')
    root.focus_force()

def add_to_shell():
    mb.showinfo('提示', '请在终端rc文件里面添加alias jichou="%s %s term"' % (sys.executable, __file__))


class Rank:
    def __init__(self):
        self.win = tk.Toplevel(root)
        self.tree = ttk.Treeview(self.win, columns=('people', 'count'), height=12)
        self.tree.heading('#0', text='名次')
        self.tree.heading('people', text='仇人')
        self.tree.heading('count', text='次数')
        self.tree.column('people', width=250)
        self.tree.column('count', width=250)
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.show()

    def show(self):
        c = 0
        all_people = []
        for i in [tree.item(item, 'values') for item in tree.get_children()]:
            people, _, _ = i
            all_people.append(people)
        rank = self.sort(all_people)
        c = 0
        for people, count in rank.items():
            c += 1
            self.tree.insert('', 'end', text='第%d名' % c, values=(people, count))

    def sort(self, values):
        a = {}
        for i in values:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        return dict(sorted(a.items(), key=lambda x: x[1], reverse=True))


root = tk.Tk()
root.title('记仇本')
root.configure(bg='#0000c8')

title = tk.Label(root, text='记仇本', bg='#0000c8', fg='white', font=('Arial', 30))
title.pack()

style = ttk.Style()
style.configure('Treeview.Heading', font=('Arial', 20))
style.configure('Treeview', font=('Arial', 20), rowheight=40)
style.map('Treeview', background=[('selected', '#0000c8')])

tree = ttk.Treeview(root, columns=('people', 'time', 'thing'), height=10)
tree.heading('#0', text='序号')
tree.heading('people', text='仇人')
tree.heading('time', text='记仇时间')
tree.heading('thing', text='发生的事')
tree.column('people', width=250)
tree.column('time', width=250)
tree.column('thing', width=250)
tree.pack(fill=tk.BOTH, expand=True)

new_btn = tk.Button(root, text='添加一项', command=new, font=('Arial', 20))
new_btn.pack(fill=tk.X, padx=50)
re_btn = tk.Button(root, text='刷新列表', command=read, font=('Arial', 20))
re_btn.pack(fill=tk.X, padx=50)
del_btn = tk.Button(root, text='删除选中项', command=delete, font=('Arial', 20))
del_btn.pack(fill=tk.X, padx=50)
rank_btn = tk.Button(root, text='排行榜', command=lambda: Rank(), font=('Arial', 20))
rank_btn.pack(fill=tk.X, padx=50)
add_to_shell_btn = tk.Button(root, text='添加到终端', font=('Arial', 20), command=add_to_shell)
add_to_shell_btn.pack(fill=tk.X, padx=50)
tk.Label(root, text='君子报仇，十年不晚。                              ——《史记》', font=('Arial', 20), fg='white', bg='#0000c8', anchor=tk.W).pack(fill=tk.X, padx=10, expand=True, anchor=tk.W)

root.after(100, read)

root.focus_force()
root.mainloop()
