import pymysql,sys
class Mesage():
    def __init__(self,name,age,gender,city):
        self.name=name
        self.age=age
        self.gender=gender
        self.city=city
    def showof(self):
        print('姓名{}年龄{}性别{}来自{}'.format(self.name,self.age,self.gender,self.city))
class Manger():
    all_list=[]
    new_list=[]
    all_dict={}
    def __init__(self,version):
        self.version=version
    #创建一个库
    def create_data(self,t):
        connect=pymysql.connect(host='localhost',user='root',password='123')
        cursor=connect.cursor()
        sql='create database {} charset=utf8'.format(t)
        cursor.execute(sql)
        cursor.close()
        connect.close()
    def show_data(self,t):
        connect = pymysql.connect(host='localhost', user='root', password='123')
        cursor = connect.cursor()
        sql = 'show databases'
        cursor.execute(sql)
        all_data=cursor.fetchall()
        #print(all_data)
        if (t,) not in all_data:
            self.create_data(t)
        cursor.close()
        connect.close()
    #创建表
    def create_table(self,t,t1):
        connect = pymysql.connect(host='localhost', user='root', password='123',database=t)
        cursor = connect.cursor()
        sql = 'create table {}(name char(32),age int,gender char(32),city char(32)) charset=utf8'.format(t1)
        cursor.execute(sql)
        cursor.close()
        connect.close()
    def show_table(self,t,t1):

        self.show_data(t)
        connect = pymysql.connect(host='localhost', user='root', password='123', database=t)
        cursor = connect.cursor()
        sql ='show tables'
        cursor.execute(sql)
        all_table=cursor.fetchall()
        if (t1,) not in all_table:
            self.create_table(t,t1)
        cursor.close()
        connect.close()
        self.load(t,t1)
    #加载此表
    def load(self,t,t1):
        connect = pymysql.connect(host='localhost', user='root', password='123', database=t)
        cursor = connect.cursor()
        sql = 'select * from {}'.format(t1)
        cursor.execute(sql)
        all_table = cursor.fetchall()
        for item in all_table:
            Manger.all_list.append(item)
        print(Manger.all_list)
        cursor.close()
        connect.close()
    def save(self,t,t1,t2):
        connect = pymysql.connect(host='localhost', user='root', password='123', database=t)
        cursor = connect.cursor()
        sql = 'insert into {}(name,age,gender,city) value(%s,%s,%s,%s)'.format(t1)
        cursor.execute(sql,t2)
        connect.commit()
        cursor.close()
        connect.close()
    def add(self,t,t1):
        name=input('请输入姓名')
        age=eval(input('请输入年龄'))
        gender=input('请输入性别')
        city=input('请输入城市')
        if name.isalpha() and  gender.isalpha() and city.isalpha():
            mes =Mesage(name,age,gender,city)
            has = 1
            for item in Manger.all_list:
                if mes.name == item[0] :
                    has = 0
            if has == 1:
                print('添加信息成功')
                Manger.new_list.append(mes)
            else:
                print('此信息重复，请重新输入')
        else:
            print('输入有误，重新输入')
    def sava_data(self,t,t1):
        for j in range(len(Manger.new_list)):
            # print(i)
            one = Manger.new_list[j]
            if isinstance(one, Mesage):
                t2 = (one.name, one.age, one.gender, one.city)
                if t2 not in Manger.all_list:
                    print(t2)
                    # print(one)
                    self.save(t,t1,t2)
    def func(self):
        list1 = []
        for item in Manger.all_list:
            # if item[3] not in Manger.all_dict:
            #     Manger.all_dict[item[3]] = 1
            # else:
            #     Manger.all_dict[item[3]] += 1
            list1.append(item[3])
        for i in list1:
                Manger.all_dict[i]=list1.count(i)
        print(Manger.all_dict)
    def showmain(self):
        print('欢迎使用添加信息{}版本'.format(self.version))
    def exit(self,t,t1):
        print('谢谢使用')
        self.sava_data(t, t1)
        sys.exit()
def test():
    t='mesage'
    t1='user'
    manger = Manger(2.0)
    manger.showmain()
    manger.show_table(t, t1)
    while True:
        ret = input('请您你选择1添加2退出')
        if ret=='1':
            manger.func()
            manger.add(t,t1)
        elif ret=='2':
            manger.exit(t,t1)
test()









# manger.show_table('mesage','user')
# manger.add()





